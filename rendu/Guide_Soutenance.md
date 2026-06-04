# Guide de Soutenance

## PoC d'authentification serverless COFRAP

**Format de l'oral :** 20 minutes de présentation + 30 minutes de questions du jury.

**Équipe :**
- Mohamed CHAHOUR — Scrum Master
- Wassim LOMRI — Product Owner
- Samir FOUL — DevOps
- Akram KALAMI — Lead Developer

---

## 1. Structure de la Présentation (20 minutes)

### 0:00 - 2:00 — Introduction

**Présentateur principal :** Wassim LOMRI

**Objectif du passage :** poser le contexte, expliciter le besoin métier, rassurer le jury sur la maîtrise du sujet.

**Messages clés à faire passer :**
- COFRAP a besoin d'un mécanisme d'authentification moderne, sécurisé et modulaire.
- Le PoC répond à un besoin de validation technique avant industrialisation.
- Le choix serverless vise la simplicité de déploiement, la scalabilité et l'isolation des fonctions.
- Le projet couvre à la fois la dimension technique et la dimension pilotage de projet.
- L'équipe s'est organisée par rôles complémentaires.

**Ce qu'il faut montrer à l'écran :**
- Slide d'ouverture avec titre du projet.
- Logo ou contexte COFRAP.
- Schéma très simple du besoin : utilisateur, frontend, fonctions serverless, authentification forte.
- Slide équipe avec noms et rôles.

**Accroche orale conseillée :**
- « Notre objectif était de démontrer qu'un parcours d'authentification sécurisé pouvait être mis en œuvre rapidement dans une architecture serverless, tout en restant pilotable comme un vrai projet SI. »

**Phrase de transition :**
- « Une fois le besoin posé, nous avons structuré le projet comme un projet professionnel, avec un découpage, un planning, des ressources et un budget. »

### 2:00 - 5:00 — Compétence C1 : Organisation projet

**Présentateur principal :** Mohamed CHAHOUR

**Objectif du passage :** démontrer la capacité à planifier et organiser un projet de bout en bout.

**Messages clés à faire passer :**
- Le projet a été découpé en lots de travail via un WBS.
- Le séquencement a été matérialisé dans un diagramme de Gantt.
- Les dépendances critiques ont été identifiées très tôt.
- Les ressources humaines ont été affectées selon les rôles et compétences.
- Le budget a été estimé de manière réaliste, y compris les coûts potentiels d'infrastructure et de temps homme.

**Ce qu'il faut montrer à l'écran :**
- Capture du WBS.
- Capture du diagramme de Gantt initial.
- Tableau synthétique budget / ressources.
- Slide avec chemin critique et jalons.

**Points d'insistance :**
- Justifier les durées par complexité relative et dépendances.
- Montrer qu'il ne s'agit pas d'un simple projet scolaire improvisé.
- Mettre en avant la logique de répartition des charges.

**Phrase de transition :**
- « Cette organisation n'avait de sens que si elle servait un besoin cadré ; c'est pourquoi nous avons produit un double cadrage, fonctionnel et technique. »

### 5:00 - 8:00 — Compétence C2 : Cahiers des charges

**Présentateur principal :** Wassim LOMRI

**Objectif du passage :** montrer la capacité à traduire un besoin métier en exigences exploitables.

**Messages clés à faire passer :**
- Le cahier des charges fonctionnel décrit les usages, acteurs et attentes métier.
- Le cahier des charges technique décrit les contraintes, composants et exigences non fonctionnelles.
- Les user stories ont servi de pont entre besoin métier et réalisation.
- Les critères d'acceptation ont permis de rendre le périmètre vérifiable.
- Le PoC a volontairement gardé un périmètre limité mais démonstratif.

**Ce qu'il faut montrer à l'écran :**
- Extrait du cahier des charges fonctionnel.
- Extrait du cahier des charges technique.
- Quelques user stories représentatives.
- Un tableau « besoin -> user story -> livrable ».

**Exemples de formulations à citer :**
- Inscription utilisateur.
- Génération de QR code pour 2FA.
- Authentification avec second facteur.
- Gestion d'expiration de crédentiel.

**Phrase de transition :**
- « Une fois le cadre défini, il fallait choisir une méthode de travail adaptée à un projet court, itératif et à forte coordination. »

### 8:00 - 11:00 — Compétence C3 : Méthode agile

**Présentateur principal :** Mohamed CHAHOUR

**Objectif du passage :** justifier le choix de Scrum et montrer sa mise en œuvre concrète.

**Messages clés à faire passer :**
- Scrum a été choisi pour son découpage itératif et la visibilité offerte au groupe.
- Les rôles ont été clairement assumés : PO, Scrum Master, DevOps, Lead Dev.
- Les cérémonies ont structuré la coordination.
- Les outils ont fluidifié le suivi : backlog, tickets, communication, documentation.
- Le mode agile a permis d'ajuster le PoC sans perdre le fil du besoin initial.

