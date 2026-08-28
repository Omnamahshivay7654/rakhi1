/* ==========================================================================
   PREMIUM INDIAN FESTIVE RAKSHA BANDHAN - MASTER JAVASCRIPT ENGINE
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initAudioEngine();
  initBackgroundCanvas();
  initNavigation();

  // Page Specific Inits based on DOM elements
  initPage1Greeting();
  initPage2RakhiStudio();
  initPage3AartiStudio();
  initPage4SweetsStudio();
  initPage5GiftStudio();
});

/* ==========================================================================
   1. AUDIO ENGINE & SOUND SYNTHESIZER
   ========================================================================== */
let audioCtx = null;
let bgAudio = null;
let isMusicPlaying = false;

function initAudioEngine() {
  bgAudio = document.getElementById('bgAudio');
  const playBtn = document.getElementById('playToggleBtn');
  const volumeSlider = document.getElementById('volumeSlider');
  const musicDisc = document.getElementById('musicDisc');

  // Auto-init Web Audio Context on first click/touch anywhere
  const unlockAudio = () => {
    if (!audioCtx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) audioCtx = new AudioContextClass();
    }
    if (bgAudio && bgAudio.paused && !isMusicPlaying) {
      bgAudio.play().then(() => {
        isMusicPlaying = true;
        updateMusicUI(true);
      }).catch(e => console.log('Autoplay deferred until user action:', e));
    }
    document.removeEventListener('click', unlockAudio);
    document.removeEventListener('touchstart', unlockAudio);
  };
  document.addEventListener('click', unlockAudio);
  document.addEventListener('touchstart', unlockAudio);

  if (playBtn && bgAudio) {
    playBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (!audioCtx) {
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (AudioContextClass) audioCtx = new AudioContextClass();
      }
      if (bgAudio.paused) {
        bgAudio.play();
        isMusicPlaying = true;
        updateMusicUI(true);
        playSynthesizedSound('sparkle');
      } else {
        bgAudio.pause();
        isMusicPlaying = false;
        updateMusicUI(false);
      }
    });
  }

  if (volumeSlider && bgAudio) {
    volumeSlider.addEventListener('input', (e) => {
      bgAudio.volume = e.target.value;
    });
  }
}

function updateMusicUI(playing) {
  const playBtn = document.getElementById('playToggleBtn');
  const musicDisc = document.getElementById('musicDisc');
  if (playBtn) playBtn.innerHTML = playing ? '⏸' : '▶';
  if (musicDisc) {
    if (playing) musicDisc.classList.add('playing');
    else musicDisc.classList.remove('playing');
  }
}

// Web Audio API Synthesizer for rich dynamic sound effects
function playSynthesizedSound(type) {
  if (!audioCtx) return;
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }

  const now = audioCtx.currentTime;
  const masterGain = audioCtx.createGain();
  masterGain.connect(audioCtx.destination);

  if (type === 'click') {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(800, now);
    osc.frequency.exponentialRampToValueAtTime(400, now + 0.08);
    gain.gain.setValueAtTime(0.3, now);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.08);
    osc.connect(gain);
    gain.connect(masterGain);
    osc.start(now);
    osc.stop(now + 0.08);
  } else if (type === 'bell') {
    const freqs = [1200, 2400, 3600];
    freqs.forEach((f, i) => {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(f, now);
      const vol = 0.3 / (i + 1);
      gain.gain.setValueAtTime(vol, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 1.8);
      osc.connect(gain);
      gain.connect(masterGain);
      osc.start(now);
      osc.stop(now + 1.8);
    });
  } else if (type === 'sparkle') {
    const notes = [523.25, 659.25, 783.99, 1046.50, 1318.51];
    notes.forEach((freq, idx) => {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, now + idx * 0.06);
      gain.gain.setValueAtTime(0.2, now + idx * 0.06);
      gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.06 + 0.3);
      osc.connect(gain);
      gain.connect(masterGain);
      osc.start(now + idx * 0.06);
      osc.stop(now + idx * 0.06 + 0.3);
    });
  } else if (type === 'sweetPop') {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(300, now);
    osc.frequency.exponentialRampToValueAtTime(900, now + 0.12);
    gain.gain.setValueAtTime(0.4, now);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12);
    osc.connect(gain);
    gain.connect(masterGain);
    osc.start(now);
    osc.stop(now + 0.12);
  } else if (type === 'fanfare') {
    const chords = [523.25, 659.25, 783.99, 1046.50];
    chords.forEach(freq => {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, now);
      gain.gain.setValueAtTime(0.25, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 1.2);
      osc.connect(gain);
      gain.connect(masterGain);
      osc.start(now);
      osc.stop(now + 1.2);
    });
  }
}

