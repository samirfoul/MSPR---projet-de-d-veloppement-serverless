import os
import sys
import json
import time
import importlib.util
import pyotp
import psycopg2

# Configuration des variables d'environnement pour le test local
os.environ["DB_HOST"] = "localhost"
os.environ["DB_PORT"] = "5432"
os.environ["DB_NAME"] = "cofrap_db"
os.environ["DB_USER"] = "postgres_user"
os.environ["DB_PASSWORD"] = "postgres_password"
os.environ["ENCRYPTION_KEY"] = "MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI="

# Mock pour l'événement OpenFaaS
class MockEvent:
    def __init__(self, body_dict):
        self.body = json.dumps(body_dict).encode('utf-8')

class MockContext:
    pass

def load_handler(module_name, path_to_file):
    spec = importlib.util.spec_from_file_location(module_name, path_to_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Chemins absolus vers les handlers
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_FN_PWD = os.path.join(BASE_DIR, "../functions/fn-generate-password/handler.py")
PATH_FN_MFA = os.path.join(BASE_DIR, "../functions/fn-generate-mfa/handler.py")
PATH_FN_AUTH = os.path.join(BASE_DIR, "../functions/fn-authenticate/handler.py")

print("Chargement des fonctions OpenFaaS...")
fn_pwd = load_handler("fn_pwd", PATH_FN_PWD)
fn_mfa = load_handler("fn_mfa", PATH_FN_MFA)
fn_auth = load_handler("fn_auth", PATH_FN_AUTH)
print("Fonctions chargées avec succès.\n")

def check_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            connect_timeout=3
        )
        conn.close()
        return True
    except Exception as e:
        print(f"⚠️ Erreur de connexion à la base de données : {e}")
        print("Avez-vous démarré le conteneur PostgreSQL local avec docker-compose ?")
        return False

def run_tests():
    if not check_db_connection():
        return

    username = "michel.ranu"
    print(f"--- 1. Test de génération du mot de passe pour {username} ---")
    event_pwd = MockEvent({"username": username})
    res_pwd = fn_pwd.handle(event_pwd, MockContext())
    
    print(f"Status Code: {res_pwd['statusCode']}")
    body_pwd = json.loads(res_pwd['body'])
    print(f"Body: {json.dumps(body_pwd, indent=2)[:300]}...\n")
    
    raw_password = body_pwd.get("raw_password")
    
    print(f"--- 2. Test de génération du secret 2FA/MFA pour {username} ---")
    event_mfa = MockEvent({"username": username})
    res_mfa = fn_mfa.handle(event_mfa, MockContext())
    
    print(f"Status Code: {res_mfa['statusCode']}")
    body_mfa = json.loads(res_mfa['body'])
    print(f"Body: {json.dumps(body_mfa, indent=2)[:300]}...\n")
    
    totp_secret = body_mfa.get("totp_secret")

    # Générer le code TOTP actuel
    totp = pyotp.TOTP(totp_secret)
    current_code = totp.now()
    print(f"Code TOTP actuel généré : {current_code}")

    print(f"\n--- 3. Test d'authentification réussie (Mots de passe + TOTP corrects) ---")
    event_auth_ok = MockEvent({
        "username": username,
        "password": raw_password,
        "code": current_code
    })
    res_auth_ok = fn_auth.handle(event_auth_ok, MockContext())
    print(f"Status Code: {res_auth_ok['statusCode']}")
    print(f"Body: {res_auth_ok['body']}\n")

    print(f"--- 4. Test d'authentification échouée (Mauvais mot de passe) ---")
    event_auth_bad_pwd = MockEvent({
        "username": username,
        "password": "MauvaisMotDePasse123!",
        "code": current_code
    })
    res_auth_bad_pwd = fn_auth.handle(event_auth_bad_pwd, MockContext())
    print(f"Status Code: {res_auth_bad_pwd['statusCode']}")
    print(f"Body: {res_auth_bad_pwd['body']}\n")

    print(f"--- 5. Test d'authentification échouée (Mauvais code TOTP) ---")
    event_auth_bad_totp = MockEvent({
        "username": username,
        "password": raw_password,
        "code": "000000"
    })
    res_auth_bad_totp = fn_auth.handle(event_auth_bad_totp, MockContext())
    print(f"Status Code: {res_auth_bad_totp['statusCode']}")
    print(f"Body: {res_auth_bad_totp['body']}\n")

    print(f"--- 6. Test d'expiration des identifiants (Simulation > 6 mois d'ancienneté) ---")
    # Simuler en modifiant la date de génération (gendate) en BDD à 7 mois dans le passé
    print("Modification de 'gendate' en BDD à 7 mois dans le passé...")
    try:
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"]
        )
        cur = conn.cursor()
        seven_months_ago = int(time.time()) - (7 * 30 * 24 * 3600)
        cur.execute("UPDATE users SET gendate = %s, expired = 0 WHERE username = %s;", (seven_months_ago, username))
        conn.commit()
        cur.close()
        conn.close()
        print("Date mise à jour.")
    except Exception as e:
        print(f"Erreur de modification BDD: {e}")
        return

    # Tenter de s'authentifier
    current_code = totp.now() # Régénérer le code au cas où la minute a changé
    event_auth_expired = MockEvent({
        "username": username,
        "password": raw_password,
        "code": current_code
    })
    res_auth_expired = fn_auth.handle(event_auth_expired, MockContext())
    print(f"Status Code: {res_auth_expired['statusCode']}")
    print(f"Body: {res_auth_expired['body']}\n")

    # Vérifier que le statut expiré a bien été enregistré
    print("Vérification du statut 'expired' en base de données...")
    try:
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"]
        )
        cur = conn.cursor()
        cur.execute("SELECT expired FROM users WHERE username = %s;", (username,))
        expired_status = cur.fetchone()[0]
        cur.close()
        conn.close()
        print(f"Valeur de 'expired' en BDD : {expired_status} (Attendu : 1)")
    except Exception as e:
        print(f"Erreur de lecture: {e}")

if __name__ == "__main__":
    run_tests()
