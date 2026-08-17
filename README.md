# SITE WEB PROMOTIONNEL GITHUB PAGES — LE GÈNE DE QIN
**Auteur :** Franck PLATON  
**Livre promu :** *Le Gène de Qin* (Best-seller Techno-thriller Amazon KDP)  
**Lien d'achat Amazon officiel :** [https://amzn.eu/d/04xCrOHY](https://amzn.eu/d/04xCrOHY)

---

## 🎯 PRÉSENTATION & ARCHITECTURE
Ce dépôt contient le site promotionnel officiel « One-Page » pour le roman *Le Gène de Qin*. Conçu pour convertir les visiteurs en lecteurs sur Amazon KDP, le site fonctionne **à 100 % en fichiers statiques (HTML5, CSS3, JS Vanilla)**, sans base de données, sans build tool obligatoire et **sans aucune dépendance payante**.

### Arborescence du projet :
```text
.
├── index.html          # Page principale optimisée SEO & Conversion Amazon KDP
├── css/
│   └── style.css       # Styles complets (Variables :root, Flex/Grid, Dark Mode)
├── js/
│   └── main.js         # Interactions JS Vanilla (Chronologie interactive, Lightbox, etc.)
├── images/             # Ensemble des visuels A+, couverture officielle (couverture_le_gene_de_qin.jpg) et illustrations
└── README.md           # Guide de déploiement et de personnalisation
```

---

## 🚀 GUIDE DE DÉPLOIEMENT GITHUB PAGES EN 5 ÉTAPES

### Étape 1 : Créer un dépôt GitHub
1. Connectez-vous à votre compte sur [GitHub](https://github.com/).
2. Cliquez sur **New Repository** (Nouveau dépôt).
3. Nommez-le par exemple : `le-gene-de-qin-roman` ou `franck-platon-livres`.
4. Cochez **Public** (indispensable pour la gratuité GitHub Pages) et validez via **Create repository**.

### Étape 2 : Envoyer les fichiers du site
Vous pouvez envoyer les fichiers soit par l'interface web, soit via Git en ligne de commande :
```bash
git init
git add .
git commit -m "Déploiement initial du site promotionnel Le Gène de Qin"
git branch -M main
git remote add origin https://github.com/<VOTRE_NOM_UTILISATEUR>/le-gene-de-qin-roman.git
git push -u origin main
```

### Étape 3 : Activer GitHub Pages dans les paramètres
1. Dans votre dépôt GitHub, allez dans l'onglet **Settings** (Paramètres).
2. Dans le menu de gauche, descendez jusqu'à la section **Pages**.
3. Dans **Build and deployment > Source**, choisissez **Deploy from a branch**.
4. Dans le sélecteur de branche (**Branch**), choisissez `main` (ou `master`), dossier `/ (root)` et cliquez sur **Save**.

### Étape 4 : Vérifier la compilation automatique
1. Patientez 30 à 60 secondes.
2. Allez dans l'onglet **Actions** de votre dépôt GitHub : vous verrez le workflow de déploiement s'exécuter avec une icône verte ✅.
3. Retournez dans **Settings > Pages** : l'URL officielle de votre site apparaît sous la forme :
   `https://<VOTRE_NOM_UTILISATEUR>.github.io/le-gene-de-qin-roman/`

### Étape 5 : Connecter un nom de domaine personnalisé (Optionnel)
1. Si vous possédez un domaine (ex. `www.franckplaton.com` ou `www.legenedeqin.fr`), inscrivez-le dans **Custom domain** dans **Settings > Pages**.
2. Chez votre registraire de domaine (OVH, Namecheap, Cloudflare), créez un enregistrement **CNAME** pointant vers `<VOTRE_NOM_UTILISATEUR>.github.io`.
3. Cochez **Enforce HTTPS** sur GitHub : votre site dispose automatiquement d'un certificat SSL gratuit !

---

## ⚙️ PERSONNALISATION FACILE
- **Modifier les couleurs ou polices :** Ouvrez `css/style.css` et ajustez les variables `:root` en tête de fichier (`--color-accent-cyan`, `--color-bg-dark`, etc.).
- **Modifier le lien Amazon :** Tous les boutons d'achat dans `index.html` pointent vers le lien court [https://amzn.eu/d/04xCrOHY](https://amzn.eu/d/04xCrOHY). Remplacez-le par votre ASIN ou votre lien d'affiliation Amazon si besoin.
- **Ajouter vos propres avis ou chroniques :** Vous pouvez dupliquer un bloc dans la section *Synopsis* ou *Personnages* directement dans `index.html`.

---
*Développé pour l'écosystème Amazon KDP — Prêt à propulser vos ventes en 2026 !*