**Ce qu'il faut montrer à l'écran :**
- Backlog ou tableau Kanban/Scrum.
- Sprint board.
- Exemple de user story passée de « To do » à « Done ».
- Schéma des cérémonies : sprint planning, daily, review, retrospective.

**Points d'insistance :**
- Expliquer pourquoi Scrum et non Kanban.
- Montrer que l'agilité n'a pas remplacé le pilotage, mais l'a renforcé.
- Mentionner la cadence des points d'équipe.

**Phrase de transition :**
- « Cette méthode n'était utile que si nous savions mesurer l'avancement réel ; nous avons donc construit un tableau de bord de suivi. »

### 11:00 - 13:00 — Compétence C4 : Tableau de bord de suivi

**Présentateur principal :** Mohamed CHAHOUR

**Objectif du passage :** prouver la capacité à suivre, piloter et corriger l'exécution.

**Messages clés à faire passer :**
- Le tableau de bord consolide planning, indicateurs et alertes.
- Les KPI permettent d'objectiver le rythme de production.
- Le Gantt actualisé matérialise les écarts entre prévu et réalisé.
- L'EVM apporte une lecture coût / délai / valeur produite.
- Les décisions de pilotage sont prises à partir de faits observables.

**Ce qu'il faut montrer à l'écran :**
- Capture du tableau de bord.
- Gantt actualisé.
- KPI clés : avancement, tâches terminées, charge restante, risques ouverts.
- Si disponible : SPI/CPI ou équivalents EVM.

**Points d'insistance :**
- Expliquer comment un indicateur déclenche une action.
- Insister sur l'intérêt du suivi pour arbitrer les priorités.

**Phrase de transition :**
- « Au-delà de l'équipe interne, le pilotage impliquait aussi la maîtrise des contributions externes et des engagements de service. »

### 13:00 - 14:00 — Compétence C5 : Pilotage prestataires

**Présentateur principal :** Samir FOUL

**Objectif du passage :** montrer la maîtrise contractuelle et opérationnelle d'intervenants externes.

**Messages clés à faire passer :**
- Les SLA formalisent les attentes de disponibilité, délai et qualité.
- Le suivi prestataire repose sur des points de contrôle et des métriques.
- Les pénalités sont un levier de contractualisation, pas un objectif en soi.
- La logique recherchée est la prévention, l'escalade puis la correction.
- Dans un contexte PoC, cette compétence est démontrée à travers un cadre de pilotage simulé mais crédible.

**Ce qu'il faut montrer à l'écran :**
- Extrait de SLA.
- Tableau de suivi prestataire.
- Exemple de matrice seuil / alerte / pénalité.

**Phrase de transition :**
- « Le projet ne repose pas seulement sur des outils et des contrats ; il repose d'abord sur une équipe qu'il faut animer, coordonner et faire progresser. »

### 14:00 - 16:00 — Compétences C6 à C9 : Conduite d'équipe, communication, innovation, processus de communication

**Présentateur principal :** Akram KALAMI

**Objectif du passage :** montrer la maturité managériale, relationnelle et collaborative.

**Messages clés à faire passer :**
- C6 : la conduite d'équipe s'appuie sur la priorisation, l'entraide et l'arbitrage.
- C7 : l'écoute active améliore la qualité des décisions et la motivation.
- C8 : l'anticipation des différences culturelles ou de styles de travail réduit les frictions.
- C9 : les processus de communication structurent les échanges et évitent la perte d'information.
- Le binôme technique / organisation a permis d'avancer sans silos.

**Ce qu'il faut montrer à l'écran :**
- Organigramme projet léger.
- Exemples de canaux de communication.
- Routine check-in / check-out.
- Extrait de compte-rendu ou décision tracée.

**Points d'insistance :**
- Donner un exemple concret d'ajustement d'équipe.
- Montrer que la communication a été pensée et non subie.

**Phrase de transition :**
- « Cette logique d'animation se prolonge naturellement dans la réunion, le partage d'information et l'organisation du travail à distance. »

### 16:00 - 18:00 — Compétences C10 à C12 : Animation réunion, partage information, télétravail

**Présentateur principal :** Akram KALAMI

**Objectif du passage :** démontrer la capacité à faire vivre la collaboration, notamment en contexte hybride ou distant.

**Messages clés à faire passer :**
- C10 : une réunion efficace a un objectif, un timing, un animateur et une trace.
- C11 : le partage d'information repose sur des outils choisis pour leur complémentarité.
- C12 : le télétravail nécessite des règles explicites, de la discipline et de la visibilité.
- Les outils servent le processus, ils ne le remplacent pas.
- L'équipe a intégré la logique de disponibilité asynchrone et de synchronisation ciblée.

