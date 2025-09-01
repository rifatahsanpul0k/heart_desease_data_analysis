// Smooth scroll for navigation links
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

// Header background on scroll
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (window.scrollY > 100) {
        header.style.background = 'rgba(13, 17, 23, 0.98)';
    } else {
        header.style.background = 'rgba(13, 17, 23, 0.95)';
    }
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', () => {
    const animateElements = document.querySelectorAll('.overview-card, .feature-item, .step, .capability');
    
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Mobile menu toggle (if needed in future)
const createMobileMenu = () => {
    const nav = document.querySelector('.nav');
    const navLinks = document.querySelector('.nav-links');
    
    if (window.innerWidth <= 768) {
        if (!document.querySelector('.mobile-menu-toggle')) {
            const toggle = document.createElement('button');
            toggle.classList.add('mobile-menu-toggle');
            toggle.innerHTML = '☰';
            toggle.style.cssText = `
                background: none;
                border: none;
                color: var(--text-primary);
                font-size: 1.5rem;
                cursor: pointer;
                display: block;
            `;
            
            toggle.addEventListener('click', () => {
                navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '100%';
                navLinks.style.left = '0';
                navLinks.style.right = '0';
                navLinks.style.background = 'var(--dark-bg)';
                navLinks.style.padding = '1rem';
                navLinks.style.borderTop = '1px solid var(--border-color)';
            });
            
            nav.appendChild(toggle);
        }
    }
};

// Call mobile menu function on resize
window.addEventListener('resize', createMobileMenu);
createMobileMenu();

// Add loading animation
window.addEventListener('load', () => {
    document.body.style.opacity = '1';
    document.body.style.transition = 'opacity 0.5s ease';
});

// Initialize page
document.body.style.opacity = '0';