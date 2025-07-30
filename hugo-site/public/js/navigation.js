/**
 * Simple navigation and interactions for CNS 2.0 blog
 */

document.addEventListener('DOMContentLoaded', function() {
    // Mobile navigation toggle
    const navToggle = document.getElementById('nav-toggle');
    const navList = document.querySelector('.nav-list');

    if (navToggle && navList) {
        navToggle.addEventListener('click', function() {
            navList.classList.toggle('active');
            
            // Update icon
            const icon = navToggle.querySelector('i');
            if (icon) {
                const isOpen = navList.classList.contains('active');
                icon.setAttribute('data-feather', isOpen ? 'x' : 'menu');
                if (window.feather) feather.replace();
            }
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!navToggle.contains(event.target) && !navList.contains(event.target) && navList.classList.contains('active')) {
                navList.classList.remove('active');
                const icon = navToggle.querySelector('i');
                if (icon) {
                    icon.setAttribute('data-feather', 'menu');
                    if (window.feather) feather.replace();
                }
            }
        });

        // Close menu when clicking nav links
        navList.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', function() {
                navList.classList.remove('active');
                const icon = navToggle.querySelector('i');
                if (icon) {
                    icon.setAttribute('data-feather', 'menu');
                    if (window.feather) feather.replace();
                }
            });
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const headerHeight = document.querySelector('.site-header')?.offsetHeight || 0;
                const targetPosition = target.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Initialize code blocks with line numbers and copy buttons
    function initializeCodeBlocks() {
        // Add line numbers by wrapping each line in a span
        document.querySelectorAll('div.highlight pre code').forEach(code => {
            if (code.classList.contains('line-numbered')) return; // Already processed
            
            const lines = code.textContent.split('\n');
            const wrappedLines = lines.map(line => `<span class="line">${line}</span>`).join('\n');
            code.innerHTML = wrappedLines;
            code.classList.add('line-numbered');
        });
        
        addCopyButtons();
    }
    
    // Copy code functionality
    function addCopyButtons() {
        document.querySelectorAll('pre[class*="language-"]').forEach(pre => {
            if (pre.querySelector('.copy-code-btn')) return; // Already has button
            
            const button = document.createElement('button');
            button.className = 'copy-code-btn';
            button.innerHTML = '<i data-feather="copy"></i>';
            button.setAttribute('aria-label', 'Copy code');
            
            button.addEventListener('click', async function() {
                const code = pre.querySelector('code');
                if (!code) return;
                
                try {
                    await navigator.clipboard.writeText(code.textContent);
                    
                    // Visual feedback
                    button.innerHTML = '<i data-feather="check"></i>';
                    button.style.background = 'rgba(72, 187, 120, 0.3)';
                    if (window.feather) feather.replace();
                    
                    setTimeout(() => {
                        button.innerHTML = '<i data-feather="copy"></i>';
                        button.style.background = 'rgba(255, 255, 255, 0.1)';
                        if (window.feather) feather.replace();
                    }, 2000);
                } catch (err) {
                    console.log('Copy failed:', err);
                }
            });
            
            pre.appendChild(button);
        });
        
        if (window.feather) feather.replace();
    }

    // Initialize after Prism loads
    setTimeout(initializeCodeBlocks, 1000);
    
    // Also run after window load as backup
    window.addEventListener('load', initializeCodeBlocks);

    // Simple keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // ESC to close mobile menu
        if (e.key === 'Escape' && navList?.classList.contains('active')) {
            navList.classList.remove('active');
            const icon = navToggle?.querySelector('i');
            if (icon) {
                icon.setAttribute('data-feather', 'menu');
                if (window.feather) feather.replace();
            }
        }
    });

    console.log('🧠 CNS 2.0 Educational Blog - Navigation initialized');
});