**Ce qu'il faut montrer à l'écran :**
- Modèle d'ordre du jour.
- Exemple de compte-rendu court.
- Cartographie des outils : messagerie, documentation, tickets, visio.
- Règles de fonctionnement à distance.

**Phrase de transition :**
- « Après le cadrage, le pilotage et l'organisation d'équipe, nous vous proposons de voir le résultat concret avec une démonstration du PoC. »

### 18:00 - 19:00 — Démonstration live du PoC

**Présentateur principal :** Akram KALAMI

**Support technique :** Samir FOUL

**Objectif du passage :** montrer rapidement que le PoC fonctionne réellement.

**Messages clés à faire passer :**
- Le frontend est opérationnel.
- Le parcours d'inscription et d'authentification est cohérent.
- La 2FA renforce le scénario de sécurité.
- Les fonctions serverless sont visibles et exécutables.
- Le PoC matérialise bien le lien entre besoin métier et architecture technique.

**Ce qu'il faut montrer à l'écran :**
- Frontend.
- Création de compte.
- QR code.
- Authentification réussie.
- Interface OpenFaaS / passerelle avec les fonctions.

**Phrase de transition :**
- « Cette démonstration illustre la faisabilité ; nous terminons par les enseignements et les perspectives d'évolution. »

### 19:00 - 20:00 — Conclusion et perspectives

**Présentateur principal :** Wassim LOMRI

**Objectif du passage :** conclure proprement, valoriser le travail et ouvrir sur la suite.

**Messages clés à faire passer :**
- Le PoC a validé la faisabilité du parcours d'authentification serverless.
- Le projet a été piloté avec des méthodes et livrables professionnels.
- Les choix techniques restent évolutifs.
- Des perspectives existent : industrialisation, monitoring renforcé, sécurisation complémentaire, tests de charge.
- L'équipe a su articuler méthode, gouvernance et démonstration technique.

**Ce qu'il faut montrer à l'écran :**
- Slide de synthèse.
- Trois réussites principales.
- Trois perspectives réalistes.

**Phrase de clôture conseillée :**
- « Notre PoC démontre qu'une approche serverless peut répondre à un besoin d'authentification sécurisé tout en restant pilotable, mesurable et évolutive. Nous sommes maintenant prêts à répondre à vos questions. »

---

## 2. Qui Présente Quoi

| Section | Compétence / sujet | Présentateur principal | Raison du choix | Backup speaker |
|---|---|---|---|---|
| Introduction | Contexte, problème, équipe | Wassim LOMRI | Vision produit et cadrage métier | Mohamed CHAHOUR |
| C1 | Organisation projet | Mohamed CHAHOUR | Rôle Scrum Master et pilotage | Wassim LOMRI |
| C2 | Cahiers des charges | Wassim LOMRI | Rôle Product Owner | Mohamed CHAHOUR |
| C3 | Méthode agile | Mohamed CHAHOUR | Rôle Scrum Master | Akram KALAMI |
| C4 | Tableau de bord suivi | Mohamed CHAHOUR | Suivi, KPI, arbitrage | Samir FOUL |
| C5 | Pilotage prestataires | Samir FOUL | Logique infra, services, SLA | Mohamed CHAHOUR |
| C6 | Conduite d'équipe | Akram KALAMI | Coordination technique et entraide | Mohamed CHAHOUR |
| C7 | Écoute active | Akram KALAMI | Gestion opérationnelle du collectif | Wassim LOMRI |
| C8 | Communication interculturelle / innovation relationnelle | Akram KALAMI | Lead technique transversal | Mohamed CHAHOUR |
| C9 | Processus de communication | Akram KALAMI | Mise en pratique quotidienne | Wassim LOMRI |
| C10 | Animation de réunion | Akram KALAMI | Animation opérationnelle | Mohamed CHAHOUR |
| C11 | Partage d'information | Akram KALAMI | Choix et usage des outils | Samir FOUL |
| C12 | Télétravail / travail hybride | Akram KALAMI | Coordination distante | Mohamed CHAHOUR |
| Démo | Frontend + parcours fonctionnel | Akram KALAMI | Lead Developer | Samir FOUL |
| Démo technique | OpenFaaS / fonctions / support | Samir FOUL | DevOps | Akram KALAMI |
| Conclusion | Bilan et perspectives | Wassim LOMRI | Vision produit et suite | Mohamed CHAHOUR |

### Répartition synthétique par membre

**Mohamed CHAHOUR**
- C1
- C3
- C4
- Appui sur transitions globales

**Wassim LOMRI**
- Introduction
- C2
- Conclusion
- Relance sur la valeur métier

**Samir FOUL**
- C5
- Support démo
- Réponses jury sur infra, SLA, déploiement, environnement

**Akram KALAMI**
- C6 à C12
- Démo live
- Réponses jury sur implémentation et fonctionnement applicatif

