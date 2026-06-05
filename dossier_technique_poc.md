# Rapport Technique : Proof of Concept d'Authentification Serverless COFRAP

**Auteurs :** Architecte Cloud & Tech Lead  
**Destinataire :** Direction de la COFRAP  
**Date :** 5 juin 2026  
**Projet :** Remaniement du processus de création et d'authentification des comptes cloud (Mandatory 2FA, Auto-pwd et Rotation)  

---

## 1. Introduction et Contexte

Dans le cadre du renforcement global de la sécurité des applications cloud de la **COFRAP**, la direction a identifié plusieurs vulnérabilités majeures sur les processus d'authentification existants, notamment :
*   L'utilisation récurrente par les collaborateurs de mots de passe trop simples ou réutilisés.
*   Le faible taux d'adoption de la double authentification (2FA), restée jusqu'ici optionnelle.

### Objectifs du PoC (Proof of Concept)
Pour éradiquer ces failles et garantir l'intégrité des accès, le projet fixe les règles suivantes :
1.  **Génération automatique et stricte** de mots de passe de haute complexité (24 caractères incluant majuscules, minuscules, chiffres et caractères spéciaux).
2.  **Double authentification (2FA/MFA) de type TOTP obligatoire** dès la création du compte.
3.  **Rotation obligatoire tous les six mois** des mots de passe et des secrets TOTP, avec blocage automatique d'accès en cas d'expiration.
4.  **Optimisation financière des infrastructures** grâce à une architecture moderne "Scale to Zero" (extinction automatique des instances inactives).

Ce rapport présente l'implémentation technique et la réussite de la validation de cette solution.

---

## 2. Justification des Choix Technologiques

Afin de répondre au besoin de performance, de sécurité et d'agilité, l'architecture suivante a été retenue et validée pour le PoC :

| Technologie | Rôle dans le projet | Justification technique & Choix d'architecture |
| :--- | :--- | :--- |
| **Minikube (Kubernetes)** | Simulateur de cluster local | Permet de simuler fidèlement un environnement de production multi-nœuds Kubernetes sur macOS (via le driver Docker Desktop) sans surcoût d'infrastructure cloud. |
| **OpenFaaS (Community Edition)** | Framework Serverless / FaaS | Fournit une gestion simplifiée du cycle de vie des fonctions. Permet d'encapsuler la logique métier dans des micro-services autonomes et d'envisager la fonctionnalité *Scale to Zero* (extinction des instances) en production. |
| **PostgreSQL** | Base de données relationnelle | Choisi pour sa conformité ACID, sa robustesse dans la persistance des données et sa gestion native des requêtes `UPSERT` indispensables lors de la rotation des accès. |
| **Python 3** | Langage de développement des fonctions | Recommandé par la COFRAP pour sa concision, son écosystème de librairies sécurisées (`bcrypt` pour le hachage de mots de passe, `cryptography` pour le chiffrement symétrique et `pyotp` pour le calcul TOTP). |
| **Helm** | Gestionnaire de paquets Kubernetes | Indispensable pour industrialiser le déploiement d'OpenFaaS, du réseau et de l'idling dans le cluster de manière réutilisable via des charts. |

---

## 3. Architecture Globale du Système

L'application repose sur un découpage en trois tiers (Frontend, Gateway FaaS, Base de données) assurant une isolation complète et une scalabilité horizontale indépendante.

### Schéma d'Architecture Réseau & Flux

```
                        +---------------------------------------------+
                        |           Navigateur Utilisateur            |
                        +----------------------+----------------------+
                                               |
                                               | (1) HTTP / Port 3000
                                               v
                        +----------------------+----------------------+
                        |       Frontend SPA: HTML5/CSS/JS            |
                        +----------------------+----------------------+
                                               |
                                               | (2) API REST / Port 8080
                                               v
+----------------------------------------------+----------------------------------------------+
| Kubernetes (Minikube)                                                                       |
|                                                                                             |
|                       +----------------------+----------------------+                       |
|                       |           OpenFaaS Gateway                  |                       |
|                       +----------------------+----------------------+                       |
|                                              |                                              |
|                       +----------------------+----------------------+                       |
|                       |        Routage interne (openfaas-fn)        |                       |
|                       +-------+--------------+--------------+-------+                       |
|                               |              |              |                               |
|                               v              v              v                               |
|                         +-----------+  +-----------+  +-----------+                         |
|                         |    F1     |  |    F2     |  |    F3     |                         |
|                         | Password  |  |    MFA    |  |    Auth   |                         |
|                         +-----+-----+  +-----+-----+  +-----+-----+                         |
|                               |              |              |                               |
|                               +--------------+--------------+                               |
|                                              | (4) TCP / Port 5432                          |
|                                              v                                              |
|                               +--------------+--------------+                               |
|                               |        postgres-service     |                               |
|                               +--------------+--------------+                               |
|                                              |                                              |
|                                              v                                              |
|                               +--------------+--------------+                               |
|                               |      PostgreSQL Database    |                               |
|                               +-----------------------------+                               |
+---------------------------------------------------------------------------------------------+
```

### Rôle des Composants Réseau et Packaging :
*   **Helm** : Utilise la chart `faas-netes` pour déployer de façon autonome tous les contrôleurs, agents de surveillance (Prometheus) et passerelles de la stack OpenFaaS dans le cluster Kubernetes.
*   **Ingress / Port-Forward** : Assure l'exposition sécurisée des services internes. Dans le cadre de ce PoC local, le trafic HTTP externe du port `8080` de macOS est redirigé vers le service `gateway` interne de Kubernetes grâce à `kubectl port-forward`.