/* ==========================================================================
   2. FLOATING BACKGROUND CANVAS PARTICLES (Petals, Sparkles, Diyas, Hearts)
   ========================================================================== */
function initBackgroundCanvas() {
  const canvas = document.getElementById('bgCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width = canvas.width = window.innerWidth;
  let height = canvas.height = window.innerHeight;

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  const particles = [];
  const particleCount = 45;

  const types = ['petal', 'sparkle', 'heart', 'diya'];

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      size: 6 + Math.random() * 12,
      speedY: 0.5 + Math.random() * 1.2,
      speedX: Math.sin(Math.random() * Math.PI) * 0.8,
      rotation: Math.random() * 360,
      rotSpeed: (Math.random() - 0.5) * 2,
      type: types[Math.floor(Math.random() * types.length)],
      opacity: 0.4 + Math.random() * 0.5
    });
  }

  function render() {
    ctx.clearRect(0, 0, width, height);

    particles.forEach(p => {
      p.y -= p.speedY;
      p.x += p.speedX;
      p.rotation += p.rotSpeed;

      if (p.y < -30) {
        p.y = height + 30;
        p.x = Math.random() * width;
      }

      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate((p.rotation * Math.PI) / 180);
      ctx.globalAlpha = p.opacity;

      if (p.type === 'petal') {
        ctx.fillStyle = '#E85D75';
        ctx.beginPath();
        ctx.ellipse(0, 0, p.size, p.size / 2, 0, 0, Math.PI * 2);
        ctx.fill();
      } else if (p.type === 'sparkle') {
        ctx.fillStyle = '#FFD700';
        ctx.beginPath();
        ctx.arc(0, 0, p.size / 3, 0, Math.PI * 2);
        ctx.fill();
      } else if (p.type === 'heart') {
        ctx.fillStyle = '#FF4D6D';
        ctx.beginPath();
        const s = p.size / 2;
        ctx.moveTo(0, s / 2);
        ctx.bezierCurveTo(-s, -s / 2, -s, -s, 0, -s * 1.2);
        ctx.bezierCurveTo(s, -s, s, -s / 2, 0, s / 2);
        ctx.fill();
      } else if (p.type === 'diya') {
        ctx.fillStyle = '#FF9933';
        ctx.beginPath();
        ctx.arc(0, 0, p.size / 2, 0, Math.PI);
        ctx.fill();
        ctx.fillStyle = '#FFD700';
        ctx.beginPath();
        ctx.arc(0, -p.size / 4, p.size / 4, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.restore();
    });

    requestAnimationFrame(render);
  }

  render();
}

/* ==========================================================================
   3. NAVIGATION LOGIC & ACTIVE HIGHLIGHT
   ========================================================================== */
function initNavigation() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  const hamburger = document.getElementById('hamburgerBtn');
  const mobileMenu = document.getElementById('mobileMenu');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.toggle('active');
      playSynthesizedSound('click');
    });
  }

  // Add click sound to all buttons
  document.querySelectorAll('button, .btn-festive, .btn-secondary, .page-step-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      playSynthesizedSound('click');
    });
  });
}

/* ==========================================================================
   4. PAGE 1 — GREETING & ENVELOPE SURPRISE
   ========================================================================== */
function initPage1Greeting() {
  const openWishBtn = document.getElementById('openWishBtn');
  const wishModal = document.getElementById('wishModalOverlay');
  const closeWishBtn = document.getElementById('closeWishBtn');

  if (openWishBtn && wishModal) {
    openWishBtn.addEventListener('click', () => {
      wishModal.classList.add('active');
      playSynthesizedSound('sparkle');
      spawnConfetti();
    });
  }

  if (closeWishBtn && wishModal) {
    closeWishBtn.addEventListener('click', () => {
      wishModal.classList.remove('active');
    });
  }
}

