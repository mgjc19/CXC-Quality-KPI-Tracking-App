document.addEventListener('DOMContentLoaded', function () {
    // Auto-dismiss flash messages
    document.querySelectorAll('.flash').forEach(function (el) {
        setTimeout(function () {
            el.style.transition = 'opacity 0.3s, transform 0.3s';
            el.style.opacity = '0';
            el.style.transform = 'translateY(-8px)';
            setTimeout(function () { el.remove(); }, 300);
        }, 5000);
    });

    // Auto-open Projects submenu if a project-related page is active
    var submenu = document.getElementById('projectsSubmenu');
    var chevron = document.getElementById('projectsChevron');
    if (submenu && submenu.querySelector('.sidebar-sublink.active')) {
        submenu.classList.add('open');
        if (chevron) chevron.classList.add('open');
    }
});

function toggleProjectsMenu() {
    var submenu = document.getElementById('projectsSubmenu');
    var chevron = document.getElementById('projectsChevron');
    submenu.classList.toggle('open');
    chevron.classList.toggle('open');
}
