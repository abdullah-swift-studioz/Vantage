document.addEventListener('DOMContentLoaded', () => {

    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');

                // Handle specific animations
                if (entry.target.classList.contains('stat-number-anim')) {
                    animateValue(entry.target);
                }

                if (entry.target.classList.contains('bar-fill')) {
                    animateProgressBar(entry.target);
                }

                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements
    document.querySelectorAll('.stat-card, .service-card, .mentor-card, .testimonial-card, .section-title, .hero-content > *').forEach(el => {
        el.classList.add('fade-up-element');
        observer.observe(el);
    });

    // Observe specific elements for custom animations
    document.querySelectorAll('.stat-number-anim').forEach(el => observer.observe(el));
    document.querySelectorAll('.bar-fill').forEach(el => {
        // Width already in data-width, just waiting for intersection
        observer.observe(el);
    });

    // Number Counter Animation
    function animateValue(obj) {
        const target = parseInt(obj.dataset.target);
        const suffix = obj.dataset.suffix || '';
        const isPercent = obj.innerText.includes('%') || (obj.dataset.target && obj.dataset.target.includes('%'));

        // Determine actual suffix to append
        let finalSuffix = suffix;
        if (isPercent && !suffix.includes('%')) finalSuffix += '%';

        const duration = 2000;
        let startTimestamp = null;

        // Check if target is valid
        if (isNaN(target)) return;

        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);

            // Ease out quart
            const easeProgress = 1 - Math.pow(1 - progress, 4);

            const currentVal = Math.floor(easeProgress * target);

            let displayVal = currentVal.toLocaleString();
            displayVal += finalSuffix;

            obj.innerText = displayVal;

            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                // Ensure final consistency
                obj.innerText = target.toLocaleString() + finalSuffix;
            }
        };

        window.requestAnimationFrame(step);
    }

    // Progress Bar Animation
    function animateProgressBar(el) {
        // Force a reflow
        el.offsetHeight;
        el.style.width = el.dataset.width;
    }

    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        };

        window.addEventListener('scroll', handleScroll);
        // Trigger once on load in case of refresh
        handleScroll();
    }

    // Dropdown Click Logic
    document.querySelectorAll('.nav-link').forEach(link => {
        const dropdown = link.nextElementSibling;
        if (dropdown && dropdown.classList.contains('nav-dropdown')) {
            const navItem = link.parentElement;

            link.addEventListener('click', (e) => {
                e.preventDefault(); // Prevent link navigation
                e.stopPropagation(); // Stop bubbling

                // Close other open dropdowns
                document.querySelectorAll('.nav-item.active').forEach(item => {
                    if (item !== navItem) item.classList.remove('active');
                });

                // Toggle current
                navItem.classList.toggle('active');
            });
        }
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', () => {
        document.querySelectorAll('.nav-item.active').forEach(item => {
            item.classList.remove('active');
        });
    });

    // Stop propagation inside dropdown so clicking inside doesn't close it immediately
    document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
        dropdown.addEventListener('click', (e) => {
            e.stopPropagation();
        });
    });

    // Sticky CTA Close Logic
    const stickyCta = document.querySelector('#stickyCta');
    const closeStickyBtn = document.querySelector('#closeSticky');
    if (stickyCta && closeStickyBtn) {
        closeStickyBtn.addEventListener('click', () => {
            stickyCta.style.display = 'none';
        });
    }

});

// Mobile Menu Toggle (Global function)
// Mobile Menu Toggle (Global function)
function toggleMobileMenu() {
    const menu = document.getElementById('mobileMenu');

    // Toggle the class that moves the menu from "left: -150%" to "left: 0"
    menu.classList.toggle('active');

    // Handle scrolling
    if (menu.classList.contains('active')) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }
}

function toggleMobileSubMenu(subMenuId) {
    const subMenu = document.getElementById(subMenuId);
    if (subMenu) {
        subMenu.style.display = subMenu.style.display === 'flex' ? 'none' : 'flex';

        // Rotate arrow if present
        const btn = document.querySelector(`button[onclick="toggleMobileSubMenu('${subMenuId}')"] span`);
        if (btn) {
            btn.style.transform = subMenu.style.display === 'none' ? 'rotate(0deg)' : 'rotate(180deg)';
            btn.style.transition = 'transform 0.3s ease';
        }
    }
}
