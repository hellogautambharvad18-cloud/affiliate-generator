(function(){
  // Reveal-on-scroll + animate dossier bars and radial gauges
  // Safety net: if anything below throws, ensure nothing stays hidden
  setTimeout(function(){
    document.querySelectorAll('.vc-reveal:not(.is-in)').forEach(function(el){
      el.classList.add('is-in');
      var bar=el.querySelector('.vc-doss__track i');
      if(bar){bar.style.setProperty('--w',(el.getAttribute('data-w')||0)+'%');}
    });
  },2500);
  var els=document.querySelectorAll('.vc-reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(!e.isIntersecting) return;
        var el=e.target; el.classList.add('is-in');
        var bar=el.querySelector('.vc-doss__track i')||el.querySelector('.vc-clock__track i');
        if(bar){ bar.style.setProperty('--w',(el.getAttribute('data-w')||0)+'%'); }
        var g=el.querySelector('.vc-gauge__fg');
        if(g){ var p=parseFloat(el.getAttribute('data-pct')||0);
               g.style.strokeDashoffset=(226-(226*p/100)).toFixed(0); }
        io.unobserve(el);
      });
    },{threshold:0.18});
    els.forEach(function(el){io.observe(el);});
  } else {
    els.forEach(function(el){
      el.classList.add('is-in');
      var bar=el.querySelector('.vc-doss__track i');
      if(bar){bar.style.setProperty('--w',(el.getAttribute('data-w')||0)+'%');}
    });
  }
  // Scrollspy on the homepage nav
  var secs=[].slice.call(document.querySelectorAll('main section[id]'));
  var links=[].slice.call(document.querySelectorAll('.vc-nav .nav-link[href*="#"]'));
  if(secs.length && links.length && 'IntersectionObserver' in window){
    var so=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(!e.isIntersecting) return;
        var id=e.target.getAttribute('id');
        links.forEach(function(a){
          a.classList.toggle('active', a.getAttribute('href').split('#')[1]===id);
        });
      });
    },{rootMargin:'-45% 0px -50% 0px'});
    secs.forEach(function(s){so.observe(s);});
  }
  // Bootstrap JS fallback: wire collapse + accordion if the CDN bundle is absent
  if(!window.bootstrap){
    document.querySelectorAll('[data-bs-toggle="collapse"]').forEach(function(btn){
      btn.addEventListener('click',function(){
        var t=document.querySelector(btn.getAttribute('data-bs-target'));
        if(!t) return;
        var open=t.classList.toggle('show');
        btn.setAttribute('aria-expanded',open?'true':'false');
        btn.classList.toggle('collapsed',!open);
        var parent=t.getAttribute('data-bs-parent');
        if(open && parent){
          document.querySelectorAll(parent+' .accordion-collapse.show').forEach(function(o){
            if(o!==t){
              o.classList.remove('show');
              var ob=document.querySelector('[data-bs-target="#'+o.id+'"]');
              if(ob){ob.classList.add('collapsed');ob.setAttribute('aria-expanded','false');}
            }
          });
        }
      });
    });
  }
  // Close the mobile collapse after tapping an in-page anchor
  var nav=document.getElementById('vcNav');
  if(nav){
    nav.addEventListener('click',function(ev){
      var a=ev.target.closest('a'); if(!a) return;
      if(!nav.classList.contains('show')) return;
      if(window.bootstrap){
        var c=window.bootstrap.Collapse.getOrCreateInstance(nav); if(c) c.hide();
      } else {
        nav.classList.remove('show');
        var t=document.querySelector('[data-bs-target="#vcNav"]');
        if(t){t.classList.add('collapsed');t.setAttribute('aria-expanded','false');}
      }
    });
  }
})();