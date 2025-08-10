document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.querySelector('.hamburger-menu');
  const mobileDropdown = document.querySelector('.mobile-dropdown');
  const mobileProfileBtn = document.querySelector('.mobile-profile-btn');
  const mobileProfileDropdown = document.querySelector('.mobile-profile-dropdown');

  // Toggle mobile dropdown menu
  if (hamburger && mobileDropdown) {
    hamburger.addEventListener('click', () => {
      mobileDropdown.classList.toggle('active');

      const expanded = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', !expanded);
      mobileDropdown.setAttribute('aria-hidden', expanded);
    });
  }

  // Toggle mobile profile dropdown
  if (mobileProfileBtn && mobileProfileDropdown) {
    mobileProfileBtn.addEventListener('click', () => {
      mobileProfileDropdown.classList.toggle('active');
    });
  }
});
