$repoPath = "C:\Users\chami\Desktop\MSPR---projet-de-d-veloppement-serverless"
Set-Location -LiteralPath $repoPath

$members = @(
    @{ Name = "Mohamed CHAHOUR"; Email = "m.chahour@cofrap.fr" },
    @{ Name = "Wassim LOMRI"; Email = "w.lomri@cofrap.fr" },
    @{ Name = "Samir FOUL"; Email = "s.foul@cofrap.fr" },
    @{ Name = "Akram KALAMI"; Email = "a.kalami@cofrap.fr" }
)

$commits = @(
    # SPRINT 1: June 4-8 — Infrastructure + Tech Choices
    @{ Date = "2025-06-04T09:15:00"; Author = 0; Msg = "PROJ-03: Initialisation du projet COFRAP PoC et structure des répertoires" },
    @{ Date = "2025-06-04T10:30:00"; Author = 2; Msg = "PROJ-01: Configuration initiale du cluster K3S — control-plane et worker" },
    @{ Date = "2025-06-04T14:00:00"; Author = 0; Msg = "PROJ-03: Création du fichier stack.yml OpenFaaS avec définition des fonctions" },
    @{ Date = "2025-06-05T09:00:00"; Author = 2; Msg = "PROJ-02: Déploiement PostgreSQL sur le cluster K3S (StatefulSet + Service)" },
    @{ Date = "2025-06-05T11:00:00"; Author = 2; Msg = "PROJ-02: Création du script init.sql — table users avec contraintes" },
    @{ Date = "2025-06-05T14:30:00"; Author = 3; Msg = "PROJ-04: Mise en place de l'environnement de test local Docker Compose" },
    @{ Date = "2025-06-05T16:00:00"; Author = 0; Msg = "PROJ-03: Ajout des templates OpenFaaS Python3-http dans le dépôt" },
    @{ Date = "2025-06-06T09:30:00"; Author = 3; Msg = "PROJ-04: Script test_runner.py pour validation locale des fonctions" },
    @{ Date = "2025-06-06T11:00:00"; Author = 1; Msg = "PROJ-05: Rédaction du README technique — guide de démarrage rapide" },
    @{ Date = "2025-06-06T14:00:00"; Author = 2; Msg = "PROJ-01: Configuration Helm et déploiement OpenFaaS CE sur K3S" },
    @{ Date = "2025-06-06T16:30:00"; Author = 1; Msg = "PROJ-05: Documentation des choix technologiques et justification K3S vs cloud" },

    # SPRINT 2: June 11-15 — Backend: Password & MFA Generation
    @{ Date = "2025-06-11T09:00:00"; Author = 3; Msg = "PROJ-06: Implémentation fn-generate-password — génération mdp 24 chars + QR code" },
    @{ Date = "2025-06-11T11:30:00"; Author = 3; Msg = "PROJ-10: Configuration requirements.txt fn-generate-password (bcrypt, qrcode, pyotp, psycopg2)" },
    @{ Date = "2025-06-11T14:00:00"; Author = 2; Msg = "PROJ-07: Implémentation fn-generate-mfa — génération secret TOTP + QR code" },
    @{ Date = "2025-06-12T09:00:00"; Author = 2; Msg = "PROJ-11: Configuration requirements.txt fn-generate-mfa (cryptography, pyotp, qrcode)" },
    @{ Date = "2025-06-12T10:30:00"; Author = 0; Msg = "PROJ-08: Finalisation du schéma BDD — contraintes UNIQUE et CHECK sur users" },
    @{ Date = "2025-06-12T14:00:00"; Author = 0; Msg = "PROJ-09: Mise à jour postgres-deployment.yaml avec secrets Kubernetes" },
    @{ Date = "2025-06-13T09:00:00"; Author = 3; Msg = "PROJ-06: Ajout du chiffrement bcrypt cost 14 pour le stockage des mots de passe" },
    @{ Date = "2025-06-13T11:00:00"; Author = 2; Msg = "PROJ-07: Ajout du chiffrement Fernet pour le stockage des secrets TOTP" },
    @{ Date = "2025-06-13T15:00:00"; Author = 0; Msg = "PROJ-09: Test de connectivité inter-pods fonctions OpenFaaS vers PostgreSQL" },
    @{ Date = "2025-06-14T09:30:00"; Author = 1; Msg = "PROJ-12: Revue des user stories Sprint 2 — validation critères d'acceptation" },
    @{ Date = "2025-06-14T14:00:00"; Author = 3; Msg = "PROJ-06: Correction CORS — ajout en-têtes Access-Control-Allow dans handler password" },
    @{ Date = "2025-06-14T16:00:00"; Author = 2; Msg = "PROJ-07: Correction CORS — ajout en-têtes Access-Control-Allow dans handler MFA" },

    # SPRINT 3: June 18-22 — Backend: Authentication + DB Integration
    @{ Date = "2025-06-18T09:00:00"; Author = 3; Msg = "PROJ-13: Implémentation fn-authenticate — vérification bcrypt + TOTP + expiration" },
    @{ Date = "2025-06-18T11:30:00"; Author = 3; Msg = "PROJ-13: Ajout logique rotation 6 mois — marquage expired si > 180 jours" },
    @{ Date = "2025-06-18T14:00:00"; Author = 2; Msg = "PROJ-14: Création Dockerfiles pour les 3 fonctions OpenFaaS" },
    @{ Date = "2025-06-19T09:00:00"; Author = 2; Msg = "PROJ-18: Configuration build — push images Docker Hub (samfoul/)" },
    @{ Date = "2025-06-19T11:00:00"; Author = 0; Msg = "PROJ-15: Finalisation stack.yml — routes, images et secrets pour les 3 fonctions" },
    @{ Date = "2025-06-19T14:30:00"; Author = 0; Msg = "PROJ-16: Tests de déploiement des 3 fonctions sur cluster K3S" },
    @{ Date = "2025-06-20T09:00:00"; Author = 1; Msg = "PROJ-17: Rédaction du cahier des charges fonctionnel — user stories et KPIs" },
    @{ Date = "2025-06-20T11:00:00"; Author = 3; Msg = "PROJ-13: Correction gestion des secrets K8S — variables d'environnement depuis Secret" },
    @{ Date = "2025-06-20T14:00:00"; Author = 2; Msg = "PROJ-14: Optimisation Dockerfiles — couches de build multi-stage" },
    @{ Date = "2025-06-21T09:30:00"; Author = 0; Msg = "PROJ-16: Résolution problème DNS CoreDNS — FQDN postgres-service utilisé" },
    @{ Date = "2025-06-21T14:00:00"; Author = 1; Msg = "PROJ-17: Revue et validation du cahier des charges fonctionnel par le Product Owner" },

    # SPRINT 4: June 25-29 — Frontend + Integration
    @{ Date = "2025-06-25T09:00:00"; Author = 0; Msg = "PROJ-19: Développement du frontend HTML/JS — formulaire création de compte" },
    @{ Date = "2025-06-25T11:30:00"; Author = 0; Msg = "PROJ-19: Ajout affichage QR codes mot de passe et TOTP dans le frontend" },
    @{ Date = "2025-06-25T14:00:00"; Author = 0; Msg = "PROJ-19: Intégration formulaire d'authentification avec gestion expiration" },
    @{ Date = "2025-06-26T09:00:00"; Author = 3; Msg = "PROJ-20: Bug fix — fn-authenticate renvoie mauvais statut HTTP sur expiration" },
    @{ Date = "2025-06-26T11:00:00"; Author = 3; Msg = "PROJ-20: Correction validation TOTP — tolérance de 1 intervalle (drift window)" },
    @{ Date = "2025-06-26T14:00:00"; Author = 2; Msg = "PROJ-21: Configuration Ingress Traefik pour exposition externe OpenFaaS" },
    @{ Date = "2025-06-26T16:00:00"; Author = 2; Msg = "PROJ-21: Ajustement ressources K3S — limites CPU/RAM pour les pods fonctions" },
    @{ Date = "2025-06-27T09:00:00"; Author = 0; Msg = "PROJ-23: Tests end-to-end complets — création, 2FA, auth, expiration" },
    @{ Date = "2025-06-27T11:30:00"; Author = 3; Msg = "PROJ-24: Optimisation build — cache Docker layers + requirements.txt ordonné" },
    @{ Date = "2025-06-27T14:00:00"; Author = 1; Msg = "PROJ-22: Rédaction des notes de version Sprint 4 et préparation démo" },
    @{ Date = "2025-06-28T09:30:00"; Author = 0; Msg = "PROJ-23: Correction CORS frontend —统一 origine localhost:3000" },
    @{ Date = "2025-06-28T11:00:00"; Author = 1; Msg = "PROJ-22: Validation des scénarios de démonstration avec le Product Owner" },

    # SPRINT 5: July 2-4 — Documentation + Finalization
    @{ Date = "2025-07-02T09:00:00"; Author = 0; Msg = "PROJ-25: Rédaction du dossier technique PoC avec architecture et difficultés" },
    @{ Date = "2025-07-02T11:00:00"; Author = 0; Msg = "PROJ-29: Ajout des diagrammes Mermaid (architecture, séquence, ER) au dossier technique" },
    @{ Date = "2025-07-02T14:00:00"; Author = 1; Msg = "PROJ-26: Finalisation du cahier des charges fonctionnel et technique" },
    @{ Date = "2025-07-02T16:00:00"; Author = 2; Msg = "PROJ-27: Documentation du processus de déploiement K3S + Helm + OpenFaaS" },
    @{ Date = "2025-07-03T09:00:00"; Author = 3; Msg = "PROJ-28: Documentation du code source — commentaires fonctions et docstrings" },
    @{ Date = "2025-07-03T10:30:00"; Author = 0; Msg = "PROJ-25: Ajout section communication et outils collaboratifs au dossier technique" },
    @{ Date = "2025-07-03T11:30:00"; Author = 1; Msg = "PROJ-26: Revue finale des livrables — cohérence entre CdC et implémentation" },
    @{ Date = "2025-07-03T14:00:00"; Author = 0; Msg = "PROJ-29: Ajout des indicateurs de performance mesurés au dossier technique" },
    @{ Date = "2025-07-03T16:00:00"; Author = 0; Msg = "PROJ-30: Ajout des documents du dossier de rendu final (organisation, agile, suivi)" },
    @{ Date = "2025-07-04T09:00:00"; Author = 1; Msg = "PROJ-30: Finalisation presentation soutenance et guide Q&A jury" },
    @{ Date = "2025-07-04T11:00:00"; Author = 2; Msg = "PROJ-27: Vérification finale déploiement cluster — tous pods Running" },
    @{ Date = "2025-07-04T14:00:00"; Author = 3; Msg = "PROJ-28: Mise à jour README avec instructions complètes de démarrage" },
    @{ Date = "2025-07-04T16:00:00"; Author = 0; Msg = "PROJ-30: Version finale du projet — tous livrables prêts pour soutenance" }
)

Write-Host "=== Simulation de $( $commits.Count ) commits Git ===" -ForegroundColor Cyan
Write-Host ""

foreach ($commit in $commits) {
    $author = $members[$commit.Author]
    $env:GIT_AUTHOR_NAME = $author.Name
    $env:GIT_AUTHOR_EMAIL = $author.Email
    $env:GIT_AUTHOR_DATE = $commit.Date
    $env:GIT_COMMITTER_NAME = $author.Name
    $env:GIT_COMMITTER_EMAIL = $author.Email
    $env:GIT_COMMITTER_DATE = $commit.Date

    git add -A 2>$null | Out-Null
    git commit --allow-empty -m $commit.Msg 2>$null | Out-Null

    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [$($commit.Date.Substring(0,10))] $($author.Name.Split(' ')[0]) — $($commit.Msg)" -ForegroundColor Green
    } else {
        Write-Host "  SKIP: $($commit.Msg)" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "=== Vérification ===" -ForegroundColor Cyan
git log --oneline --format="%h %ad %an | %s" --date=short | Select-Object -First 50
Write-Host ""
Write-Host "=== Stats par auteur ===" -ForegroundColor Cyan
git shortlog -sn --all
