(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {

    var toggle = document.querySelector('.ge-toggle');
    var links = document.querySelector('.ge-links');
    if (toggle && links) {
      toggle.addEventListener('click', function () {
        var open = links.classList.toggle('open');
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      links.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () {
          links.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
        });
      });
    }

    document.querySelectorAll('.ge-faq-row').forEach(function (row) {
      var btn = row.querySelector('.ge-faq-btn');
      var body = row.querySelector('.ge-faq-body');
      if (!btn || !body) return;
      btn.addEventListener('click', function () {
        var wasOpen = row.classList.contains('on');
        document.querySelectorAll('.ge-faq-row').forEach(function (o) {
          o.classList.remove('on');
          var ob = o.querySelector('.ge-faq-body');
          if (ob) ob.style.maxHeight = null;
          var oq = o.querySelector('.ge-faq-btn');
          if (oq) oq.setAttribute('aria-expanded', 'false');
        });
        if (!wasOpen) {
          row.classList.add('on');
          body.style.maxHeight = body.scrollHeight + 'px';
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });

    /* ---- renewal glow: concentric rings brighten outward in sequence ---- */
    var host = document.querySelector('.ge-glow');
    if (host) {
      var svgWrap = host.querySelector('.ge-glow-svg');
      svgWrap.innerHTML =
        '<svg viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg">' +
        '<circle cx="100" cy="60" r="10" fill="#A67C3D" class="r0" />' +
        '<circle cx="100" cy="60" r="24" fill="none" stroke="#D88A93" stroke-width="2.5" class="r1" />' +
        '<circle cx="100" cy="60" r="38" fill="none" stroke="#D88A93" stroke-width="2" opacity="0" class="r2" />' +
        '<circle cx="100" cy="60" r="52" fill="none" stroke="#E9D9CA" stroke-width="1.5" opacity="0" class="r3" />' +
        '</svg>';
      var circles = host.querySelectorAll('.ge-glow-svg circle');
      var played = false;
      function play() {
        if (played) return;
        played = true;
        circles.forEach(function (c, i) {
          setTimeout(function () { c.classList.add('on'); }, 220 * i);
        });
      }
      if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (entries) {
          entries.forEach(function (e) { if (e.isIntersecting) { play(); io.disconnect(); } });
        }, { threshold: 0.4 });
        io.observe(host);
      } else {
        play();
      }
    }

  });
})();
