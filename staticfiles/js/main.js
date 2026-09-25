// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const navLinksItems = document.querySelectorAll('.nav-links a');

    function setMenuOpen(isOpen) {
        document.body.classList.toggle('menu-open', isOpen);
    }
    
    if (mobileMenuToggle && navLinks) {
        mobileMenuToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            const willOpen = !navLinks.classList.contains('active');
            navLinks.classList.toggle('active');
            this.classList.toggle('active');
            setMenuOpen(willOpen);
        });
        
        // Close menu when clicking on a link
        navLinksItems.forEach(link => {
            link.addEventListener('click', function() {
                navLinks.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                setMenuOpen(false);
            });
        });
        // Keep mobile menu open when using services dropdown toggle
        const dropToggle = navLinks.querySelector('.nav-dropdown-toggle');
        if (dropToggle) {
            dropToggle.addEventListener('click', function(e) {
                e.stopPropagation();
            });
        }
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!navLinks.contains(e.target) && !mobileMenuToggle.contains(e.target)) {
                navLinks.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                setMenuOpen(false);
            }
        });
        
        // Close menu on window resize if it becomes desktop size
        window.addEventListener('resize', function() {
            if (window.innerWidth > 768) {
                navLinks.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                setMenuOpen(false);
            }
        });
    }
    
    // Services dropdown
    document.querySelectorAll('.nav-dropdown').forEach(function(drop) {
        const toggle = drop.querySelector('.nav-dropdown-toggle');
        if (!toggle) return;
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            const open = drop.classList.toggle('open');
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
            document.querySelectorAll('.nav-dropdown').forEach(function(other) {
                if (other !== drop) {
                    other.classList.remove('open');
                    const t = other.querySelector('.nav-dropdown-toggle');
                    if (t) t.setAttribute('aria-expanded', 'false');
                }
            });
        });
    });
    document.addEventListener('click', function() {
        document.querySelectorAll('.nav-dropdown.open').forEach(function(drop) {
            drop.classList.remove('open');
            const t = drop.querySelector('.nav-dropdown-toggle');
            if (t) t.setAttribute('aria-expanded', 'false');
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('.service-card, .person-card, .equipment-card, .staff-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

