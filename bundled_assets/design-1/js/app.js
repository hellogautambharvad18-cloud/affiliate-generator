(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', function () {

    var toggle = document.querySelector('.bpo-toggle');
    var links = document.querySelector('.bpo-links');
    if (toggle && links) {
      toggle.addEventListener('click', function () {
        var open = links.classList.toggle('open');
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      links.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () { links.classList.remove('open'); });
      });
    }

    document.querySelectorAll('.bpo-faq-row').forEach(function (row) {
      var btn = row.querySelector('.bpo-faq-btn');
      var body = row.querySelector('.bpo-faq-body');
      if (!btn || !body) return;
      btn.addEventListener('click', function () {
        var wasOpen = row.classList.contains('on');
        document.querySelectorAll('.bpo-faq-row').forEach(function (o) {
          o.classList.remove('on');
          var ob = o.querySelector('.bpo-faq-body');
          if (ob) ob.style.maxHeight = null;
        });
        if (!wasOpen) {
          row.classList.add('on');
          body.style.maxHeight = body.scrollHeight + 'px';
        }
      });
    });

  });
})();
