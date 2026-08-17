/**
 * ============================================================
 * SCRIPT INTERACTIF PRINCIPAL — LE GÈNE DE QIN
 * Auteur : Franck PLATON | Promotion Amazon KDP 2026
 * Standard : ES6+ Vanilla JavaScript (Strict Mode, zéro jQuery)
 * ============================================================
 */
'use strict';

/**
 * Initialisation de l'application au chargement du DOM.
 */
document.addEventListener('DOMContentLoaded', () => {
  initMobileNavigation();
  initSmoothScroll();
  initTimelineInteractive();
  initCharacterSecrets();
  initScrollReveal();
  initHeaderScrollEffect();
});

/**
 * 1. NAVIGATION MOBILE RESPONSIVE (BURGER MENU)
 * Gère l'ouverture et la fermeture du menu sur smartphones et tablettes.
 */
function initMobileNavigation() {
  const burgerBtn = document.getElementById('burgerBtn');
  const navLinks = document.getElementById('navLinks');

  if (!burgerBtn || !navLinks) return;

  burgerBtn.addEventListener('click', () => {
    const isExpanded = burgerBtn.getAttribute('aria-expanded') === 'true';
    burgerBtn.setAttribute('aria-expanded', !isExpanded);
    navLinks.classList.toggle('nav-open');
  });

  // Fermer le menu lors d'un clic sur un lien de navigation
  const links = navLinks.querySelectorAll('a');
  links.forEach((link) => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('nav-open');
      burgerBtn.setAttribute('aria-expanded', 'false');
    });
  });
}

/**
 * 2. DÉFILEMENT FLUIDE (SMOOTH SCROLL)
 * Gère le défilement vers les sections d'ancrage avec compensation du header fixe.
 */
function initSmoothScroll() {
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  const headerHeight = 72;

  anchorLinks.forEach((anchor) => {
    anchor.addEventListener('click', function (event) {
      const targetId = this.getAttribute('href');
      if (!targetId || targetId === '#') return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        event.preventDefault();
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerHeight;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

/**
 * 3. CHRONOLOGIE & GÉOGRAPHIE INTERACTIVE (TIMELINE DES LIEUX)
 * Permet d'explorer les 5 nœuds géographiques et scientifiques du roman.
 */
function initTimelineInteractive() {
  const buttons = document.querySelectorAll('.timeline-btn');
  const panels = document.querySelectorAll('.timeline-panel');

  if (buttons.length === 0 || panels.length === 0) return;

  buttons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const targetNode = btn.getAttribute('data-node');

      // Réinitialiser tous les boutons et panneaux
      buttons.forEach((b) => b.classList.remove('active'));
      panels.forEach((p) => {
        p.classList.remove('active');
        p.setAttribute('hidden', 'true');
      });

      // Activer le bouton sélectionné et son panneau associé
      btn.classList.add('active');
      const targetPanel = document.getElementById(`panel-${targetNode}`);
      if (targetPanel) {
        targetPanel.removeAttribute('hidden');
        targetPanel.classList.add('active');
      }
    });
  });
}

/**
 * 4. INTERACTION DES CARACTÈRES (RÉVÉLATION DE SECRETS NARRATIFS)
 * Gère le déploiement des cartes personnages au clic.
 */
function initCharacterSecrets() {
  const characterCards = document.querySelectorAll('.character-card');

  characterCards.forEach((card) => {
    const moreBtn = card.querySelector('.char-more-btn');
    const secretBox = card.querySelector('.char-secret');

    if (!moreBtn || !secretBox) return;

    moreBtn.addEventListener('click', () => {
      const isHidden = secretBox.hasAttribute('hidden');
      if (isHidden) {
        secretBox.removeAttribute('hidden');
        moreBtn.textContent = 'Masquer le détail ↑';
        moreBtn.setAttribute('aria-expanded', 'true');
      } else {
        secretBox.setAttribute('hidden', 'true');
        moreBtn.textContent = 'Découvrir son arc narratif ↓';
        moreBtn.setAttribute('aria-expanded', 'false');
      }
    });
  });
}

/**
 * 5. ANIMATIONS AU DÉFILEMENT (SCROLL REVEAL VIA INTERSECTION OBSERVER)
 * Révèle dynamiquement les sections au fur et à mesure du scroll lecteur.
 */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.scroll-reveal');
  if (!('IntersectionObserver' in window) || revealElements.length === 0) {
    // Fallback si IntersectionObserver non supporté
    revealElements.forEach((el) => el.classList.add('revealed'));
    return;
  }

  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -60px 0px',
    threshold: 0.15
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  revealElements.forEach((el) => revealObserver.observe(el));
}

/**
 * 6. EFFET D'EN-TÊTE AU DEFILEMENT (HEADER GLASSMORPHISM)
 * Renforce le flou et l'ombre du header lorsque l'utilisateur descend sur la page.
 */
function initHeaderScrollEffect() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.style.boxShadow = '0 10px 30px rgba(0,0,0,0.7)';
      header.style.backgroundColor = 'rgba(10, 10, 12, 0.95)';
    } else {
      header.style.boxShadow = 'none';
      header.style.backgroundColor = 'rgba(10, 10, 12, 0.88)';
    }
  });
}
