/* Broke Nigga Baddie ($BNB) — interactions. Parody meme, not Binance. */
(() => {
  const d = document, $ = (s, r = d) => r.querySelector(s), $$ = (s, r = d) => [...r.querySelectorAll(s)];
  d.documentElement.classList.remove('no-js');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const POSES = window.BNB_POSES || [];

  /* smooth scroll (Lenis) + GSAP ticker */
  let lenis = null;
  if (!reduce && window.Lenis) {
    lenis = new Lenis({ lerp: 0.11, smoothWheel: true });
    if (window.gsap && window.ScrollTrigger) {
      gsap.registerPlugin(ScrollTrigger);
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(t => lenis.raf(t * 1000)); gsap.ticker.lagSmoothing(0);
    } else { const raf = t => { lenis.raf(t); requestAnimationFrame(raf); }; requestAnimationFrame(raf); }
  }
  const offset = () => -(parseInt(getComputedStyle(d.documentElement).getPropertyValue('--strip-h')) + 64);
  $$('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
    const id = a.getAttribute('href'); const t = id.length > 1 && $(id); if (!t) return;
    e.preventDefault(); nav.classList.remove('open'); burger.setAttribute('aria-expanded', 'false');
    lenis ? lenis.scrollTo(t, { offset: offset() }) : t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
  }));

  /* nav */
  const nav = $('[data-nav]'), burger = $('[data-burger]');
  burger.addEventListener('click', () => { const o = nav.classList.toggle('open'); burger.setAttribute('aria-expanded', o); });
  const onScroll = () => nav.classList.toggle('scrolled', scrollY > 30);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* reveals */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  $$('.rv').forEach(el => io.observe(el));

  /* pocket counter (shared hero + atm) */
  let pockets = 0;
  const bumpPockets = () => { pockets++; $$('[data-pocketcount]').forEach(n => n.textContent = pockets); };

  /* hero pose swap: crossfade two layers */
  const stage = $('[data-stage]'), A = $('[data-pose-a]'), B = $('[data-pose-b]'), bubble = $('[data-bubble]');
  let front = A, back = B, cur = 1;
  POSES.forEach(p => { const i = new Image(); i.src = p.src; });
  function setPose(i) {
    if (i === cur || !POSES[i]) return; cur = i;
    back.src = POSES[i].src; back.alt = 'Broke Nigga Baddie pose ' + (i + 1);
    back.classList.remove('off'); back.removeAttribute('aria-hidden');
    front.classList.add('off'); front.setAttribute('aria-hidden', 'true');
    [front, back] = [back, front];
    bubble.textContent = POSES[i].line; bubble.classList.remove('pop'); void bubble.offsetWidth; bubble.classList.add('pop');
    $$('.poses button').forEach((b, j) => b.setAttribute('aria-pressed', j === i));
    bumpPockets();
  }
  $$('.poses button').forEach(b => {
    const i = +b.dataset.pose;
    b.addEventListener('mouseenter', () => setPose(i));
    b.addEventListener('focus', () => setPose(i));
    b.addEventListener('click', () => setPose(i));
  });
  // set initial pressed to pose index 1 (pose-02 is the hero)
  $$('.poses button').forEach((b, j) => b.setAttribute('aria-pressed', j === 1));
  // idle: grille slams shut every so often (closed for withdrawals)
  if (!reduce) setInterval(() => { stage.classList.add('closed'); setTimeout(() => stage.classList.remove('closed'), 1300); }, 7000);
  // tilt on pointer
  if (!reduce && matchMedia('(pointer:fine)').matches) {
    const w = $('.window', stage);
    stage.addEventListener('pointermove', e => { const r = stage.getBoundingClientRect(); const x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; w.style.transform = `perspective(900px) rotateY(${x * 6}deg) rotateX(${-y * 6}deg)`; });
    stage.addEventListener('pointerleave', () => w.style.transform = '');
  }

  /* ATM toy */
  const faceBox = $('[data-face]'), face = $('[data-face-img]'), bal = $('[data-bal]'), msg = $('[data-msg]'),
        rec = $('[data-receipt]'), total = $('[data-total]');
  let balance = 0, fees = 0;
  const money = v => (v < 0 ? '-$' : '$') + Math.abs(v).toFixed(2);
  const pick = a => a[Math.floor(Math.random() * a.length)];
  const LINES = {
    balance: { pose: 4, fee: 0, out: ['BALANCE: $0.00. SAME AS 5 SECONDS AGO.', 'YOU HAVE $0.00 AND A GREAT ATTITUDE.', 'BALANCE LOADING… STILL $0.00.'] },
    withdraw: { pose: 0, fee: -0.69, out: ['WITHDRAWALS PAUSED. FEE CHARGED ANYWAY.', 'INSUFFICIENT FUNDS. SUFFICIENT FEES.', 'REQUEST QUEUED BEHIND 4,000,000 OTHERS.'] },
    shake: { pose: 1, fee: 0, out: ['FOUND: 1 LINT, 1 RECEIPT, 0 COINS.', 'POCKETS SHAKEN. NOTHING FELL OUT.', 'FOUND A GUM WRAPPER. NOT LIQUID.'] },
    safu: { pose: 3, fee: 0, out: ['FUNDS ARE SAFU. (NOT YOURS.)', 'SAFU STATUS: SAFU-ISH. TRY AGAIN SUNDAY.', 'SAFU FUND: EXISTS. FOR SOMEONE.'] },
    bailout: { pose: 5, fee: -0.01, out: ['BAILOUT DENIED. HERE IS A KISS.', 'BAILOUT APPROVED FOR: NOT YOU.', 'SENT TO MANAGER. MANAGER IS ALSO BROKE.'] },
  };
  const LABEL = { balance: 'BALANCE CHECK', withdraw: 'WITHDRAW ATTEMPT', shake: 'POCKET SHAKE', safu: 'SAFU INQUIRY', bailout: 'BAILOUT REQUEST' };
  function print(label, amt) {
    const li = d.createElement('li'); li.className = 'new';
    li.innerHTML = `<span></span><span>${money(amt)}</span>`; li.firstChild.textContent = label;
    rec.appendChild(li); rec.parentElement.scrollTop = rec.parentElement.scrollHeight;
  }
  function lint(btn) {
    if (reduce) return;
    const r = btn.getBoundingClientRect();
    ['lint', '0.00', 'IOU', 'lint', '¢?'].forEach((t, i) => {
      const s = d.createElement('span'); s.className = 'lint'; s.textContent = t;
      s.style.left = (r.left + r.width / 2) + 'px'; s.style.top = (r.top) + 'px'; d.body.appendChild(s);
      const dx = (Math.random() - .5) * 260, dy = -80 - Math.random() * 140;
      s.animate([{ transform: 'translate(0,0) rotate(0)', opacity: 1 }, { transform: `translate(${dx}px,${dy}px) rotate(${dx / 2}deg)`, opacity: 1, offset: .55 }, { transform: `translate(${dx * 1.3}px,${dy + 220}px) rotate(${dx}deg)`, opacity: 0 }], { duration: 1100 + i * 90, easing: 'cubic-bezier(.2,.7,.4,1)' }).onfinish = () => s.remove();
    });
  }
  $$('[data-act]').forEach(btn => btn.addEventListener('click', () => {
    const act = btn.dataset.act;
    if (act === 'reset') { rec.innerHTML = '<li><span>SESSION OPENED</span><span>$0.00</span></li>'; balance = 0; fees = 0; bal.textContent = '$0.00'; bal.classList.remove('neg'); total.textContent = '$0.00'; msg.textContent = 'NEW RECEIPT. SAME BALANCE.'; return; }
    const L = LINES[act]; fees += L.fee; balance = +(0 + fees).toFixed(2);
    if (POSES[L.pose]) face.src = POSES[L.pose].src;
    faceBox.classList.remove('shake'); void faceBox.offsetWidth; faceBox.classList.add('shake');
    msg.textContent = pick(L.out); bal.textContent = money(balance); bal.classList.toggle('neg', balance < 0);
    print(LABEL[act], L.fee); total.textContent = '$0.00';
    if (act === 'shake' || act === 'withdraw') lint(btn);
    bumpPockets();
  }));

  /* lightbox */
  const lb = $('[data-lb]'), lbImg = $('[data-lb-img]'), lbCap = $('[data-lb-cap]'), lbDl = $('[data-lb-dl]');
  let set = [], idx = 0, lastFocus = null;
  function show(i) { idx = (i + set.length) % set.length; const t = set[idx]; lbImg.src = t.dataset.full; lbImg.alt = t.dataset.cap; lbCap.textContent = t.dataset.cap; lbDl.href = t.dataset.full; lbDl.setAttribute('download', t.dataset.full.split('/').pop()); }
  $$('[data-gallery]').forEach(g => $$('.tile', g).forEach((t, i) => t.addEventListener('click', () => { set = $$('.tile', g); lastFocus = t; show(i); lb.classList.add('on'); lenis && lenis.stop(); $('[data-lb-close]').focus(); })));
  const close = () => { lb.classList.remove('on'); lenis && lenis.start(); lastFocus && lastFocus.focus(); };
  $('[data-lb-close]').addEventListener('click', close);
  $('[data-lb-prev]').addEventListener('click', () => show(idx - 1));
  $('[data-lb-next]').addEventListener('click', () => show(idx + 1));
  lb.addEventListener('click', e => { if (e.target === lb) close(); });
  addEventListener('keydown', e => { if (!lb.classList.contains('on')) return; if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(idx - 1); if (e.key === 'ArrowRight') show(idx + 1); });

  /* GSAP: pinned horizontal incident report (desktop) + hero entrance */
  if (!reduce && window.gsap && window.ScrollTrigger) {
    gsap.from('.hero h1 .l', { yPercent: 60, opacity: 0, rotate: -3, stagger: .09, duration: .8, ease: 'back.out(1.6)' });
    gsap.from('.stage', { y: 40, opacity: 0, rotate: 3, duration: .9, delay: .15, ease: 'power3.out' });
    const mm = gsap.matchMedia();
    mm.add('(min-width: 761px)', () => {
      const track = $('[data-track]');
      const dist = () => Math.max(0, track.scrollWidth - innerWidth);
      gsap.to(track, { x: () => -dist(), ease: 'none', scrollTrigger: { trigger: '#incident', start: 'top top', end: () => '+=' + dist(), pin: true, scrub: .6, invalidateOnRefresh: true } });
    });
    gsap.to('.marquee', { rotate: 1.2, scrollTrigger: { trigger: '.marquee', start: 'top bottom', end: 'bottom top', scrub: true } });
    addEventListener('load', () => ScrollTrigger.refresh());
  }
})();
