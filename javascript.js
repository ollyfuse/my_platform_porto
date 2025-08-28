// Navigation functionality
document.addEventListener('DOMContentLoaded', function() {
    // Theme toggle functionality
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const body = document.body;

    // Check for saved theme preference or default to 'light'
    const currentTheme = localStorage.getItem('theme') || 'light';
    body.setAttribute('data-theme', currentTheme);

    // Update icon based on current theme
    updateThemeIcon(currentTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = body.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            body.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (themeIcon) {
            if (theme === 'dark') {
                themeIcon.className = 'fas fa-sun';
            } else {
                themeIcon.className = 'fas fa-moon';
            }
        }
    }
    // Mobile navigation toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }

    // Enhanced smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('.nav-link');
    const navbar = document.querySelector('.navbar');
    const navbarHeight = navbar ? navbar.offsetHeight : 80;

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                // Calculate the exact position accounting for navbar height
                const targetPosition = targetSection.offsetTop - navbarHeight - 20; // 20px extra padding

                // Enhanced smooth scroll with custom easing
                smoothScrollTo(targetPosition, 1000); // 1 second duration
            }

            // Close mobile menu if open
            if (navMenu && navMenu.classList.contains('active')) {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            }

            // Update active link with smooth transition
            navLinks.forEach(navLink => {
                navLink.classList.remove('active');
                navLink.style.transition = 'color 0.3s ease';
            });
            this.classList.add('active');
        });
    });

    // Custom smooth scroll function with easing
    function smoothScrollTo(targetPosition, duration) {
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        let startTime = null;

        function animation(currentTime) {
            if (startTime === null) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const run = easeInOutCubic(timeElapsed, startPosition, distance, duration);
            window.scrollTo(0, run);
            if (timeElapsed < duration) requestAnimationFrame(animation);
        }

        // Easing function for smooth animation
        function easeInOutCubic(t, b, c, d) {
            t /= d / 2;
            if (t < 1) return c / 2 * t * t * t + b;
            t -= 2;
            return c / 2 * (t * t * t + 2) + b;
        }

        requestAnimationFrame(animation);
    }

    // Apply smooth scrolling to all internal links
    const allInternalLinks = document.querySelectorAll('a[href^="#"]');
    allInternalLinks.forEach(link => {
        // Skip if it's already a nav-link (already handled above)
        if (!link.classList.contains('nav-link')) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetSection = document.querySelector(targetId);

                if (targetSection) {
                    const targetPosition = targetSection.offsetTop - navbarHeight - 20;
                    smoothScrollTo(targetPosition, 1000);

                    // Update active nav link
                    const correspondingNavLink = document.querySelector(`.nav-link[href="${targetId}"]`);
                    if (correspondingNavLink) {
                        navLinks.forEach(navLink => navLink.classList.remove('active'));
                        correspondingNavLink.classList.add('active');
                    }
                }
            });
        }
    });

    // Project filter functionality
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectItems = document.querySelectorAll('.project-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');

            // Update active filter button
            filterBtns.forEach(filterBtn => filterBtn.classList.remove('active'));
            this.classList.add('active');

            // Filter projects
            projectItems.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-category') === filter) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });

    // Contact form handling
    const contactForm = document.getElementById('contactForm');
    const submitBtn = document.getElementById('submitBtn');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(this);
            const email = formData.get('email');
            const subject = formData.get('subject');
            const message = formData.get('message');

            // Basic validation
            if (!email || !subject || !message) {
                showFormMessage('Please fill in all fields', 'error');
                return;
            }

            // reCAPTCHA validation
            const recaptchaResponse = grecaptcha.getResponse();
            if (!recaptchaResponse) {
                showFormMessage('Please complete the reCAPTCHA verification', 'error');
                return;
            }

            // Disable submit button
            submitBtn.disabled = true;
            submitBtn.textContent = 'Sending...';

            // Simulate form submission
            setTimeout(() => {
                showFormMessage('Thank you for your message! I will get back to you soon.', 'success');
                this.reset();
                grecaptcha.reset();
                submitBtn.disabled = false;
                submitBtn.textContent = 'Send Message';
            }, 1500);
        });
    }

    function showFormMessage(message, type) {
        const existingMessage = document.querySelector('.form-message');
        if (existingMessage) existingMessage.remove();

        const messageDiv = document.createElement('div');
        messageDiv.className = `form-message ${type}`;
        messageDiv.textContent = message;
        
        submitBtn.parentNode.insertBefore(messageDiv, submitBtn);
        
        setTimeout(() => messageDiv.remove(), 5000);
    }

    // Scroll progress indicator
    const scrollProgress = document.getElementById('scroll-progress');

    // Enhanced scroll-based navigation highlighting and progress
    let isScrolling = false;

    window.addEventListener('scroll', () => {
        if (!isScrolling) {
            window.requestAnimationFrame(() => {
                updateActiveNavLink();
                updateScrollProgress();
                isScrolling = false;
            });
            isScrolling = true;
        }
    });

    function updateScrollProgress() {
        if (scrollProgress) {
            const scrollTop = window.pageYOffset;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrollPercent = (scrollTop / docHeight) * 100;
            scrollProgress.style.width = scrollPercent + '%';
        }
    }

    function updateActiveNavLink() {
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('.nav-link');
        const scrollPosition = window.scrollY + navbarHeight + 50; // Account for navbar and some padding

        let current = '';

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionBottom = sectionTop + section.offsetHeight;

            // Check if the section is currently in view
            if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                current = section.getAttribute('id');
            }
        });

        // Handle the case when we're at the very top
        if (window.scrollY < 100) {
            current = 'home';
        }

        // Update active states with smooth transitions
        navLinks.forEach(link => {
            const isActive = link.getAttribute('href') === '#' + current;

            if (isActive && !link.classList.contains('active')) {
                // Remove active from all links first
                navLinks.forEach(navLink => navLink.classList.remove('active'));
                // Add active to current link
                link.classList.add('active');
            }
        });
    }

    // Navbar background on scroll
    window.addEventListener('scroll', () => {
        const navbar = document.querySelector('.navbar');
        const currentTheme = body.getAttribute('data-theme') || 'light';

        if (window.scrollY > 100) {
            if (currentTheme === 'dark') {
                navbar.style.background = 'rgba(31, 41, 55, 0.98)';
            } else {
                navbar.style.background = 'rgba(52, 53, 57, 0.98)';
            }
        } else {
            if (currentTheme === 'dark') {
                navbar.style.background = 'rgba(31, 41, 55, 0.95)';
            } else {
                navbar.style.background = 'rgba(52, 53, 57, 0.95)';
            }
        }
    });

    // Animate skill bars when in view
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const skillBars = entry.target.querySelectorAll('.skill-progress');
                skillBars.forEach(bar => {
                    const width = bar.style.width;
                    bar.style.width = '0%';
                    setTimeout(() => {
                        bar.style.width = width;
                    }, 100);
                });
            }
        });
    }, observerOptions);

    const skillsSection = document.querySelector('.skills');
    if (skillsSection) {
        observer.observe(skillsSection);
    }

    // Section fade-in animation on scroll
    const sections = document.querySelectorAll('section:not(#home)'); // Exclude hero section

    // Add fade-in class initially
    sections.forEach(section => {
        section.classList.add('fade-in');
    });

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    sections.forEach(section => {
        sectionObserver.observe(section);
    });

    // Initialize scroll progress on page load
    updateScrollProgress();

    // Chat Widget Functionality
    const chatToggle = document.getElementById('chatToggle');
    const chatWidget = document.getElementById('chatWidget');
    const chatClose = document.getElementById('chatClose');
    const chatInput = document.getElementById('chatInput');
    const chatSend = document.getElementById('chatSend');
    const chatMessages = document.getElementById('chatMessages');
    const agentSelect = document.getElementById('agentSelect');

    // API endpoint - use Netlify functions in production
    const API_BASE = window.location.hostname === 'localhost' 
        ? 'http://localhost:8000' 
        : '/.netlify/functions';

    // Toggle chat widget
    chatToggle.addEventListener('click', () => {
        chatWidget.classList.toggle('active');
        if (chatWidget.classList.contains('active')) {
            chatInput.focus();
            if (chatMessages.children.length === 0) {
                addMessage('Hello! I\'m Olivier\'s AI assistant. How can I help you today?', 'bot');
            }
        }
    });

    chatClose.addEventListener('click', () => {
        chatWidget.classList.remove('active');
    });

    // Send message function
    async function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        addMessage(message, 'user');
        chatInput.value = '';
        
        // Show typing indicator
        const typingMsg = addMessage('Thinking...', 'bot');
        
        try {
            const response = await fetch(`${API_BASE}/api/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    agent_type: agentSelect.value
                })
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            
            // Remove typing indicator
            typingMsg.remove();
            
            // Add bot response
            addMessage(data.response, 'bot');
            
        } catch (error) {
            console.error('Chat error:', error);
            typingMsg.remove();
            addMessage('Sorry, I\'m having trouble connecting right now. Please try again later or contact me directly at cyotero26@gmail.com', 'bot');
        }
    }

    // Add message to chat
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        return messageDiv;
    }

    // Send message on button click
    chatSend.addEventListener('click', sendMessage);

    // Send message on Enter key
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Agent selection change
    agentSelect.addEventListener('change', () => {
        const agentName = agentSelect.options[agentSelect.selectedIndex].text;
        addMessage(`Switched to ${agentName}. How can I help you?`, 'bot');
    });

    // Reflection Journal Functionality
    const journalText = document.getElementById('journalText');
    const addReflectionBtn = document.getElementById('addReflection');
    const journalEntries = document.getElementById('journalEntries');

    // Load saved reflections from localStorage
    loadReflections();

    addReflectionBtn.addEventListener('click', addReflection);
    journalText.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && e.ctrlKey) {
            addReflection();
        }
    });

    function addReflection() {
        const text = journalText.value.trim();
        if (!text) return;

        const reflection = {
            id: Date.now(),
            content: text,
            date: new Date().toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'short',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
            })
        };

        // Add to DOM
        const entryDiv = createReflectionEntry(reflection);
        journalEntries.insertBefore(entryDiv, journalEntries.firstChild);

        // Save to localStorage
        saveReflection(reflection);

        // Clear input
        journalText.value = '';
        
        // Scroll to top of entries
        journalEntries.scrollTop = 0;
    }

    function createReflectionEntry(reflection) {
        const entryDiv = document.createElement('div');
        entryDiv.className = 'journal-entry';
        entryDiv.innerHTML = `
            <div class="entry-date">${reflection.date}</div>
            <div class="entry-content">${reflection.content}</div>
        `;
        return entryDiv;
    }

    function saveReflection(reflection) {
        const reflections = JSON.parse(localStorage.getItem('reflections') || '[]');
        reflections.unshift(reflection);
        // Keep only last 50 reflections
        if (reflections.length > 50) reflections.pop();
        localStorage.setItem('reflections', JSON.stringify(reflections));
    }

    function loadReflections() {
        const reflections = JSON.parse(localStorage.getItem('reflections') || '[]');
        // Clear default entry if we have saved reflections
        if (reflections.length > 0) {
            journalEntries.innerHTML = '';
        }
        reflections.forEach(reflection => {
            const entryDiv = createReflectionEntry(reflection);
            journalEntries.appendChild(entryDiv);
        });
    }
});

