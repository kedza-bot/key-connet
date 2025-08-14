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
});


// Toggle mobile profile dropdown
document.addEventListener("DOMContentLoaded", function () {
    const profileBtn = document.querySelector(".mobile-profile-btn");
    const profileHeader = document.querySelector(".mobile-profile-header");

    if (profileBtn) {
        profileBtn.addEventListener("click", function (e) {
            e.stopPropagation(); // Prevent click from bubbling
            profileHeader.classList.toggle("active");
        });

        // Close dropdown when clicking outside
        document.addEventListener("click", function (e) {
            if (!profileHeader.contains(e.target)) {
                profileHeader.classList.remove("active");
            }
        });
    }
});




// card function for the cards  
document.addEventListener('DOMContentLoaded', function(){
  const container = document.querySelector('.feature-cards');
  if (!container){
    console.warn('No .feature-cards found — check your HTML.');
    return;
  }

  const featuresSection = container.closest('.features');
  if (!featuresSection) {
    console.warn('No .features parent found.');
    return;
  }

  // Try to find existing buttons; if missing, create them
  let leftBtn = featuresSection.querySelector('.scroll-btn.left');
  let rightBtn = featuresSection.querySelector('.scroll-btn.right');

  function makeBtn(side){
    const b = document.createElement('button');
    b.className = `scroll-btn ${side}`;
    b.type = 'button';
    b.setAttribute('aria-label', side === 'left' ? 'Scroll left' : 'Scroll right');
    b.innerHTML = side === 'left' ? '&#10094;' : '&#10095;';
    return b;
  }

  if (!leftBtn) { leftBtn = makeBtn('left'); featuresSection.appendChild(leftBtn); }
  if (!rightBtn) { rightBtn = makeBtn('right'); featuresSection.appendChild(rightBtn); }

  // compute scroll amount = one card width + gap
  function getGapPx(){
    const computed = getComputedStyle(container).gap || getComputedStyle(document.documentElement).getPropertyValue('--gap');
    return parseFloat(computed) || 20;
  }

  function getCardScrollAmount(){
    const card = container.querySelector('.feture-card');
    if (!card) return container.clientWidth;
    const rect = card.getBoundingClientRect();
    return Math.round(rect.width + getGapPx());
  }

  let scrollAmount = getCardScrollAmount();

  // Scroll handlers
  leftBtn.addEventListener('click', () => {
    container.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
  });
  rightBtn.addEventListener('click', () => {
    container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
  });

  // toggle visibility / disabled state of buttons
  function toggleButtons(){
    const maxScrollLeft = container.scrollWidth - container.clientWidth;
    if (maxScrollLeft <= 5){
      leftBtn.style.display = 'none';
      rightBtn.style.display = 'none';
      return;
    } else {
      leftBtn.style.display = '';
      rightBtn.style.display = '';
    }
    leftBtn.disabled = container.scrollLeft <= 5;
    rightBtn.disabled = container.scrollLeft >= (maxScrollLeft - 5);
  }

  // update on scroll / resize
  container.addEventListener('scroll', () => requestAnimationFrame(toggleButtons));
  window.addEventListener('resize', () => {
    scrollAmount = getCardScrollAmount();
    requestAnimationFrame(toggleButtons);
  });

  // keyboard support for the scroller
  container.tabIndex = 0;
  container.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') { e.preventDefault(); container.scrollBy({ left: scrollAmount, behavior: 'smooth'}); }
    if (e.key === 'ArrowLeft')  { e.preventDefault(); container.scrollBy({ left: -scrollAmount, behavior: 'smooth'}); }
  });

  // initial setup
  scrollAmount = getCardScrollAmount();
  toggleButtons();
});




