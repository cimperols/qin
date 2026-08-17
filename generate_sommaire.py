import os
import re

root_dir = "/home/user/pack_aplus_promotion"

# Define category mapping for folders
def get_category(folder_name):
    num = int(folder_name.split("_")[0])
    if num in [1, 51]:
        return "cat-a", "Catégorie A — Logos, Insignes & Symboles"
    elif num in [2, 17, 21, 29, 33, 37, 41, 45, 49, 53]:
        return "cat-b", "Catégorie B — Bandeaux Cinématographiques & Hero Banners"
    elif num in [3, 11, 16, 19, 35, 36, 47, 52]:
        return "cat-c", "Catégorie C — Cartes Archéo-Géographiques, Infographies & Blueprints"
    elif num in [4, 12, 15, 27]:
        return "cat-d", "Catégorie D — Artbooks, Concept Art & Équipements High-Tech"
    elif num in [7, 43, 46]:
        return "cat-e", "Catégorie E — Fiches Personnages Tactiques, Confrontations & Duels"
    elif num in [5, 9, 13, 23, 25, 28]:
        return "cat-f", "Catégorie F — Affiches Cinéma, Storyboards, Moodboards & Éditions"
    elif num in [8, 20, 31, 44]:
        return "cat-g", "Catégorie G — Artefacts Muséaux, Archives Impériales & Carnets"
    elif num in [24, 32, 39, 40, 48]:
        return "cat-h", "Catégorie H — Cartes de Tropes, Citations, Éloges & Dilemmes"
    elif num in [6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54]:
        return "cat-i", "Catégorie I — Les 13 Applications Web & Lead Magnets HTML5"
    return "cat-other", "Autre Catégorie"

