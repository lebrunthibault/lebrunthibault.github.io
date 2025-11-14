document.addEventListener('DOMContentLoaded', function() {
  const menuButton = document.getElementById('mobile-menu-button');
  const mobileMenu = document.getElementById('mobile-menu');

  if (menuButton && mobileMenu) {
    menuButton.addEventListener('click', function() {
      const isExpanded = menuButton.getAttribute('aria-expanded') === 'true';
      menuButton.setAttribute('aria-expanded', !isExpanded);
      menuButton.setAttribute('aria-label', isExpanded ? 'Ouvrir le menu de navigation' : 'Fermer le menu de navigation');
      mobileMenu.classList.toggle('hidden');
      mobileMenu.classList.toggle('flex');
    });
  }
});