//big a screen testimonial slider
(function(){
  'use strict';
  document.addEventListener('DOMContentLoaded', function(){
    const sections = document.querySelectorAll('.testimonials');
    if (!sections.length) {
      console.warn('No .testimonials sections found.');
      return;
    }

    sections.forEach((section, idx) => {
      const container = section.querySelector('.testimonial-cards');
      if (!container) {
        console.warn(`.testimonials[#${idx}] has no .testimonial-cards`);
        return;
      }

      // find or create buttons
      let leftBtn  = section.querySelector('.testimonial-btn.left');
      let rightBtn = section.querySelector('.testimonial-btn.right');

      function makeBtn(side){
        const b = document.createElement('button');
        b.type = 'button';
        b.className = `testimonial-btn ${side}`;
        b.setAttribute('aria-label', side === 'left' ? 'Scroll left' : 'Scroll right');
        b.innerHTML = side === 'left' ? '&#10094;' : '&#10095;';
        return b;
      }
      if (!leftBtn)  { leftBtn  = makeBtn('left');  section.appendChild(leftBtn); }
      if (!rightBtn) { rightBtn = makeBtn('right'); section.appendChild(rightBtn); }

      // compute gap in px (fallback to 20)
      function getGapPx(){
        const cs = window.getComputedStyle(container);
        const gapVal = cs.getPropertyValue('gap') || cs.getPropertyValue('column-gap') || '20px';
        return parseFloat(gapVal) || 20;
      }

      // compute card width
      function getCardWidth(){
        const card = container.querySelector('.testimonial-card');
        if (!card) return Math.round(container.clientWidth * 0.9);
        return Math.round(card.getBoundingClientRect().width);
      }

      let scrollAmount = getCardWidth() + getGapPx();

      // click handlers
      leftBtn.addEventListener('click', () => {
        container.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
      });
      rightBtn.addEventListener('click', () => {
        container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
      });

      // toggle/hide if not scrollable
      function toggleButtons(){
        const maxScrollLeft = container.scrollWidth - container.clientWidth;
        if (maxScrollLeft <= 5) {
          leftBtn.style.display = 'none';
          rightBtn.style.display = 'none';
          return;
        } else {
          leftBtn.style.display = '';
          rightBtn.style.display = '';
        }
        leftBtn.disabled  = container.scrollLeft <= 5;
        rightBtn.disabled = container.scrollLeft >= (maxScrollLeft - 5);
      }

      // update on scroll/resize
      container.addEventListener('scroll', () => requestAnimationFrame(toggleButtons));
      window.addEventListener('resize', () => {
        scrollAmount = getCardWidth() + getGapPx();
        requestAnimationFrame(toggleButtons);
      });

      // keyboard support
      container.tabIndex = 0;
      container.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') { e.preventDefault(); container.scrollBy({ left: scrollAmount, behavior: 'smooth' }); }
        if (e.key === 'ArrowLeft')  { e.preventDefault(); container.scrollBy({ left: -scrollAmount, behavior: 'smooth' }); }
      });

      // initial setup
      scrollAmount = getCardWidth() + getGapPx();
      toggleButtons();
    });
  });
})();



//vedio hero section 
document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".hero-item");
  const previewContainer = document.querySelector(".video-previews");
  let currentIndex = 0;
  let slideInterval;

  // Create thumbnail previews
  slides.forEach((slide, index) => {
    const videoSrc = slide.querySelector("video source")?.src || slide.querySelector("video").src;
    const thumb = document.createElement("video");
    thumb.src = videoSrc;
    thumb.muted = true;
    thumb.loop = true;
    thumb.autoplay = true;
    if (index === 0) thumb.classList.add("active-thumb");
    thumb.addEventListener("click", () => showSlide(index));
    previewContainer.appendChild(thumb);
  });

  const thumbs = previewContainer.querySelectorAll("video");

  function showSlide(index) {
    slides[currentIndex].classList.remove("active");
    thumbs[currentIndex].classList.remove("active-thumb");

    currentIndex = index;

    slides[currentIndex].classList.add("active");
    thumbs[currentIndex].classList.add("active-thumb");

    resetInterval();
  }

  function nextSlide() {
    let nextIndex = (currentIndex + 1) % slides.length;
    showSlide(nextIndex);
  }

  function resetInterval() {
    clearInterval(slideInterval);
    slideInterval = setInterval(nextSlide, 7000); // 7 seconds per slide
  }

  resetInterval();
});