# Folder descriptions
descriptions = {
    1: "Logos institutionnels tactiques pour La Veille Valmont (Antarctique) et Sterling Biotech (L'Odyssée). Idéaux en tête de page A+ pour marquer l'identité du techno-thriller.",
    2: "Bandeaux Hero en écran large représentant le Tibet en 221 av. J.-C. (massif du Kunlun) et le yacht L'Odyssée en pleine tempête méditerranéenne.",
    3: "Carte archéo-géographique globale et tactique situant les 5 théâtres de l'intrigue (Tibet, Méditerranée, Bhoutan, Japon, Antarctique) sous classification Niveau Cosmos.",
    4: "Planches d'artbook immersives et spécifications scientifiques sur la caverne de l'élixir au Kunlun et les ruines sous-marines de Yonaguni.",
    5: "Affiche de cinéma style blockbuster grand spectacle et mockup studio d'édition dorée reliée collector avec rappel des prix officiels.",
    6: "Application HTML5 autonome « Terminal d'Enquête KDP — Niveau Cosmos » (Visual Novel) permettant au lecteur d'explorer les 4 dossiers classifiés.",
    7: "Fiches de profils cliniques, militaires et géopolitiques pour les 4 protagonistes : Dr Léo Valmont, Samira Belkacem, Julian Sterling et la Générale Anja Petrova.",
    8: "Fiches techniques d'artefacts muséaux authentiques : la stèle rupestre tibétaine de 221 av. J.-C. et la seringue du sérum virale de Yonaguni.",
    9: "Bandeau studio comparant côte à côte vos 3 formats d'édition (Broché 10,90 €, Relié 24,99 €, Kindle 3,99 €) avec leurs arguments clés.",
    10: "Expérience HTML5 interactive simulant la fréquence radio polaire 14.285 MHz du brise-glace Le Valmont et les archives sonores de Samira.",
    11: "Schémas infographiques comparant l'horloge biologique (progeria vs télomérase) et chronologie split-screen 221 av. J.-C. vs 2025.",
    12: "Concept art high-tech en coupe du yacht-laboratoire L'Odyssée (118 mètres) et du brise-glace rouge et noir Le Valmont en Antarctique.",
    13: "Storyboards cinématographiques en écran large pour le climax de plongée à -30m à Yonaguni et l'incipit des alchimistes au Kunlun.",
    14: "Application HTML5 autonome simulant le Séquenceur Génétique du Dr Léo Valmont et le test d'activité télomérase (+999 %).",
    15: "Fiches matériels cliniques et tactiques : moniteur de séquençage ADN à bord de L'Odyssée et combinaison polaire à visière thermique de Samira.",
    16: "Plans blueprints architecturaux tactiques : base souterraine géothermique de Vostok en Antarctique et relevé sonar de Yonaguni -30m.",
    17: "Bandeaux atmosphériques pour le monastère de Paro au Bhoutan dans la brume et le lac Léman à Genève au coucher du soleil.",
    18: "Application HTML5 simulant le réseau satellite orbital de La Veille Valmont traquant les 5 coordonnées géographiques du roman.",
    19: "Evidence Board (tableau d'enquête d'espionnage) reliant Léo, Sam, Sterling et Anja + schéma infographique de la symbiose parasitaire.",
    20: "Artefacts muséaux d'époque Qin : lamelle de bambou calligraphiée par le scribe Bao au Tibet et fiole de bronze ornée de dragons impériaux.",
    21: "Hero Banners grand format pour le gigantesque escalier monolithique immergé de Yonaguni à -30m et les sommets du Kunlun au crépuscule.",
    22: "Application HTML5 simulant les archives déclassifiées du Kremlin et de la DGSE (Projet Kochei) avec blocs noirs à censurer/révéler.",
    23: "Collages moodboards en 4 panneaux reliant les décors et objets clés de l'Atlantide glaciaire et du huis clos en mer sur L'Odyssée.",
    24: "Cartes graphiques de laurier doré et ADN célébrant l'excellence littéraire, la rigueur scientifique et l'archéo-SF du livre.",
    25: "Matrice de comparaison littéraire situant Le Gène de Qin dans la lignée de Michael Crichton, James Rollins et Frank Schätzing.",
    26: "Application HTML5 de chronologie interactive en 5 jalons historiques et scientifiques (221 av. J.-C. → 2026).",
    27: "Dossiers de documentation médicale clinique comparant la progeria d'Élise Valmont à l'enzyme télomérase et à l'autoréparation cellulaire.",
    28: "Visualisation en écran large du parcours lecteur en 4 actes et carte d'expérience techno-thriller exigence & rythme.",
    29: "Hero Banners split-screen en double atmosphère : dualité Tibet/Japon (Kunlun/Yonaguni) et dualité Mer/Glace (L'Odyssée/Le Valmont).",
    30: "Application HTML5 encyclopédie et base de données littéraire répertoriant les 5 lieux, navires et reliques du Gène de Qin.",
    31: "Dossiers de recherche d'auteur montrant le bureau d'enquête historique sur le Tibet (221 av. J.-C.) et le sonar de Yonaguni (-30m).",
    32: "Cartes dilemmes posant au lecteur le prix de l'éternité (ADN vs sablier) et le sacrifice génétique de Léo (60 ans de sa vie en 3 jours).",
    33: "Compendiums en écran large réunissant les 4 théâtres de la saga en un panorama continu et la base géothermique antarctique de Vostok.",
    34: "Application HTML5 de quiz psychologique et tactique en 3 étapes : « Quel héros êtes-vous face à l'immortalité ? »",
    35: "Anatomies et déconstructions techniques de la mise en scène d'action pour la plongée de Yonaguni et la tempête sur L'Odyssée.",
    36: "Matrices de vérité clinique comparant les faits réels vérifiés (progeria, stèle tibétaine 2025) aux extrapolations du techno-thriller.",
    37: "Bandeaux grand format polaires et sous-marins : ciel étoilé antarctique sous aurore boréale et abysse indigo de la fosse de Ryukyu.",
    38: "Application HTML5 Matrice de Vérité interactive distinguant la science réelle du techno-thriller sur 5 dossiers cliniques.",
    39: "Cartes de tropes littéraires KDP pour identifier instantanément les promesses « Techno-Thriller Clinique » et « Archéo-SF Antique ».",
    40: "Overlays de citations immersives sur le lac Léman (Léo : l'intensité de la vie) et sur le bureau de verre (Sterling : l'apothéose).",
    41: "Bandeaux panoramiques sur les sommets du Kunlun en 221 av. J.-C. et sur la passerelle du brise-glace Le Valmont en Antarctique.",
    42: "Application HTML5 Sélecteur de Tropes et d'Intrigues guidant l'acheteur vers l'édition adaptée à ses goûts littéraires.",
    43: "Confrontations duales split-screen : duel idéologique Léo vs Sterling (éthique vs hybris) et duel tactique Samira vs Anja Petrova.",
    44: "Photographies muséales des carnets d'écriture en cuir de Franck Platon annotés sur l'incipit du Tibet et l'épilogue de Genève.",
    45: "Hero Banners immersives de nuit sur la mer Méditerranée (L'Odyssée) et sous-marine à -30m devant la pyramide de Yonaguni.",
    46: "Application HTML5 Face-à-Face confrontant les arguments et citations sur 4 duels de protagonistes.",
    47: "Fiches d'architecture du suspense (20 chapitres sans temps mort / ligne de pouls ECG) et triple échelle de danger (cyan, ambre, rouge).",
    48: "Cartes macro sensorielles plongeant dans la matière : goutte épaisse d'obsidienne noire et cristaux de givre sur pierre sacrée du Tibet.",
    49: "Bandeaux horizon polaire sous le soleil de minuit en Antarctique (Le Valmont) et océanographique en Méditerranée à l'aube (L'Odyssée).",
    50: "Application HTML5 Moniteur d'Analyse du Rythme Narratif (pouls ECG : 95 BPM → 185 BPM) déconstruisant l'intrigue en 4 actes.",
    51: "Fiches de mythologie taoïste : sceau impérial en bronze d'époque Qin orné d'un dragon et calligraphie antique YAO à l'encre obsidienne.",
    52: "Échiquier géopolitique d'espionnage (FSB, Sterling Biotech, La Veille Valmont) et tampon rouge de classification « NIVEAU COSMOS ».",
    53: "Bandeaux émotionnels : serment de Samira Belkacem seule sur la passerelle polaire et mémoire d'Élise sur le lac Léman au coucher du soleil.",
    54: "Application HTML5 Échiquier Géopolitique permettant d'analyser les ressources et motivations secrètes des 4 factions en présence."
}