/* Confetti Burst Generator */
function spawnConfetti() {
  const colors = ['#FFD700', '#FF9933', '#E85D75', '#FFFDD0', '#8B0000'];
  for (let i = 0; i < 60; i++) {
    const conf = document.createElement('div');
    conf.style.position = 'fixed';
    conf.style.left = '50vw';
    conf.style.top = '50vh';
    conf.style.width = (6 + Math.random() * 8) + 'px';
    conf.style.height = (6 + Math.random() * 8) + 'px';
    conf.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    conf.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
    conf.style.zIndex = '2500';
    conf.style.pointerEvents = 'none';
    
    const angle = Math.random() * Math.PI * 2;
    const velocity = 150 + Math.random() * 300;
    const tx = Math.cos(angle) * velocity;
    const ty = Math.sin(angle) * velocity;

    document.body.appendChild(conf);

    conf.animate([
      { transform: 'translate(0, 0) scale(1)', opacity: 1 },
      { transform: `translate(${tx}px, ${ty}px) scale(0)`, opacity: 0 }
    ], {
      duration: 1200 + Math.random() * 600,
      easing: 'cubic-bezier(0.165, 0.84, 0.44, 1)',
      fill: 'forwards'
    });

    setTimeout(() => conf.remove(), 2000);
  }
}

/* ==========================================================================
   5. PAGE 2 — RAKHI SELECTION STUDIO & TYING
   ========================================================================== */
function initPage2RakhiStudio() {
  const rakhiCards = document.querySelectorAll('.rakhi-card');
  const selectedRakhiImg = document.getElementById('selectedRakhiImg');
  const selectedRakhiTitle = document.getElementById('selectedRakhiTitle');
  const tieRakhiBtn = document.getElementById('tieRakhiBtn');
  const tyingRakhiObj = document.getElementById('tyingRakhiObj');
  const tieSuccessMsg = document.getElementById('tieSuccessMsg');

  let selectedRakhiSrc = 'rakhi-1.svg';
  let selectedRakhiName = 'Royal Gold Rakhi';

  rakhiCards.forEach(card => {
    card.addEventListener('click', () => {
      rakhiCards.forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');

      selectedRakhiSrc = card.getAttribute('data-img');
      selectedRakhiName = card.getAttribute('data-title');

      if (selectedRakhiImg) selectedRakhiImg.src = selectedRakhiSrc;
      if (selectedRakhiTitle) selectedRakhiTitle.innerText = selectedRakhiName;
      if (tyingRakhiObj) tyingRakhiObj.src = selectedRakhiSrc;

      playSynthesizedSound('sparkle');
    });
  });

  if (tieRakhiBtn && tyingRakhiObj) {
    tieRakhiBtn.addEventListener('click', () => {
      playSynthesizedSound('sparkle');
      tyingRakhiObj.classList.add('tied');

      setTimeout(() => {
        playSynthesizedSound('bell');
        spawnConfetti();
        if (tieSuccessMsg) tieSuccessMsg.style.display = 'block';
      }, 1000);
    });
  }
}

/* ==========================================================================
   6. PAGE 3 — ROTATING AARTI THALI STUDIO
   ========================================================================== */
function initPage3AartiStudio() {
  const thaliWrapper = document.getElementById('aartiThaliWrapper');
  const btnPause = document.getElementById('btnPauseAarti');
  const btnResume = document.getElementById('btnResumeAarti');
  const btnSlow = document.getElementById('btnSlowAarti');
  const btnFast = document.getElementById('btnFastAarti');
  const btnStartAarti = document.getElementById('startAartiBtn');
  const blessingBanner = document.getElementById('aartiBlessingBanner');

  if (!thaliWrapper) return;

  // Speed & Pause controls
  if (btnPause) {
    btnPause.addEventListener('click', () => {
      thaliWrapper.style.animationPlayState = 'paused';
      playSynthesizedSound('click');
    });
  }
  if (btnResume) {
    btnResume.addEventListener('click', () => {
      thaliWrapper.style.animationPlayState = 'running';
      playSynthesizedSound('click');
    });
  }
  if (btnSlow) {
    btnSlow.addEventListener('click', () => {
      thaliWrapper.className = 'aarti-thali-wrapper orbiting speed-slow';
      playSynthesizedSound('click');
    });
  }
  if (btnFast) {
    btnFast.addEventListener('click', () => {
      thaliWrapper.className = 'aarti-thali-wrapper orbiting speed-fast';
      playSynthesizedSound('click');
    });
  }

  // Interactive Diya Click Boost
  thaliWrapper.addEventListener('click', () => {
    playSynthesizedSound('bell');
    spawnConfetti();
    thaliWrapper.style.filter = 'drop-shadow(0 0 45px #FFD700)';
    setTimeout(() => {
      thaliWrapper.style.filter = 'none';
    }, 1500);
  });

  // Start Aarti Ceremony Button
  if (btnStartAarti) {
    btnStartAarti.addEventListener('click', () => {
      playSynthesizedSound('bell');
      spawnConfetti();
      thaliWrapper.className = 'aarti-thali-wrapper orbiting speed-fast';
      if (blessingBanner) blessingBanner.style.display = 'block';
    });
  }
}