### Règle de secours si un membre est absent

- Si Mohamed est absent, Wassim reprend C1 et C4, Akram reprend C3.
- Si Wassim est absent, Mohamed reprend introduction et conclusion, plus C2 avec appui des user stories.
- Si Samir est absent, Akram gère la partie démo technique et Mohamed reprend C5.
- Si Akram est absent, Samir gère la démo et Mohamed/Wassim répartissent C6 à C12 sous forme plus synthétique.

---

## 3. Questions Probables du Jury

## C1 — Organisation projet

### Q1. Comment avez-vous estimé les durées des tâches ?

**Cadre de réponse :**
- Expliquer la décomposition en tâches élémentaires via WBS.
- Dire que l'estimation combine complexité, dépendances et disponibilité des membres.
- Mentionner l'appui sur retour d'expérience académique et technique.
- Citer un exemple de tâche courte et une tâche à risque.

### Q2. Pourquoi ce budget ?

**Cadre de réponse :**
- Distinguer coût humain, coût outillage, coût hébergement éventuel.
- Préciser qu'un PoC vise une estimation réaliste plus qu'un chiffrage industriel exhaustif.
- Justifier les hypothèses retenues.
- Montrer que le budget sert à arbitrer les choix.

### Q3. Quelles étaient les tâches critiques du projet ?

**Cadre de réponse :**
- Citer les tâches bloquantes : architecture, intégration 2FA, démo bout en bout.
- Expliquer la notion de dépendance sur le Gantt.
- Montrer qu'un retard sur une tâche critique impacte la date finale.
- Dire quelles marges de sécurité ont été prévues.

## C2 — Cahiers des charges

### Q4. Quelle est la différence entre votre cahier des charges technique et fonctionnel ?

**Cadre de réponse :**
- Fonctionnel = besoins, usages, acteurs, valeur attendue.
- Technique = contraintes, architecture, sécurité, intégration, performance.
- Expliquer que les deux documents sont complémentaires.
- Donner un exemple concret pris dans le projet.

### Q5. Comment avez-vous transformé le besoin en user stories ?

**Cadre de réponse :**
- Partir du persona ou de l'utilisateur cible.
- Utiliser la structure « En tant que... je veux... afin de... ».
- Ajouter des critères d'acceptation vérifiables.
- Montrer un exemple sur l'inscription ou la 2FA.

### Q6. Comment avez-vous géré le périmètre du PoC ?

**Cadre de réponse :**
- Expliquer ce qui a été inclus et exclu.
- Dire que le PoC vise la démonstration de faisabilité et non l'exhaustivité produit.
- Justifier les arbitrages par valeur, temps et risque.
- Citer une fonctionnalité volontairement reportée.

## C3 — Méthode agile

### Q7. Pourquoi Scrum plutôt que Kanban ?

**Cadre de réponse :**
- Scrum est adapté à un groupe restreint avec objectifs itératifs clairs.
- Les sprints donnent une cadence et des points de contrôle visibles.
- Kanban aurait été possible mais moins structurant pour la démonstration pédagogique.
- Relier ce choix au besoin de cérémonies et de rôles explicites.

### Q8. Quelles cérémonies avez-vous réellement mises en œuvre ?

**Cadre de réponse :**
- Citer sprint planning, points courts, revue, rétrospective.
- Expliquer leur finalité opérationnelle.
- Montrer que chaque cérémonie débouche sur une action ou décision.
- Donner un exemple de décision prise en revue ou rétro.

### Q9. Comment avez-vous géré le backlog ?

**Cadre de réponse :**
- Expliquer la priorisation par valeur et dépendance.
- Dire qui tranche en cas de conflit : PO avec appui équipe.
- Mentionner la mise à jour continue du backlog.
- Illustrer par le choix de prioriser l'authentification avant des raffinements UX.

## C4 — Tableau de bord suivi

### Q10. Comment réagissez-vous si le Gantt montre du retard ?

**Cadre de réponse :**
- Analyser d'abord la cause du retard.
- Identifier impact sur chemin critique et livrables.
- Décider : réaffectation, réduction de périmètre, replanification.
- Communiquer rapidement la décision et suivre l'effet correctif.

### Q11. Quels KPI étaient réellement utiles ?

**Cadre de réponse :**
- Citer peu d'indicateurs mais actionnables.
- Exemple : tâches terminées, taux d'avancement, charge restante, anomalies ouvertes.
- Expliquer pourquoi un KPI doit conduire à une décision.
- Refuser l'accumulation de métriques décoratives.

### Q12. À quoi vous sert l'EVM dans un projet comme celui-ci ?

**Cadre de réponse :**
- L'EVM donne une lecture combinée délai / effort / avancement.
- Même simplifié, il aide à objectiver un décalage.
- Il permet de comparer prévu, acquis et consommé.
- Mentionner SPI/CPI si utilisés, sinon expliquer la logique simplement.

