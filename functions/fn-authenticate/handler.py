import json
import os
import time
import bcrypt
import pyotp
import psycopg2
from cryptography.fernet import Fernet

# Constante pour définir la limite de 6 mois d'ancienneté (en secondes)
# 6 mois = 6 * 30 jours * 24 heures * 3600 secondes = 15 552 000 secondes
SIX_MONTHS_SECONDS = 6 * 30 * 24 * 3600

def get_fernet():
    key = os.environ.get("ENCRYPTION_KEY")
    if not key:
        key = "MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI="
    return Fernet(key.encode('utf-8') if isinstance(key, str) else key)

def decrypt_secret(encrypted_token: str) -> str:
    f = get_fernet()
    return f.decrypt(encrypted_token.encode('utf-8')).decode('utf-8')

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        port=os.environ.get("DB_PORT", "5432"),
        database=os.environ.get("DB_NAME", "cofrap_db"),
        user=os.environ.get("DB_USER", "postgres_user"),
        password=os.environ.get("DB_PASSWORD", "postgres_password")
    )

def handle(event, context):
    # Gérer les requêtes CORS Preflight (OPTIONS)
    if event.method == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": ""
        }

    try:
        body_str = event.body.decode('utf-8') if isinstance(event.body, bytes) else event.body
        data = json.loads(body_str) if body_str else {}
    except Exception:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Requête malformée. JSON attendu."})
        }

    # Accepter 'login' ou 'username' pour être flexible
    username = data.get("username") or data.get("login")
    password = data.get("password")
    code_2fa = data.get("code")

    if not username or not password or not code_2fa:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Les paramètres 'username'/'login', 'password' et 'code' sont requis."})
        }

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Récupérer l'utilisateur
        cur.execute("""
            SELECT password, mfa, gendate, expired 
            FROM users 
            WHERE username = %s;
        """, (username,))
        
        user_row = cur.fetchone()
        
        if not user_row:
            cur.close()
            conn.close()
            return {
                "statusCode": 401,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"status": "unauthorized", "message": "Identifiants incorrects (utilisateur introuvable)."})
            }
            
        hashed_password_db, encrypted_mfa_db, gendate, expired = user_row
        
        # 1. Vérification du mot de passe
        if not check_password(password, hashed_password_db):
            cur.close()
            conn.close()
            return {
                "statusCode": 401,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"status": "unauthorized", "message": "Identifiants ou code MFA incorrects (mot de passe invalide)."})
            }

        # 2. Vérification de l'ancienneté (6 mois maximum) ou si déjà marqué comme expiré
        now = int(time.time())
        age_seconds = now - gendate
        
        if expired == 1 or age_seconds > SIX_MONTHS_SECONDS:
            # Marquer comme expiré si ce n'est pas déjà fait
            if expired == 0:
                cur.execute("UPDATE users SET expired = 1 WHERE username = %s;", (username,))
                conn.commit()
            
            cur.close()
            conn.close()
            
            return {
                "statusCode": 403,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({
                    "status": "expired",
                    "message": "Vos identifiants ont expiré (plus de 6 mois). Veuillez renouveler votre mot de passe et MFA."
                })
            }

        # 3. Validation de la double authentification (MFA / 2FA)
        if not encrypted_mfa_db:
            cur.close()
            conn.close()
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"status": "mfa_missing", "message": "Le MFA n'est pas encore configuré pour ce compte."})
            }

        # Déchiffrer le secret TOTP
        try:
            totp_secret = decrypt_secret(encrypted_mfa_db)
        except Exception:
            cur.close()
            conn.close()
            return {
                "statusCode": 500,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"error": "Erreur interne de déchiffrement du secret MFA."})
            }

        # Valider le code TOTP avec pyotp
        totp = pyotp.TOTP(totp_secret)
        if not totp.verify(code_2fa):
            cur.close()
            conn.close()
            return {
                "statusCode": 401,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"status": "unauthorized", "message": "Identifiants ou code MFA incorrects (code TOTP invalide)."})
            }

        # Authentification réussie
        cur.close()
        conn.close()
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "status": "authenticated",
                "message": f"Utilisateur '{username}' authentifié avec succès."
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": f"Erreur de base de données : {str(e)}"})
        }
