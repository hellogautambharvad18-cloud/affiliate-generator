/* ============================================================
   BREATHIZEN™ — bbreathizen.com — js/script.js
   ============================================================ */

function toggleMenu() {
  document.getElementById('mobileMenu').classList.toggle('open');
}

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.mobile-menu a').forEach(function (link) {
    link.addEventListener('click', function () {
      document.getElementById('mobileMenu').classList.remove('open');
    });
  });
});

function toggleFaq(btn) {
  var item = btn.closest('.faq-item');
  document.querySelectorAll('.faq-item').forEach(function (i) {
    if (i !== item) {
      i.classList.remove('open');
      var b = i.querySelector('.faq-question');
      if (b) b.setAttribute('aria-expanded', 'false');
    }
  });
  var isOpen = item.classList.toggle('open');
  btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
}

document.addEventListener('DOMContentLoaded', function () {
  var fadeEls = document.querySelectorAll('.fade-up');
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });
    fadeEls.forEach(function (el) { observer.observe(el); });
  } else {
    fadeEls.forEach(function (el) { el.classList.add('visible'); });
  }
});

window.addEventListener('scroll', function () {
  var nav = document.querySelector('nav');
  nav.style.boxShadow = window.scrollY > 10
    ? '0 4px 28px rgba(28,43,58,0.65)'
    : '0 2px 20px rgba(28,43,58,0.5)';
}, { passive: true });

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
});