/* ==========================================================================
   7. PAGE 4 — MITHAI TIME & FLY-TO-PLATE PHYSICS
   ========================================================================== */
function initPage4SweetsStudio() {
  const addButtons = document.querySelectorAll('.add-sweet-btn');
  const plate = document.getElementById('decorativePlate');
  const sweetsCountBadge = document.getElementById('sweetsCountBadge');
  const clearPlateBtn = document.getElementById('clearPlateBtn');
  const celebrateMithaiBtn = document.getElementById('celebrateMithaiBtn');

  let count = 0;

  addButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const sweetCard = btn.closest('.sweet-card');
      const img = sweetCard.querySelector('img');
      const imgSrc = img.src;

      playSynthesizedSound('sweetPop');

      // Create Flying Clone Animation
      const flyingImg = document.createElement('img');
      flyingImg.src = imgSrc;
      flyingImg.className = 'flying-sweet';

      const rect = img.getBoundingClientRect();
      const plateRect = plate.getBoundingClientRect();

      flyingImg.style.left = rect.left + 'px';
      flyingImg.style.top = rect.top + 'px';

      document.body.appendChild(flyingImg);

      requestAnimationFrame(() => {
        flyingImg.style.left = (plateRect.left + plateRect.width / 2 - 40) + 'px';
        flyingImg.style.top = (plateRect.top + plateRect.height / 2 - 40) + 'px';
        flyingImg.style.transform = 'scale(0.6) rotate(360deg)';
        flyingImg.style.opacity = '0.5';
      });

      setTimeout(() => {
        flyingImg.remove();

        // Append real item inside decorative plate
        const item = document.createElement('img');
        item.src = imgSrc;
        item.className = 'plate-sweet-item';
        item.title = 'Click to remove';

        item.addEventListener('click', () => {
          item.remove();
          count = Math.max(0, count - 1);
          if (sweetsCountBadge) sweetsCountBadge.innerText = `Sweets Added: ${count} 🍬`;
          playSynthesizedSound('click');
        });

        if (plate) plate.appendChild(item);
        count++;
        if (sweetsCountBadge) sweetsCountBadge.innerText = `Sweets Added: ${count} 🍬`;
      }, 800);
    });
  });

  if (clearPlateBtn && plate) {
    clearPlateBtn.addEventListener('click', () => {
      plate.innerHTML = '';
      count = 0;
      if (sweetsCountBadge) sweetsCountBadge.innerText = `Sweets Added: 0 🍬`;
      playSynthesizedSound('click');
    });
  }

  if (celebrateMithaiBtn) {
    celebrateMithaiBtn.addEventListener('click', () => {
      playSynthesizedSound('fanfare');
      spawnConfetti();
      alert('🍬 Happy Raksha Bandhan! Enjoy the sweet celebration! 🎉');
    });
  }
}

/* ==========================================================================
   8. PAGE 5 — FUNNY GIFT DEMAND & UNBOXING
   ========================================================================== */
function initPage5GiftStudio() {
  const giftCards = document.querySelectorAll('.gift-card');
  const openGiftBtn = document.getElementById('openGiftBtn');
  const giftBoxWrapper = document.getElementById('giftBoxWrapper');
  const revealedGiftDisplay = document.getElementById('revealedGiftDisplay');
  const revealedGiftImg = document.getElementById('revealedGiftImg');
  const revealedGiftTitle = document.getElementById('revealedGiftTitle');

  let selectedGiftSrc = 'phone.svg';
  let selectedGiftName = 'New Phone 📱';

  giftCards.forEach(card => {
    card.addEventListener('click', () => {
      giftCards.forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');

      selectedGiftSrc = card.getAttribute('data-img');
      selectedGiftName = card.getAttribute('data-title');

      playSynthesizedSound('sparkle');
    });
  });

  if (openGiftBtn && giftBoxWrapper) {
    openGiftBtn.addEventListener('click', () => {
      playSynthesizedSound('sparkle');
      giftBoxWrapper.classList.add('shake');

      setTimeout(() => {
        giftBoxWrapper.classList.remove('shake');
        giftBoxWrapper.style.display = 'none';

        if (revealedGiftImg) revealedGiftImg.src = selectedGiftSrc;
        if (revealedGiftTitle) revealedGiftTitle.innerText = selectedGiftName;
        if (revealedGiftDisplay) revealedGiftDisplay.style.display = 'block';

        playSynthesizedSound('fanfare');
        spawnConfetti();
      }, 1500);
    });
  }
}