html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SOMMAIRE GÉNÉRAL INTERACTIF — LE GÈNE DE QIN | FRANCK PLATON</title>
  <style>
    :root {
      --bg-dark: #06080F;
      --card-bg: #0D1322;
      --card-hover: #141D33;
      --border-blue: #1C3358;
      --cyan-neon: #00F0FF;
      --blue-accent: #0D74FF;
      --gold-imperial: #F59E0B;
      --red-alert: #DC2626;
      --text-main: #E2E8F0;
      --text-dim: #64748B;
      --font-mono: 'Courier New', Courier, monospace;
      --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-sans);
      min-height: 100vh;
      line-height: 1.6;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(0, 240, 255, 0.08) 0%, transparent 75%),
        linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px);
      background-size: 100% 100%, 35px 35px, 35px 35px;
    }

    .header-nav {
      position: sticky;
      top: 0;
      background: rgba(6, 8, 15, 0.92);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-blue);
      z-index: 1000;
      padding: 0.75rem 0;
    }

    .nav-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .logo-brand {
      font-family: var(--font-mono);
      font-size: 1.1rem;
      font-weight: bold;
      color: #FFFFFF;
      text-decoration: none;
      letter-spacing: 1px;
    }

    .logo-brand span { color: var(--cyan-neon); }

    .nav-links {
      display: flex;
      gap: 1.25rem;
      flex-wrap: wrap;
    }

    .nav-link {
      color: var(--text-dim);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      transition: color 0.2s;
    }

    .nav-link:hover { color: var(--cyan-neon); }

    .hero-banner {
      max-width: 1280px;
      margin: 3rem auto 2rem auto;
      padding: 0 1.5rem;
      text-align: center;
    }

    .hero-badge {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--gold-imperial);
      background: rgba(245, 158, 11, 0.1);
      border: 1px solid rgba(245, 158, 11, 0.3);
      padding: 0.35rem 0.85rem;
      border-radius: 50px;
      margin-bottom: 1rem;
      letter-spacing: 2px;
    }

    .hero-title {
      font-size: 2.75rem;
      color: #FFFFFF;
      margin-bottom: 0.75rem;
      font-weight: 900;
    }

    .hero-subtitle {
      font-size: 1.15rem;
      color: var(--text-dim);
      max-width: 760px;
      margin: 0 auto 1.75rem auto;
    }

    .pricing-bar {
      display: inline-flex;
      gap: 1.5rem;
      background: var(--card-bg);
      border: 1px solid var(--border-blue);
      padding: 0.75rem 1.75rem;
      border-radius: 50px;
      margin-bottom: 2rem;
      flex-wrap: wrap;
      justify-content: center;
    }

    .price-item {
      font-size: 0.9rem;
      color: var(--text-dim);
    }

    .price-item strong { color: #FFFFFF; font-weight: 700; }

    .piliers-grid {
      max-width: 1280px;
      margin: 0 auto 3rem auto;
      padding: 0 1.5rem;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
    }

    .pilier-card {
      background: var(--card-bg);
      border: 1px solid var(--border-blue);
      border-radius: 10px;
      padding: 1.5rem;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .pilier-card:hover {
      transform: translateY(-4px);
      border-color: var(--cyan-neon);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
    }

    .pilier-tag {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      color: var(--cyan-neon);
      margin-bottom: 0.5rem;
      display: block;
      letter-spacing: 1px;
    }

    .pilier-title {
      font-size: 1.25rem;
      color: #FFFFFF;
      margin-bottom: 0.75rem;
    }

    .pilier-desc {
      font-size: 0.9rem;
      color: var(--text-dim);
      margin-bottom: 1.25rem;
    }

    .btn-action {
      display: inline-block;
      background: rgba(0, 240, 255, 0.1);
      border: 1px solid var(--cyan-neon);
      color: var(--cyan-neon);
      text-decoration: none;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.6rem 1.1rem;
      border-radius: 6px;
      text-align: center;
      transition: all 0.2s ease;
    }

    .btn-action:hover {
      background: var(--cyan-neon);
      color: #06080F;
    }

    .filter-tabs {
      max-width: 1280px;
      margin: 0 auto 2.5rem auto;
      padding: 0 1.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      justify-content: center;
    }

    .filter-btn {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-blue);
      color: var(--text-dim);
      padding: 0.5rem 1rem;
      border-radius: 50px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .filter-btn:hover, .filter-btn.active {
      background: rgba(0, 240, 255, 0.15);
      border-color: var(--cyan-neon);
      color: #FFFFFF;
    }

    .dossiers-grid {
      max-width: 1280px;
      margin: 0 auto 4rem auto;
      padding: 0 1.5rem;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 1.5rem;
    }

    .dossier-card {
      background: var(--card-bg);
      border: 1px solid var(--border-blue);
      border-radius: 10px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
    }

    .dossier-card:hover {
      background: var(--card-hover);
      border-color: rgba(0, 240, 255, 0.4);
      transform: translateY(-3px);
    }

    .dossier-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.75rem;
    }

    .dossier-id {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--gold-imperial);
      font-weight: bold;
    }

    .dossier-cat {
      font-size: 0.7rem;
      color: var(--text-dim);
      background: rgba(255, 255, 255, 0.05);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }

    .dossier-title {
      font-size: 1.15rem;
      color: #FFFFFF;
      margin-bottom: 0.75rem;
    }

    .dossier-desc {
      font-size: 0.85rem;
      color: var(--text-dim);
      margin-bottom: 1.5rem;
      line-height: 1.6;
    }

    .files-list {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      padding-top: 1rem;
    }

    .file-chip {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      font-size: 0.75rem;
      font-family: var(--font-mono);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-main);
      padding: 0.3rem 0.6rem;
      border-radius: 4px;
      text-decoration: none;
      transition: all 0.2s ease;
    }

    .file-chip:hover {
      background: var(--cyan-neon);
      color: #06080F;
      border-color: var(--cyan-neon);
    }

    .file-chip.app-chip {
      background: rgba(245, 158, 11, 0.1);
      border-color: var(--gold-imperial);
      color: var(--gold-imperial);
      font-weight: bold;
    }

    .file-chip.app-chip:hover {
      background: var(--gold-imperial);
      color: #06080F;
    }

    .site-footer {
      border-top: 1px solid var(--border-blue);
      padding: 3rem 1.5rem;
      text-align: center;
      background: #030509;
      margin-top: auto;
    }

    .footer-title {
      font-family: var(--font-mono);
      font-size: 1rem;
      color: #FFFFFF;
      margin-bottom: 0.5rem;
    }

    .footer-desc {
      font-size: 0.85rem;
      color: var(--text-dim);
      margin-bottom: 1.5rem;
    }

    .btn-amazon-large {
      display: inline-block;
      background: linear-gradient(135deg, var(--blue-accent), var(--cyan-neon));
      color: #06080F;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      padding: 0.85rem 2rem;
      border-radius: 6px;
      text-decoration: none;
      transition: all 0.25s ease;
    }

    .btn-amazon-large:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(0, 240, 255, 0.35);
    }
  </style>