## C5 — Pilotage prestataires

### Q13. Comment assurez-vous que vos prestataires respectent leurs SLA ?

**Cadre de réponse :**
- Définir des indicateurs mesurables dès le départ.
- Mettre en place une fréquence de contrôle.
- Prévoir escalade et plan d'action si dérive.
- Dire que la sanction vient après la tentative de correction.

### Q14. À quoi servent les pénalités si le but est de collaborer ?

**Cadre de réponse :**
- Les pénalités cadrent la relation contractuelle.
- Elles n'empêchent pas le dialogue, elles le structurent.
- Elles protègent le client en cas de manquement répété.
- Le premier objectif reste la remise à niveau du service.

### Q15. Quel type de prestataire imagineriez-vous dans ce projet ?

**Cadre de réponse :**
- Hébergeur, support infra, service de supervision, fournisseur d'identité éventuel.
- Expliquer le lien avec disponibilité et sécurité.
- Justifier pourquoi cette compétence est pertinente même dans un PoC.
- Rester concret sur les engagements attendus.

## C6 — Conduite d'équipe

### Q16. Comment gérez-vous un changement de priorité en milieu de sprint ?

**Cadre de réponse :**
- Évaluer l'urgence et l'impact.
- Arbitrer avec le PO et rendre visible le coût du changement.
- Protéger le sprint si possible, sinon renégocier explicitement le contenu.
- Conserver une traçabilité de la décision.

### Q17. Comment répartissez-vous les tâches dans l'équipe ?

**Cadre de réponse :**
- Selon rôles, compétences et charge disponible.
- En tenant compte des dépendances techniques.
- En évitant les silos par revue croisée ou binômage.
- Donner un exemple réel de répartition.

### Q18. Que faites-vous si un membre décroche ou prend du retard ?

**Cadre de réponse :**
- Commencer par un échange individuel factuel.
- Rechercher la cause : charge, blocage, incompréhension, disponibilité.
- Adapter la répartition et proposer un soutien.
- Formaliser un point de retour rapide.

## C7 — Écoute active

### Q19. Donnez un exemple concret d'écoute active dans votre équipe.

**Cadre de réponse :**
- Décrire une situation précise.
- Montrer que l'on reformule avant de répondre.
- Expliquer le bénéfice obtenu : meilleure solution, moins de tension, décision plus juste.
- Relier cela à la qualité de collaboration.

### Q20. Comment évitez-vous que les profils techniques dominent la discussion ?

**Cadre de réponse :**
- Distribuer la parole explicitement.
- Revenir systématiquement au besoin et à l'impact métier.
- Utiliser des tours de table courts.
- Valoriser les objections argumentées.

### Q21. Comment faites-vous remonter un désaccord sans créer de conflit ?

**Cadre de réponse :**
- Parler des faits et du risque, pas des personnes.
- Proposer des options plutôt qu'une opposition sèche.
- Chercher l'objectif commun.
- Tracer la décision finale.

## C8 — Communication et diversité des profils

### Q22. Comment anticipez-vous les conflits multiculturels ?

**Cadre de réponse :**
- Poser des règles explicites de communication.
- Vérifier la compréhension mutuelle.
- Éviter les implicites et les formulations ambiguës.
- Se concentrer sur objectifs, rôles et livrables.

### Q23. Comment adaptez-vous votre communication selon l'interlocuteur ?

**Cadre de réponse :**
- Métier : parler valeur, usage, risque.
- Technique : parler architecture, dette, faisabilité.
- Pilotage : parler délai, charge, arbitrage.
- Illustrer par un exemple du projet.

### Q24. Quelle innovation relationnelle avez-vous introduite ?

**Cadre de réponse :**
- Citer une pratique simple mais utile.
- Exemple : point check-in/check-out, décision log, binôme ponctuel.
- Expliquer pourquoi cela a amélioré la fluidité.
- Rester concret et crédible.

## C9 — Processus de communication

### Q25. Comment fonctionne votre check-in/check-out ?

**Cadre de réponse :**
- Check-in : disponibilité, priorité, blocage.
- Check-out : réalisé, difficulté, prochaine action.
- Format court et systématique.
- Intérêt : alignement rapide et prévention des malentendus.

### Q26. Comment évitez-vous la perte d'information ?

**Cadre de réponse :**
- Centraliser la documentation.
- Tracer les décisions importantes.
- Distinguer échange rapide et information durable.
- Rappeler que l'oral seul ne suffit pas.

### Q27. Comment choisissez-vous quel canal utiliser ?

**Cadre de réponse :**
- Urgence = messagerie instantanée.
- Décision structurante = documentation ou ticket.
- Synchronisation = réunion courte.
- Expliquer la règle d'usage commune à l'équipe.

