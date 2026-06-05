import json
import os
import io
import base64
import qrcode
import pyotp
import psycopg2
from cryptography.fernet import Fernet

def get_fernet():
    # Clé de chiffrement symétrique
    key = os.environ.get("ENCRYPTION_KEY")
    if not key:
        # Clé statique de secours pour environnement local/PoC
        key = "MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI="
    return Fernet(key.encode('utf-8') if isinstance(key, str) else key)

def encrypt_secret(secret: str) -> str:
    f = get_fernet()
    return f.encrypt(secret.encode('utf-8')).decode('utf-8')

def generate_qr_code_base64(data: str) -> str:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    base64_encoded = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{base64_encoded}"

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

    username = data.get("username")
    if not username:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Le paramètre 'username' est requis."})
        }

    # 1. Générer le secret TOTP (Base32)
    totp_secret = pyotp.random_base32()
    
    # 2. Chiffrer le secret TOTP de façon symétrique
    encrypted_secret = encrypt_secret(totp_secret)
    
    # 3. Créer l'URI d'enregistrement TOTP pour le QR Code
    totp = pyotp.TOTP(totp_secret)
    provisioning_uri = totp.provisioning_uri(name=username, issuer_name="COFRAP")
    
    # 4. Générer le QR Code à partir de cet URI
    qr_base64 = generate_qr_code_base64(provisioning_uri)

    # 5. Enregistrer le secret MFA chiffré dans la base de données
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Mettre à jour l'utilisateur existant
        cur.execute("""
            UPDATE users 
            SET mfa = %s 
            WHERE username = %s;
        """, (encrypted_secret, username))
        
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
        conn.close()
        
        if updated_rows == 0:
            return {
                "statusCode": 404,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"error": f"L'utilisateur '{username}' n'a pas été trouvé. Veuillez d'abord générer son mot de passe."})
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

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "status": "success",
            "message": "Secret TOTP/2FA généré et enregistré avec succès.",
            "username": username,
            "totp_secret": totp_secret,  # Utile pour le PoC/test
            "qr_code": qr_base64
        })
    }
