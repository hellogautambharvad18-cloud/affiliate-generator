// ==================== MOBILE MENU ====================
function openSidebar() {
    document.getElementById('mobileSidebar').classList.add('open');
    document.getElementById('sidebarOverlay').classList.add('show');
}
function closeSidebar() {
    document.getElementById('mobileSidebar').classList.remove('open');
    document.getElementById('sidebarOverlay').classList.remove('show');
}
document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeSidebar(); });

// ==================== SMOOTH SCROLL ====================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const t = document.querySelector(this.getAttribute('href'));
        if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});

// ==================== PAGE LOAD ANIMATION ====================
window.addEventListener('load', function() {
    const hero = document.querySelector('.hero-section');
    if (hero) {
        hero.style.opacity = '0';
        hero.style.transform = 'translateY(20px)';
        hero.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        setTimeout(() => { hero.style.opacity = '1'; hero.style.transform = 'translateY(0)'; }, 100);
    }
});

// ==================== FAQ ====================
function toggleFAQ(index) {
    const item = document.querySelector(`.faq-item:nth-child(${index + 1})`);
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
}

// ==================== STICKY CTA BANNER ====================
let lastScrollTop = 0, scrollTimer = null;
function handleCTABannerScroll() {
    const banner = document.getElementById('bottom-cta-banner');
    if (!banner) return;
    const current = window.pageYOffset || document.documentElement.scrollTop;
    if (current !== lastScrollTop) {
        banner.classList.add('hidden');
        if (scrollTimer) clearTimeout(scrollTimer);
        scrollTimer = setTimeout(() => banner.classList.remove('hidden'), 1000);
    }
    lastScrollTop = current;
}
function closeCTABanner() {
    const b = document.getElementById('bottom-cta-banner');
    if (b) { b.style.display = 'none'; localStorage.setItem('ctaBannerClosed', 'true'); }
}
document.addEventListener('DOMContentLoaded', function() {
    if (localStorage.getItem('ctaBannerClosed') === 'true') {
        const b = document.getElementById('bottom-cta-banner');
        if (b) b.style.display = 'none';
        return;
    }
    let ticking = false;
    window.addEventListener('scroll', function() {
        if (!ticking) { requestAnimationFrame(function() { handleCTABannerScroll(); ticking = false; }); ticking = true; }
    });
});