## C10 — Animation de réunion

### Q28. Comment préparez-vous une réunion efficace ?

**Cadre de réponse :**
- Définir objectif, durée, participants utiles.
- Envoyer ordre du jour.
- Préparer les supports nécessaires.
- Sortir avec décisions, actions, responsables.

### Q29. Que faites-vous si la réunion dévie ?

**Cadre de réponse :**
- Recadrer sur l'objectif.
- Mettre les sujets hors périmètre dans un parking lot.
- Donner une décision de traitement ultérieur.
- Protéger le temps collectif.

### Q30. Animez-nous un court exercice d'animation à distance.

**Cadre de réponse :**
- Proposer un tour de table de 30 secondes par personne.
- Objectif : statut, blocage, besoin.
- Reformuler les points clés en fin d'exercice.
- Attribuer une action claire à chaque blocage.

## C11 — Partage d'information

### Q31. Pourquoi ces outils et pas d'autres ?

**Cadre de réponse :**
- Les outils ont été choisis selon usage, simplicité et complémentarité.
- Expliquer le rôle de chaque outil : ticketing, documentation, chat, visio.
- Dire qu'un bon outil est d'abord adopté par l'équipe.
- Mentionner l'importance de limiter la dispersion.

### Q32. Comment faites-vous circuler l'information entre technique et métier ?

**Cadre de réponse :**
- Utiliser un vocabulaire adapté à chaque public.
- Relier chaque point technique à un impact utilisateur.
- Formaliser en user stories, critères d'acceptation et comptes rendus.
- Montrer le rôle pivot du PO.

### Q33. Comment garantissez-vous une information à jour ?

**Cadre de réponse :**
- Désigner la source de vérité.
- Mettre à jour au fil de l'eau et non en fin de sprint seulement.
- Faire relire les éléments structurants.
- Intégrer la mise à jour documentaire à la Definition of Done si possible.

## C12 — Télétravail / hybride

### Q34. Comment prenez-vous en compte les décalages horaires ?

**Cadre de réponse :**
- Définir une plage de recouvrement commune.
- Favoriser l'asynchrone pour le non critique.
- Documenter clairement les décisions.
- Réserver les synchronisations aux sujets à forte valeur.

### Q35. Comment maintenez-vous la cohésion à distance ?

**Cadre de réponse :**
- Rituels courts et réguliers.
- Visibilité sur les tâches et les charges.
- Encouragement à demander de l'aide rapidement.
- Moments de feedback, pas seulement de contrôle.

### Q36. Quel risque principal voyez-vous dans le télétravail projet ?

**Cadre de réponse :**
- Désalignement silencieux.
- Retard de détection des blocages.
- Fatigue informationnelle ou sur-sollicitation.
- Réponse : règles de communication, traçabilité et points de synchronisation ciblés.

---

## 4. Questions Pièges et Réponses

### 1. Vous avez choisi K3S mais le sujet recommandait K3S ou cloud, pourquoi pas le cloud ?

**Réponse attendue :**
- Dire que K3S répondait mieux à l'objectif pédagogique et à la maîtrise de bout en bout.
- Mettre en avant la reproductibilité locale et le contrôle de l'environnement.
- Ajouter que le cloud reste une perspective d'industrialisation, pas une impossibilité.

### 2. Si votre équipe passe de 4 à 6 membres demain, que changez-vous ?

**Réponse attendue :**
- Revoir la répartition des responsabilités.
- Clarifier davantage les interfaces et la documentation.
- Éviter les réunions trop lourdes en gardant un cadre Scrum efficace.

### 3. Montrez-nous votre tableau de bord de suivi en direct.

**Réponse attendue :**
- Être prêt avec un onglet déjà ouvert.
- Montrer 3 indicateurs maximum et expliquer leur usage.
- Si l'accès live échoue, basculer immédiatement sur une capture datée.

### 4. Un prestataire ne respecte pas son SLA depuis 2 semaines, que faites-vous ?

**Réponse attendue :**
- Constater objectivement l'écart.
- Déclencher l'escalade prévue au contrat.
- Exiger un plan d'action correctif avec délai et suivi.
- Activer la pénalité si nécessaire après mise en demeure ou mécanisme prévu.

### 5. Un membre de votre équipe refuse d'utiliser Slack, comment gérez-vous cela ?

**Réponse attendue :**
- Rappeler la règle commune et le besoin de synchronisation.
- Comprendre la cause du refus.
- Adapter si le problème est ergonomique, pas si cela met en risque le collectif.
- Maintenir une source de vérité unique.

### 6. Votre démo tombe en panne, que faites-vous ?

**Réponse attendue :**
- Ne pas paniquer.
- Bascule immédiate vers plan B : vidéo, captures, ou environnement de secours.
- Continuer à expliquer le scénario et les preuves disponibles.

