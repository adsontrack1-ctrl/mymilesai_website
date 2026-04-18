// MyMilesAI — shared.js — loaded on every page

(function() {
  'use strict';

  // ============ NAV: Highlight current page ============
  function highlightCurrentNav() {
    const path = location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(a => {
      const href = (a.getAttribute('href') || '').split('/').pop();
      if (href === path) a.classList.add('active');
    });
  }

  // ============ NAV: Mobile menu toggle ============
  function wireMobileMenu() {
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.querySelector('.mobile-menu');
    if (!toggle || !menu) return;
    toggle.addEventListener('click', () => {
      menu.classList.toggle('open');
    });
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => menu.classList.remove('open')));
  }

  // ============ FAQ: accordion ============
  function wireFaq() {
    document.querySelectorAll('.faq-item').forEach(item => {
      const q = item.querySelector('.faq-q');
      if (!q) return;
      q.addEventListener('click', () => {
        const wasOpen = item.classList.contains('open');
        // Close siblings
        item.parentElement.querySelectorAll('.faq-item.open').forEach(el => el.classList.remove('open'));
        if (!wasOpen) item.classList.add('open');
      });
    });
  }

  // ============ Locale detection ============
  function detectLocale() {
    const el = document.querySelector('[data-locale]');
    if (!el) return;
    try {
      const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
      const lang = (navigator.language || '').toLowerCase();
      const isCanada = /america\/(toronto|vancouver|edmonton|winnipeg|halifax|montreal|regina|st_johns)/i.test(tz) || lang.includes('-ca');
      if (isCanada) {
        el.textContent = '🇨🇦 CA';
        document.querySelectorAll('[data-us-only]').forEach(e => e.style.display = 'none');
        document.querySelectorAll('[data-ca-only]').forEach(e => e.style.display = '');
      }
    } catch(e) {}
  }

  // ============ Simple scroll reveal ============
  function wireReveal() {
    const items = document.querySelectorAll('.reveal');
    if (!items.length) return;
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    items.forEach(i => io.observe(i));
  }

  // ============ Auth modal (simple placeholder that links to dashboard) ============
  function wireAuthButtons() {
    document.querySelectorAll('[data-auth="signin"]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        // For now, point to dashboard.html which has the full auth flow
        window.location.href = 'dashboard.html';
      });
    });
  }

  // ============ Init ============
  function init() {
    highlightCurrentNav();
    wireMobileMenu();
    wireFaq();
    detectLocale();
    wireReveal();
    wireAuthButtons();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
