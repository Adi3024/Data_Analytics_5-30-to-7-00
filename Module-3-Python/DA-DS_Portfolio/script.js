/**
 * DA-DS Portfolio Interactivity
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // --- Set Current Year dynamically ---
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // --- Mobile Menu Toggle ---
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navLinks = document.getElementById('nav-links');
    
    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            // Toggle icon from bars to xmark (close)
            const icon = mobileMenuBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });
        
        // Close menu when clicking a link
        const links = navLinks.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                const icon = mobileMenuBtn.querySelector('i');
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            });
        });
    }

    // --- Navbar Scroll Effect ---
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // --- Active Link Highlighting based on scroll position ---
    const sections = document.querySelectorAll('section');
    const navItems = document.querySelectorAll('.nav-link');
    
    window.addEventListener('scroll', () => {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            // Need to adjust slightly to catch the top
            if (scrollY >= (sectionTop - sectionHeight / 3)) {
                current = section.getAttribute('id');
            }
        });

        navItems.forEach(item => {
            item.classList.remove('active');
            if (current && item.getAttribute('href').includes(current)) {
                item.classList.add('active');
            } else if (!current && item.getAttribute('href').includes('home')) {
                item.classList.add('active');
            }
        });
    });

    // --- Initialize AOS (Animate On Scroll) ---
    AOS.init({
        duration: 800,
        once: false,
        offset: 100,
    });

    // --- Initialize Typed.js ---
    const typedTextSpan = document.querySelector('.typed-text');
    if (typedTextSpan) {
        new Typed('.typed-text', {
            strings: ['Data Analyst', 'Problem Solver', 'Data Storyteller', 'Tech Enthusiast'],
            typeSpeed: 50,
            backSpeed: 30,
            backDelay: 2000,
            loop: true
        });
    }

    // --- Animated Skill Bars ---
    const progressLines = document.querySelectorAll('.progress-line span');
    
    // Create an observer just for the skill bars so they animate from 0 to width when visible
    const skillObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                const width = bar.getAttribute('data-width');
                bar.style.width = width;
                observer.unobserve(bar); // Only animate once
            }
        });
    }, { threshold: 0.5 });

    progressLines.forEach(line => {
        // Reset width to 0 initial state
        line.style.width = '0%';
        skillObserver.observe(line);
    });

    // --- Project Filtering ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');
            
            const filterValue = btn.getAttribute('data-filter');
            
            projectCards.forEach(card => {
                const categories = card.getAttribute('data-category');
                
                if (filterValue === 'all' || categories.includes(filterValue)) {
                    card.style.display = 'flex';
                    // Trigger AOS reframing if needed or simple fade
                    card.classList.remove('aos-animate');
                    setTimeout(() => card.classList.add('aos-animate'), 50);
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

});