---

## 4. Workflow de Fonctionnement (Cas Nominaux)

### A. Création de compte et initialisation 2FA
Lorsqu'un administrateur ou un utilisateur demande la création d'un compte pour un identifiant (ex: `wassim`), les étapes suivantes sont exécutées séquentiellement :

1. **Saisie & Envoi** : L'utilisateur saisit le nom d'utilisateur dans le Frontend et clique sur "Générer mon compte".
2. **Appel Fonction 1 (Mot de passe)** : Le frontend appelle `POST /function/fn-generate-password` avec le paramètre `{username}`.
   * La fonction génère un mot de passe complexe aléatoire de 24 caractères.
   * Elle calcule le hash sécurisé via `bcrypt`.
   * Elle exécute une requête `UPSERT` en base de données pour enregistrer (ou écraser en cas de rotation) l'identifiant, le mot de passe haché, la date actuelle (`gendate`), et met le drapeau `expired` à `0`.
   * Elle génère un QR Code contenant le mot de passe en clair pour l'utilisateur.
   * Elle renvoie au frontend le mot de passe brut (pour le PoC) et le QR Code encodé en base64.
3. **Appel Fonction 2 (MFA/2FA)** : Dès réception, le frontend appelle immédiatement `POST /function/fn-generate-mfa` avec le paramètre `{username}`.
   * La fonction génère un secret TOTP cryptographiquement sûr en Base32 (`pyotp.random_base32()`).
   * Elle chiffre symétriquement ce secret via l'algorithme *Fernet* (`cryptography`).
   * Elle met à jour la base de données (`UPDATE users SET mfa = secret_chiffré WHERE username`).
   * Elle construit l'URI standard de provisioning (`otpauth://totp/COFRAP:...`) et génère son QR Code.
   * Elle renvoie au frontend le QR code de configuration 2FA en base64.
4. **Affichage final** : Le frontend affiche à l'écran le mot de passe généré et les deux QR Codes.

### B. Connexion et Validation 2FA
1. L'utilisateur saisit son identifiant, son mot de passe et le code à 6 chiffres affiché sur son application mobile Authenticator (Google/Microsoft).
2. Le frontend appelle `POST /function/fn-authenticate` avec ces paramètres.
3. La fonction `fn-authenticate` effectue les contrôles suivants :
   * **Vérification du mot de passe** : Elle extrait le hash Bcrypt de la base de données et le valide via `bcrypt.checkpw()`.
   * **Vérification de la rotation (6 mois)** : Elle calcule l'ancienneté des identifiants (`now - gendate`). Si l'ancienneté dépasse 6 mois (180 jours), elle exécute un `UPDATE users SET expired = 1` et renvoie une erreur `403` spécifique pour forcer la rotation.
   * **Validation 2FA** : Si l'âge est valide, elle extrait le secret TOTP chiffré, le déchiffre avec la clé symétrique et vérifie le code saisi par l'utilisateur via la clé temporelle TOTP (`pyotp.verify()`).
   * Si tout est correct, elle renvoie un statut de succès et le frontend affiche le tableau de bord de l'utilisateur.

---

## 5. Bilan, Difficultés rencontrées et Solutions

L'intégration locale d'architectures distribuées et conteneurisées sur macOS présente des défis techniques majeurs, résolus avec succès lors de ce PoC :

### 1. Concurrence des ports et CORS (Cross-Origin Resource Sharing)
*   **Problème** : Lors du couplage du Frontend (servi sur `http://localhost:3000`) avec la Gateway OpenFaaS (sur `http://127.0.0.1:8080`), le navigateur bloquait systématiquement les requêtes AJAX en raison de la politique de sécurité CORS. Les requêtes de pré-vérification (`OPTIONS`) renvoyaient des erreurs 401 ou 405.
*   **Solution** : 
    *   Le code des handlers Python a été mis à jour pour autoriser l'en-tête `Access-Control-Allow-Origin: *`.
    *   Le template de route de la passerelle Flask dans le fichier d'entrée `template/python3-http/index.py` a été surchargé pour intercepter et autoriser explicitement la méthode `OPTIONS`, débloquant le preflight CORS natif des navigateurs.

### 2. Contraintes de licence et Registre local sur OpenFaaS CE
*   **Problème** : OpenFaaS Community Edition (CE) refuse par licence le déploiement d'images locales sans registre (comme `fn:dev`) et exige la validation d'images distantes publiques. Par ailleurs, les annotations d'auto-scaling à zéro (`com.openfaas.scale.zero`) provoquent un rejet de déploiement en version CE.
*   **Solution** :
    *   Le fichier `stack.yml` a été épuré des labels d'auto-scaling incompatibles pour la phase locale.
    *   Les images ont été renommées pour pointer vers le registre public Docker Hub de l'utilisateur (`samfoul/`). La compilation et la publication ont été automatisées via la commande `faas-cli up`, qui pousse de manière sécurisée les conteneurs compilés sur le cloud Docker Hub avant de les déployer sur Minikube.

---

## 6. Conclusion

Ce Proof of Concept démontre la viabilité technique d'une architecture d'authentification robuste basée sur le modèle Serverless. Les exigences de haute complexité de mot de passe, de double authentification stricte, et de contrôle d'expiration semestrielle sont pleinement opérationnelles. Le passage à la production pourra s'effectuer sereinement sur un cluster managé de type AWS EKS ou Azure AKS, en activant les fonctionnalités de scalabilité automatique d'OpenFaaS Pro.
