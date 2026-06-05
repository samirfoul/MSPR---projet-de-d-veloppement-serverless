import json
import secrets
import string
import os
import time
import io
import base64
import bcrypt
import qrcode
import psycopg2

def generate_complex_password(length=24):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        # S'assurer de respecter les critères de complexité de la COFRAP
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in password)):
            return password

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

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
        # Lecture du body de la requête
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

    # 1. Génération du mot de passe complexe
    raw_password = generate_complex_password(24)
    
    # 2. Hachage du mot de passe (bcrypt)
    hashed_pwd = hash_password(raw_password)
    
    # 3. Génération du QR Code
    qr_base64 = generate_qr_code_base64(raw_password)

    # 4. Stockage en base de données
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        now = int(time.time())
        
        # Enregistrer ou mettre à jour le mot de passe
        cur.execute("""
            INSERT INTO users (username, password, gendate, expired)
            VALUES (%s, %s, %s, 0)
            ON CONFLICT (username)
            DO UPDATE SET password = EXCLUDED.password, gendate = EXCLUDED.gendate, expired = 0;
        """, (username, hashed_pwd, now))
        
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": f"Erreur de base de données : {str(e)}"})
        }

    # Retourner la réponse réussie
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "status": "success",
            "message": "Mot de passe généré et enregistré avec succès.",
            "username": username,
            "raw_password": raw_password,  # Utile pour le PoC/test
            "qr_code": qr_base64
        })
    }
