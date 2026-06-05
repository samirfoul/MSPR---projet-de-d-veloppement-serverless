# COFRAP - Système d'Authentification Serverless (PoC)

Ce dépôt contient le Proof of Concept (PoC) développé pour le remaniement du système d'authentification de la **COFRAP**. La solution repose sur des fonctions Serverless hébergées sur un cluster Kubernetes local (Minikube) via **OpenFaaS**, s'interfaçant avec une base de données **PostgreSQL**.

## 🛡️ Fonctionnalités du PoC
1.  **Génération automatique de mots de passe** complexes de 24 caractères (Function 1).
2.  **Double authentification (2FA/MFA) obligatoire** de type TOTP (Function 2).
3.  **Génération de QR Codes** pour le mot de passe et l'enrôlement 2FA sous forme d'images Base64.
4.  **Vérification de la validité temporelle des identifiants (6 mois)** avec expiration automatique et renouvellement forcé (Function 3).
5.  **Interface Frontend interactive** et responsive de démonstration.

---

## 📋 Prérequis

Pour exécuter ce PoC localement, assurez-vous d'avoir installé sur votre machine :
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) (actif et en cours d'exécution)
*   [Minikube](https://minikube.sigs.k8s.io/docs/start/)
*   [Helm](https://helm.sh/)
*   [OpenFaaS CLI (faas-cli)](https://github.com/openfaas/faas-cli)
*   [Python 3.x](https://www.python.org/)

---

## 🚀 Guide de démarrage rapide

### Étape 1 : Démarrer le cluster Minikube
Lancez le cluster local avec les ressources recommandées par le cahier des charges :
```bash
minikube start --cpus=2 --memory=4096 --disk-size=20g --driver=docker
```

### Étape 2 : Déployer PostgreSQL sur le cluster
Créez la base de données et initialisez la table `users` :
```bash
# 1. Déployer Postgres
kubectl apply -f db/postgres-deployment.yaml

# 2. Attendre que le Pod soit prêt
kubectl rollout status -n openfaas-fn deploy/postgres

# 3. Créer la table users
kubectl exec -i -n openfaas-fn deploy/postgres -- psql -U postgres_user -d cofrap_db < db/init.sql
```

### Étape 3 : Exposer et connecter la passerelle OpenFaaS
*(En supposant qu'OpenFaaS soit déjà installé via Helm sur votre cluster)*

```bash
# 1. Exposer la gateway OpenFaaS sur le port 8080 de votre machine
kubectl port-forward -n openfaas svc/gateway 8080:8080 &

# 2. Récupérer le mot de passe admin de votre cluster
PASSWORD=$(kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode; echo)

# 3. Se connecter à faas-cli
echo -n $PASSWORD | faas-cli login --username admin --password-stdin --gateway http://127.0.0.1:8080
```

### Étape 4 : Déployer les fonctions OpenFaaS
Nous utilisons des images publiques sur Docker Hub conformément à la licence OpenFaaS Community Edition :
```bash
# 1. Récupérer le template de langage python
faas-cli template store pull python3-http

# 2. Compiler et déployer les fonctions (décrites dans stack.yml)
faas-cli up -f stack.yml
```

### Étape 5 : Lancer le Frontend
Démarrez le serveur web pour accéder à l'interface graphique :
```bash
cd frontend
python3 -m http.server 3000
```
Rendez-vous sur **`http://localhost:3000`** pour tester l'enrôlement et la connexion !

---

## 🧪 Tests locaux (Sans Kubernetes/OpenFaaS)

Pour valider rapidement le code Python de vos fonctions sans avoir à compiler des conteneurs ni à interagir avec Kubernetes, vous pouvez utiliser l'environnement de test local isolé :

```bash
cd local_test

# 1. Lancer un PostgreSQL de test local avec Docker Compose
docker compose up -d

# 2. Créer un environnement virtuel Python et installer les dépendances
python3 -m venv venv
source venv/bin/activate
pip install bcrypt pyotp cryptography qrcode pillow psycopg2-binary

# 3. Lancer le script de test automatique de bout en bout
python3 test_runner.py

# 4. Éteindre le conteneur de test à la fin
docker compose down
```

---

## 🛑 Arrêt des services

Pour éteindre proprement tous les composants de votre machine :
```bash
# 1. Arrêter le serveur Web du frontend
# Appuyez sur Ctrl+C dans le terminal où tourne python3 -m http.server

# 2. Arrêter le port-forward de la Gateway OpenFaaS
kill $(pgrep -f "port-forward")

# 3. Arrêter la base de données de test locale (Docker Compose)
cd local_test && docker compose down

# 4. Arrêter le cluster Minikube
minikube stop
```
