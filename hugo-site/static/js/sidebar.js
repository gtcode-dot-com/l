document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('guide-sidebar-toggle');
    const sidebar = document.querySelector('.guide-sidebar');
    const overlay = document.getElementById('guide-sidebar-overlay');

    if (toggleButton && sidebar && overlay) {
        toggleButton.addEventListener('click', function () {
            sidebar.classList.toggle('is-open');
            overlay.classList.toggle('is-visible');
        });

        overlay.addEventListener('click', function () {
            sidebar.classList.remove('is-open');
            overlay.classList.remove('is-visible');
        });
    }

    // Also, make sure feather icons are replaced if they are added dynamically
    if (window.feather) {
        window.feather.replace();
    }
});