### 7. Qu'est-ce qui prouve que votre PoC est sécurisé ?

**Réponse attendue :**
- Ne jamais dire « totalement sécurisé ».
- Dire qu'il met en œuvre des mécanismes de sécurité ciblés : 2FA, séparation par fonctions, gestion d'expiration.
- Ajouter qu'un PoC valide une approche, pas une homologation sécurité complète.

### 8. Pourquoi ne pas avoir tout développé en monolithe pour aller plus vite ?

**Réponse attendue :**
- Le sujet porte sur une architecture serverless et ses bénéfices.
- Le découpage en fonctions permet modularité, isolation et évolutivité.
- Le PoC cherche à tester ce paradigme précisément.

### 9. Quel a été votre plus grand échec pendant le projet ?

**Réponse attendue :**
- Citer un vrai point de friction maîtrisé.
- Expliquer ce qui a été appris.
- Montrer la correction mise en place.
- Transformer la difficulté en preuve de pilotage mature.

### 10. Si COFRAP voulait industrialiser demain, quelle serait votre première recommandation ?

**Réponse attendue :**
- Audit de sécurité et de robustesse.
- Mise en place CI/CD, supervision, tests, secrets management.
- Revue architecture cible et exigences non fonctionnelles.
- Gouvernance claire avant passage en production.

---

## 5. Démonstration Script

### Objectif

- Montrer un scénario simple.
- Rester fluide et rapide.
- Ne pas improviser.
- Avoir tous les onglets déjà ouverts.

### Préparation avant prise de parole

- Ouvrir le frontend dans un premier onglet.
- Ouvrir l'interface OpenFaaS Gateway dans un second onglet.
- Ouvrir l'outil TOTP ou le support visuel lié à la 2FA.
- Vérifier que l'environnement est déjà opérationnel.
- Désactiver les notifications parasites.

### Script minute par minute

#### Étape 1 — Introduction de la démo

- Phrase conseillée : « Nous allons maintenant illustrer concrètement le parcours utilisateur validé par le PoC. »
- Rappeler que la démo dure moins d'une minute.

#### Étape 2 — Afficher le frontend

- Montrer la page d'accueil ou la page d'authentification.
- Pointer visuellement les entrées principales.
- Ne pas lire l'écran ; commenter la logique d'usage.

#### Étape 3 — Créer un nouveau compte utilisateur

- Cliquer sur inscription.
- Remplir un compte de démonstration préparé.
- Valider le formulaire.
- Dire ce que l'on attend comme résultat.

#### Étape 4 — Montrer la génération du QR code

- Mettre l'accent sur l'enrôlement du second facteur.
- Expliquer que le QR code sert à configurer le TOTP.
- Rester simple : éviter de détailler toute la cryptographie.

#### Étape 5 — Configurer la 2FA

- Scanner le QR code avec l'application TOTP ou montrer le code déjà importé.
- Dire que cette étape prouve la mise en place d'une authentification forte.

#### Étape 6 — Saisir le code TOTP

- Revenir sur le frontend.
- Entrer le code à usage temporaire.
- Valider.

#### Étape 7 — Montrer l'authentification réussie

- Afficher le message de succès ou l'accès à la zone protégée.
- Dire : « Le parcours complet d'inscription et d'authentification renforcée est fonctionnel. »

#### Étape 8 — Montrer la gestion d'expiration de crédentiel

- Simuler ou afficher le cas prévu par l'application.
- Expliquer ce que l'utilisateur voit en cas d'expiration.
- Insister sur la logique de contrôle de sécurité.

#### Étape 9 — Basculer sur OpenFaaS Gateway

- Ouvrir l'onglet gateway.
- Montrer les trois fonctions déployées.
- Les nommer et rappeler leur rôle fonctionnel.

#### Étape 10 — Relier frontend et fonctions

- Expliquer brièvement que le frontend invoque les fonctions serverless.
- Mettre en avant la séparation des responsabilités.
- Si possible, montrer un appel ou un état récent.

#### Étape 11 — Conclusion de la démo

- Phrase conseillée : « Cette démonstration montre la cohérence entre le besoin métier, le parcours utilisateur et l'architecture serverless retenue. »
- Revenir immédiatement sur le slide de conclusion.

### Règles de bonne exécution

- Aucun temps mort de navigation.
- Aucun mot de passe saisi à l'improviste.
- Aucun environnement à démarrer en direct.
- Une seule personne parle pendant la démo.
- Une seconde personne reste prête en support technique.

### Plan B en cas d'échec

- Vidéo courte enregistrée du scénario complet.
- Captures d'écran ordonnées.
- Explication du flux à partir du schéma d'architecture.
- Possibilité de montrer uniquement la gateway si le frontend ne répond plus.

---

## 6. Conseils Pratiques

## Installation technique

