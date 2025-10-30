document.addEventListener("DOMContentLoaded", function() {

    const sidebar = document.getElementById('sidebar');
    const closeBtn = document.getElementById('sidebar-close');
    const toggleBtns = document.querySelectorAll('#sidebar-toggle');

    if (sidebar && toggleBtns.length > 0) {
        toggleBtns.forEach(function(btn) {
            btn.addEventListener('click', function() {
                sidebar.classList.add('aberto');
            });
        });
    }

    if (sidebar && closeBtn) {
        closeBtn.addEventListener('click', function() {
            sidebar.classList.remove('aberto');
        });
    }

    const mainContent = document.getElementById('main-content');
    if (mainContent) {
        mainContent.addEventListener('click', function(event) {
            if (sidebar.classList.contains('aberto')) {
                if (!sidebar.contains(event.target)) {
                    sidebar.classList.remove('aberto');
                }
            }
        });
    }
});