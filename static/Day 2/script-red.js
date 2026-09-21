// ==========================================================
// Mobile menu
// ==========================================================
(function mobileMenuSetup() {
  const btn = document.getElementById('menuBtn');
  const links = document.getElementById('navLinks');
  if (!btn || !links) return;

  btn.addEventListener('click', function () {
    const isOpen = links.classList.toggle('open');
    btn.classList.toggle('open', isOpen);
    btn.setAttribute('aria-expanded', String(isOpen));
  });

  links.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      links.classList.remove('open');
      btn.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    });
  });
})();

// ==========================================================
// Typing role text
// ==========================================================
(function typingSetup() {
  const el = document.getElementById('typingRole');
  if (!el) return;

  const phrases = ['Full Stack Developer', 'AI Enthusiast', 'Django Expert'];
  let phraseIndex = 0;
  let charIndex = 0;
  let deleting = false;

  function tick() {
    const current = phrases[phraseIndex];

    if (!deleting) {
      charIndex++;
      el.textContent = current.slice(0, charIndex);
      if (charIndex === current.length) {
        deleting = true;
        setTimeout(tick, 1400);
        return;
      }
    } else {
      charIndex--;
      el.textContent = current.slice(0, charIndex);
      if (charIndex === 0) {
        deleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
      }
    }

    setTimeout(tick, deleting ? 40 : 90);
  }

  tick();
})();

// ==========================================================
// Scroll reveal
// ==========================================================
(function revealSetup() {
  const sections = document.querySelectorAll('.fade-in');
  if (!sections.length) return;

  if (!('IntersectionObserver' in window)) {
    sections.forEach(function (s) { s.classList.add('visible'); });
    return;
  }

  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  sections.forEach(function (s) { observer.observe(s); });
})();

// ==========================================================
// Contact form
// ==========================================================
(function formSetup() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const name = document.getElementById('nameInput').value;
    const email = document.getElementById('emailInput').value;

    if (!name || !email) {
      alert('Please fill in all fields!');
      return;
    }

    alert('Thanks ' + name + '! Your message has been sent (check the console).');
    console.log('Form submitted:', { name: name, email: email });
    form.reset();
  });
})();

// ==========================================================
// Active nav link on scroll
// ==========================================================
(function activeNavSetup() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  if (!sections.length || !navLinks.length) return;

  window.addEventListener('scroll', function () {
    let current = '';
    sections.forEach(function (section) {
      const top = section.offsetTop - 140;
      if (window.scrollY >= top) current = section.id;
    });

    navLinks.forEach(function (link) {
      link.classList.toggle('active-link', link.getAttribute('href') === '#' + current);
    });
  });
})();