</head>
<body>

  <header class="header-nav">
    <div class="nav-container">
      <a href="sommaire.html" class="logo-brand">SOMMAIRE GÉNÉRAL <span>[LE GÈNE DE QIN]</span></a>
      <nav class="nav-links">
        <a href="index.html" class="nav-link">► Site Web Promotionnel</a>
        <a href="COMPTE_RENDU_GENERAL_MISSION_KDP.md" class="nav-link">► Compte Rendu Exécutif</a>
        <a href="bible_le_gene_de_qin.md" class="nav-link">► Bible du Livre</a>
        <a href="aplus_content_le_gene_de_qin.md" class="nav-link">► Dossier A+ KDP</a>
        <a href="rapport_final_le_gene_de_qin.md" class="nav-link">► Rapport SEO & Social</a>
      </nav>
    </div>
  </header>

  <section class="hero-banner">
    <span class="hero-badge">ARCHIVE GLOBALE DE LA MISSION KDP 2026</span>
    <h1 class="hero-title">LE GÈNE DE QIN — FRANCK PLATON</h1>
    <p class="hero-subtitle">
      Répertoire interactif complet de l'écosystème promotionnel : accès direct aux rapports d'expertise, au site web de conversion Amazon KDP et aux <strong>54 dossiers A+ indépendants</strong> créés dans le workspace.
    </p>
    <div class="pricing-bar">
      <span class="price-item">Broché : <strong>10,90 €</strong></span>
      <span class="price-item">Relié Deluxe : <strong>24,99 €</strong></span>
      <span class="price-item">Kindle Ebook : <strong>3,99 €</strong></span>
      <span class="price-item"><a href="https://amzn.eu/d/04xCrOHY" target="_blank" style="color: var(--cyan-neon); text-decoration: underline;">Acheter sur Amazon</a></span>
    </div>
  </section>

  <!-- PILIERS PRINCIPAUX -->
  <section class="piliers-grid">
    <div class="pilier-card">
      <div>
        <span class="pilier-tag">PILIERS PRINCIPAUX // 01</span>
        <h3 class="pilier-title">Site Web Promotionnel KDP</h3>
        <p class="pilier-desc">
          Landing page « One-Page » optimisée SEO, avec couverture officielle, photo auteur, chronologie interactive et liens Amazon KDP.
        </p>
      </div>
      <a href="index.html" class="btn-action">Ouvrir index.html ►</a>
    </div>

    <div class="pilier-card">
      <div>
        <span class="pilier-tag">PILIERS PRINCIPAUX // 02</span>
        <h3 class="pilier-title">Compte Rendu Exécutif Général</h3>
        <p class="pilier-desc">
          Rapport d'expertise synthétisant l'analyse en 13 points, la stratégie SEO A10, le calendrier social 30 jours et la méthodologie.
        </p>
      </div>
      <a href="COMPTE_RENDU_GENERAL_MISSION_KDP.md" class="btn-action">Ouvrir le Compte Rendu ►</a>
    </div>

    <div class="pilier-card">
      <div>
        <span class="pilier-tag">PILIERS PRINCIPAUX // 03</span>
        <h3 class="pilier-title">Bible du Livre & SEO KDP</h3>
        <p class="pilier-desc">
          Source unique de vérité : arcs de Léo, Samira, Sterling et Anja, 7 mots-clés long-tail, bios Author Central et prompt XML.
        </p>
      </div>
      <a href="bible_le_gene_de_qin.md" class="btn-action">Ouvrir la Bible (.md) ►</a>
    </div>

    <div class="pilier-card">
      <div>
        <span class="pilier-tag">PILIERS PRINCIPAUX // 04</span>
        <h3 class="pilier-title">Les 4 Architectures A+ Complètes</h3>
        <p class="pilier-desc">
          Les 4 concepts de pages A+ (Le Choc des Siècles, Le Protocole, Le Sanctuaire, La Guerre Secrète) construits sur 17 modules KDP.
        </p>
      </div>
      <a href="aplus_content_le_gene_de_qin.md" class="btn-action">Ouvrir le Dossier A+ ►</a>
    </div>
  </section>

  <!-- FILTRES PAR CATÉGORIES -->
  <div class="filter-tabs" id="filterTabs">
    <button class="filter-btn active" data-cat="all">TOUS LES DOSSIERS (54)</button>
    <button class="filter-btn" data-cat="cat-a">A. Logos & Marques (2)</button>
    <button class="filter-btn" data-cat="cat-b">B. Bandeaux Hero (10)</button>
    <button class="filter-btn" data-cat="cat-c">C. Cartes & Blueprints (8)</button>
    <button class="filter-btn" data-cat="cat-d">D. Artbooks & High-Tech (4)</button>
    <button class="filter-btn" data-cat="cat-e">E. Personnages & Duels (3)</button>
    <button class="filter-btn" data-cat="cat-f">F. Affiches & Mockups (6)</button>
    <button class="filter-btn" data-cat="cat-g">G. Artefacts Muséaux (4)</button>
    <button class="filter-btn" data-cat="cat-h">H. Tropes & Citations (4)</button>
    <button class="filter-btn" data-cat="cat-i">I. 13 Apps HTML5 Autonomes (13)</button>
  </div>

  <!-- GRILLE DES 54 DOSSIERS -->
  <section class="dossiers-grid" id="dossiersGrid">