### Avant la soutenance

- Tester la connexion internet.
- Tester le partage d'écran.
- Tester le son et la caméra si requis.
- Vérifier les droits d'accès aux applications.
- Précharger tous les onglets utiles.
- Prévoir un second navigateur déjà ouvert.

### Support de secours

- Prévoir une vidéo de démo locale.
- Prévoir un PDF avec les captures clés.
- Prévoir une copie locale des slides.
- Prévoir un hotspot mobile en ultime recours.

## Discipline de timing

### Rôle de gardien du temps

- Mohamed CHAHOUR surveille le timing global.
- Il donne un signal discret à 1 minute de la fin de chaque bloc important.
- Un second signal est prévu avant la démo.

### Si vous êtes en retard

- Réduire les détails sur un sous-point, jamais sur la conclusion.
- Garder la démo très courte et propre.
- Couper d'abord les exemples secondaires.
- Ne jamais accélérer au point de devenir inaudible.

## Posture et langage corporel

### En présentiel

- Regarder le jury, pas uniquement l'écran.
- Se tenir droit.
- Parler avec un débit régulier.
- Utiliser les mains avec sobriété.

### En distanciel ou hybride

- Regarder la caméra à intervalles réguliers.
- Laisser un léger temps entre deux intervenants.
- Ne pas se couper la parole.
- Garder le micro propre et stable.

## Comment gérer un « je ne sais pas »

- Ne jamais inventer.
- Dire : « Nous n'avons pas approfondi ce point à ce niveau, mais notre raisonnement serait le suivant... »
- Donner une réponse méthodologique, même sans chiffre exact.
- Revenir au périmètre du PoC si nécessaire.

## Code vestimentaire

- Tenue professionnelle sobre.
- Couleurs neutres.
- Éviter les logos trop visibles.
- Cohérence d'équipe souhaitable.

## Gestion de l'anglais

- Être prêts à basculer brièvement en anglais si le jury le demande.
- Préparer une mini-séquence en anglais sur l'écoute active ou la communication.
- Connaître le vocabulaire de base : backlog, sprint, requirement, dashboard, provider, SLA.

## Erreurs à éviter

- Lire les slides mot à mot.
- Trop détailler la technique avant d'avoir posé le besoin.
- Se contredire entre membres.
- Lancer une démo non testée.
- Répondre de manière défensive au jury.

---

## 7. Checklist de Préparation

## Documents et supports

- Slides finales relues.
- Cahier des charges fonctionnel accessible.
- Cahier des charges technique accessible.
- WBS accessible.
- Gantt initial accessible.
- Gantt actualisé accessible.
- Tableau de bord accessible.
- Extrait SLA accessible.
- Schéma d'architecture accessible.
- Captures de démo accessibles.

## Démo

- Frontend testé.
- Parcours inscription testé.
- Génération QR code testée.
- Configuration 2FA testée.
- Authentification réussie testée.
- Cas d'expiration testé.
- OpenFaaS Gateway accessible.
- Trois fonctions visibles.
- Vidéo de secours prête.
- Captures de secours prêtes.

## Répartition de parole

- Chaque membre connaît son bloc.
- Chaque membre connaît sa phrase d'ouverture.
- Chaque membre connaît sa phrase de transition.
- Chaque membre connaît son backup speaker.
- Chacun sait à quel moment reprendre la parole.

## Répétition

- Répétition complète 20 minutes effectuée.
- Répétition avec chronométrage effectuée.
- Répétition des transitions effectuée.
- Répétition de la démo effectuée.
- Répétition du plan B effectuée.

## Questions jury

- 10 questions pièges répétées.
- 30+ questions probables réparties entre membres.
- Réponses alignées entre tous.
- Exemples concrets prêts.
- Limites du PoC assumées et formulées proprement.

## Logistique le jour J

- Arrivée en avance.
- Machines chargées.
- Chargeurs présents.
- Connexion testée sur place.
- Fichiers disponibles localement et en cloud.
- Notifications coupées.
- Micros testés.
- Caméra testée si besoin.

## Dernier tour juste avant de commencer

- Ouvrir les slides.
- Ouvrir les onglets de démo.
- Vérifier l'ordre de passage.
- Vérifier le chronomètre.
- Se répartir les réponses de secours.
- Respirer et démarrer calmement.

---

## Conclusion opérationnelle

- Votre objectif n'est pas de tout dire.
- Votre objectif est de montrer que vous maîtrisez le besoin, la méthode, le pilotage et le résultat.
- Le jury attend de la clarté, de la cohérence et de la capacité à justifier vos choix.
- Une soutenance réussie est structurée, rythmée, démonstrative et maîtrisée.

**Rappel final :**
- Contexte clair.
- Méthode crédible.
- Pilotage visible.
- Démo courte et fiable.
- Réponses jury structurées.
