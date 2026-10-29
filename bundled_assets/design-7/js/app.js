(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {

    var toggle = document.querySelector('.mv-toggle');
    var links = document.querySelector('.mv-links');
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

    document.querySelectorAll('.mv-faq-row').forEach(function (row) {
      var btn = row.querySelector('.mv-faq-btn');
      var body = row.querySelector('.mv-faq-body');
      if (!btn || !body) return;
      btn.addEventListener('click', function () {
        var wasOpen = row.classList.contains('on');
        document.querySelectorAll('.mv-faq-row').forEach(function (o) {
          o.classList.remove('on');
          var ob = o.querySelector('.mv-faq-body');
          if (ob) ob.style.maxHeight = null;
          var oq = o.querySelector('.mv-faq-btn');
          if (oq) oq.setAttribute('aria-expanded', 'false');
        });
        if (!wasOpen) {
          row.classList.add('on');
          body.style.maxHeight = body.scrollHeight + 'px';
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });

    /* ---- the synapse spark: small interconnected nodes with a travelling spark of light, echoing neural synapse connections ---- */
    var host = document.querySelector('.mv-ascent');
    if (host) {
      var NS = 'http://www.w3.org/2000/svg';

      var svg = document.createElementNS(NS, 'svg');
      svg.setAttribute('viewBox', '0 0 120 50');
      svg.setAttribute('width', '112'); svg.setAttribute('height', '46');
      svg.setAttribute('role', 'img');
      svg.setAttribute('aria-label', 'A small web of interconnected nodes with a travelling spark of light, echoing neural synapse connections');

      var nodes = [[12,25],[38,10],[38,40],[62,25],[86,12],[86,38],[108,25]];
      var links = [[0,1],[0,2],[1,3],[2,3],[3,4],[3,5],[4,6],[5,6]];
      links.forEach(function(l){
        var a = nodes[l[0]], b = nodes[l[1]];
        var ln = document.createElementNS(NS, 'line');
        ln.setAttribute('x1', a[0]); ln.setAttribute('y1', a[1]);
        ln.setAttribute('x2', b[0]); ln.setAttribute('y2', b[1]);
        ln.setAttribute('class', 'mv-syn-line');
        svg.appendChild(ln);
      });
      nodes.forEach(function(n, i){
        var dot = document.createElementNS(NS, 'circle');
        dot.setAttribute('cx', n[0]); dot.setAttribute('cy', n[1]); dot.setAttribute('r', 3);
        dot.setAttribute('class', 'mv-syn-node');
        svg.appendChild(dot);
        var spark = document.createElementNS(NS, 'circle');
        spark.setAttribute('cx', n[0]); spark.setAttribute('cy', n[1]); spark.setAttribute('r', 4);
        spark.setAttribute('class', 'mv-syn-spark');
        spark.style.animationDelay = (i * 0.25) + 's';
        svg.appendChild(spark);
      });

      host.querySelector('h4').insertAdjacentElement('afterend', svg);

      var cap = document.createElement('div');
      cap.className = 'mv-ascent-cap';
      cap.textContent = 'Daily Serving';
      svg.insertAdjacentElement('afterend', cap);
    }

  });
})();