"""

# Now let's loop through folders and generate cards
import os
root_dir = "/home/user/pack_aplus_promotion"
folders = sorted(os.listdir(root_dir))

cards_html = ""
for folder in folders:
    path = os.path.join(root_dir, folder)
    if not os.path.isdir(path):
        continue
    
    cat_id, cat_name = get_category(folder)
    num = int(folder.split("_")[0])
    title = folder.replace(f"{num}_", "").replace("_", " ").title()
    desc = descriptions.get(num, "Dossier créatif et modulaire de contenus A+ KDP indépendants sans liens externes.")
    
    files = sorted(os.listdir(path))
    file_chips = ""
    for f in files:
        file_path = f"pack_aplus_promotion/{folder}/{f}"
        if f.endswith(".html"):
            file_chips += f'<a href="{file_path}" class="file-chip app-chip" target="_blank">► {f} (App Web)</a>\n'
        elif f.endswith(".md"):
            file_chips += f'<a href="{file_path}" class="file-chip" target="_blank">📝 {f}</a>\n'
        elif f.endswith((".jpg", ".png")):
            file_chips += f'<a href="{file_path}" class="file-chip" target="_blank">🖼️ {f}</a>\n'
    
    cards_html += f"""
    <div class="dossier-card" data-cat="{cat_id}">
      <div>
        <div class="dossier-header">
          <span class="dossier-id">DOSSIER #{num:02d}</span>
          <span class="dossier-cat">{cat_name.split(" — ")[0]}</span>
        </div>
        <h3 class="dossier-title">{title}</h3>
        <p class="dossier-desc">{desc}</p>
      </div>
      <div class="files-list">
        {file_chips}
      </div>
    </div>
"""

footer_html = """
  </section>

  <footer class="site-footer">
    <h3 class="footer-title">LE GÈNE DE QIN — THRILLER SCIENTIFIQUE DE FRANCK PLATON</h3>
    <p class="footer-desc">
      © 2026 Franck PLATON — Tous droits réservés. Écosystème A+ KDP & Web propulsé par Arena.ai Agent Mode.
    </p>
    <a href="https://amzn.eu/d/04xCrOHY" target="_blank" rel="noopener noreferrer" class="btn-amazon-large">
      COMMANDER SUR AMAZON (FR / BE / CH) ►
    </a>
  </footer>

  <script>
    const filterBtns = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.dossier-card');

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const cat = btn.getAttribute('data-cat');
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        cards.forEach(card => {
          if (cat === 'all' || card.getAttribute('data-cat') === cat) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  </script>
</body>
</html>
"""

with open("/home/user/sommaire.html", "w") as f:
    f.write(html + cards_html + footer_html)

print("sommaire.html generated successfully!!")
