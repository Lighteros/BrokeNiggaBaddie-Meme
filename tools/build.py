#!/usr/bin/env python3
"""Builds index.html for Broke Nigga Baddie ($BNB). Run from repo root: python3 tools/build.py"""
import html, json
X = "https://x.com/BrokeNiggaBadd"
SITE = "https://brokeniggabaddie.vip"
DISC = ("Parody meme only. Not affiliated with Binance, BNB Chain, CZ, or any Binance product. "
        "Not the Binance Coin. Not financial advice.")
MEMES = [
 ("meme-01","Checking the balance from a cardboard box. Still 0."),
 ("meme-02","The vault got opened. Not by her. Not for her."),
 ("meme-03","Closed for withdrawals. She waved anyway."),
 ("meme-04","City on fire, coffee in hand: funds are SAFU (whose?)."),
 ("meme-05","Neon night out with inside-out pockets."),
 ("meme-06","ATM said OUT OF ORDER. She said same."),
 ("meme-07","Sitting on bags that are emphatically not hers."),
 ("meme-08","Roadside sign, thumbs up, BROKE and proud."),
 ("meme-09","Ramen budget. Sticky-note portfolio."),
 ("meme-10","Upside-down shake test: zero coins fell out."),
 ("meme-11","Pawn shop run: one flip phone, one jar of coins."),
 ("meme-12","Zen mode: you can't lose what you never had."),
]
POSES = [
 ("pose-01","Hi. This is my wallet. It's a decorative item now."),
 ("pose-02","Pockets out. Lint is my only liquidity."),
 ("pose-03","Shopping bag? Empty. It's for the vibe."),
 ("pose-04","Arms crossed until withdrawals reopen."),
 ("pose-05","You. Yes you. Also broke? Thought so."),
 ("pose-06","Blowing a kiss to my last 3 cents."),
]
X_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.9 2H22l-6.8 7.8L23 22h-6.2l-4.8-6.3L6.4 22H3.3l7.3-8.3L1 2h6.3l4.4 5.8L18.9 2Zm-1.1 18h1.7L6.3 3.9H4.5L17.8 20Z"/></svg>'
e = html.escape

def tiles(items, folder, thumb):
    out=[]
    for i,(n,c) in enumerate(items,1):
        t = f"/img/{folder}/{n}{thumb}.webp"
        full = f"/img/{folder}/{n}.webp"
        out.append(f'<button class="tile rv" type="button" data-full="{full}" data-cap="{e(c)}" aria-label="Open {e(c)}">'
                   f'<img src="{t}" alt="{e(c)}" width="480" height="480" loading="lazy" decoding="async">'
                   f'<i class="no">{i:02d}</i><span>{e(c)}</span></button>')
    return "\n".join(out)

pose_btns = "\n".join(
  f'<button type="button" data-pose="{i}" aria-pressed="{"true" if i==0 else "false"}" aria-label="Pose {i+1}: {e(c)}">'
  f'<img src="/img/poses/{n}-t.webp" alt="" width="160" height="160" loading="lazy" decoding="async"></button>'
  for i,(n,c) in enumerate(POSES))

ld = {"@context":"https://schema.org","@type":"WebSite","name":"Broke Nigga Baddie ($BNB)","url":SITE+"/",
      "description":"Broke-girl parody meme coin. "+DISC,"sameAs":[X]}

TITLE = "Broke Nigga Baddie ($BNB) | Broke after the hot wallet got cooked · Parody meme"
DESC = ("Broke Nigga Baddie ($BNB): a broke-girl parody meme on Solana (planned). Empty pockets, duct-tape fit, SAFU irony. "
        "Not Binance, not BNB Chain. CA TBA.")
page = f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(TITLE)}</title>
<meta name="description" content="{e(DESC)}">
<meta name="theme-color" content="#F0B90B">
<link rel="canonical" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Broke Nigga Baddie">
<meta property="og:title" content="{e(TITLE)}">
<meta property="og:description" content="{e(DESC)}">
<meta property="og:url" content="{SITE}/">
<meta property="og:image" content="{SITE}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Broke Nigga Baddie pulling out her empty pockets on a Binance-yellow background (parody, not Binance)">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@BrokeNiggaBadd">
<meta name="twitter:title" content="{e(TITLE)}">
<meta name="twitter:description" content="{e(DESC)}">
<meta name="twitter:image" content="{SITE}/og.jpg">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/bungee-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/space-grotesk-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/img/poses/pose-02.webp" as="image" fetchpriority="high">
<link rel="stylesheet" href="/css/app.css?v=1">
<script type="application/ld+json">{json.dumps(ld)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<div class="strip" role="note" aria-label="Parody disclaimer">
  <div class="strip-track">
    {"".join(f'<span>{e(DISC)}</span>' for _ in range(4))}
  </div>
</div>

<header class="nav" data-nav>
  <div class="wrap">
    <a class="brand" href="#top" aria-label="Broke Nigga Baddie home"><img src="/img/logo.webp" alt="" width="42" height="42"><span>Broke Baddie<small>$BNB · parody</small></span></a>
    <ul class="nav-links" data-links>
      <li><a href="#lore">01 Who</a></li>
      <li><a href="#incident">02 Incident</a></li>
      <li><a href="#atm">03 ATM</a></li>
      <li><a href="#ledger">04 Ledger</a></li>
      <li><a href="#vault">05 Vault</a></li>
      <li><a href="#faq">06 FAQ</a></li>
    </ul>
    <div class="nav-cta">
      <a class="btn btn-sm" href="{X}" target="_blank" rel="noopener">{X_SVG}<span>X</span></a>
      <span class="btn btn-sm btn-soon" aria-disabled="true">Buy <em>SOON</em></span>
    </div>
    <button class="burger" type="button" data-burger aria-expanded="false" aria-label="Menu">MENU</button>
  </div>
</header>

<main id="main">
<!-- 1. HERO -->
<section class="hero" id="top">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="case label"><i></i> Case #BNB-000 · withdrawals paused</span>
      <h1><span class="l"><span class="tape">Broke</span></span><span class="l out">Nigga</span><span class="l">Baddie</span></h1>
      <p class="lede">Broke after the hot wallet got cooked. Pockets inside-out, duct tape holding the fit, baddie energy at a closed teller window.</p>
      <div class="ticker-row">
        <span class="ticker">$BNB</span>
        <div class="ca" data-ca><span class="label">CA</span><code>TBA</code><span class="tba">NOT LIVE</span></div>
      </div>
      <p class="ticker-warn">⚠ $BNB here = Broke Nigga Baddie. {e(DISC)}</p>
      <div class="cta-row">
        <span class="btn btn-soon" aria-disabled="true">Buy <em>SOON</em></span>
        <span class="btn btn-soon" aria-disabled="true">Chart <em>SOON</em></span>
        <a class="btn" href="{X}" target="_blank" rel="noopener">{X_SVG}<span>@BrokeNiggaBadd</span></a>
      </div>
      <p class="scam"><b>CA = TBA.</b> No contract exists yet. Any "$BNB Baddie" address you see before it is posted here <b>and</b> on @BrokeNiggaBadd is fake. We never DM first. There is no Telegram.</p>
    </div>

    <div class="stage" data-stage>
      <div class="frame">
      <span class="tape-x t1" aria-hidden="true"></span>
      <div class="window">
        <img data-pose-a src="/img/poses/pose-02.webp" alt="Broke Nigga Baddie, pockets pulled out" width="760" height="760" fetchpriority="high">
        <img data-pose-b class="off" src="/img/poses/pose-02.webp" alt="" width="760" height="760" aria-hidden="true">
        <div class="grille" aria-hidden="true"></div>
      </div>
      <div class="sign" aria-hidden="true">Teller 07<b>CLOSED</b>for withdrawals</div>
      <p class="bubble" data-bubble aria-live="polite">{e(POSES[1][1])}</p>
      </div>
      <div class="counter"><span>Pockets checked: <b data-pocketcount>0</b></span><span>Balance: $0.00</span></div>
      <div class="poses" role="group" aria-label="Swap poses">
{pose_btns}
      </div>
      <p class="hint">hover / tap a pose · she changes, the balance doesn't</p>
    </div>
  </div>
</section>

<!-- 2. MARQUEE -->
<div class="marquee" aria-hidden="true"><div class="row">
  {"".join('<span>WITHDRAWALS PAUSED</span><i>◆</i><span>FUNDS ARE SAFU (NOT YOURS)</span><i>◆</i><span>HOT WALLET: COOKED</span><i>◆</i><span>POCKETS: INSIDE-OUT</span><i>◆</i><span>PARODY · NOT BINANCE</span><i>◆</i>' for _ in range(2))}
</div></div>

<!-- 3. LORE / ABOUT -->
<section class="lore" id="lore" aria-labelledby="lore-h">
  <div class="wrap">
    <span class="label">01 / who is she</span>
    <h2 id="lore-h" class="rv">The yellow diamond stayed.<br>The money didn't.</h2>
    <div class="lore-grid">
      <figure class="polaroid rv">
        <span class="tape" aria-hidden="true"></span>
        <picture><source media="(max-width:700px)" srcset="/img/banner-sm.webp"><img src="/img/banner.webp" alt="Broke Nigga Baddie banner: she pulls out empty pockets at a trading desk" width="1600" height="533" loading="lazy" decoding="async"></picture>
        <figcaption>exhibit A · desk open, wallet closed</figcaption>
      </figure>
      <div>
        <ol class="lines rv">
          <li>She still wears the yellow diamond on a ripped crop top. Pockets inside-out. Duct tape holding the fit together.</li>
          <li>The hot wallet got emptied, withdrawals are on pause, and everyone keeps saying the funds are SAFU.</li>
          <li>Meanwhile she's waving an empty wallet at a closed teller window.</li>
          <li>No whitepaper. No affiliation. Just the girl, the yellow, and the joke that you're still broke.</li>
        </ol>
        <aside class="notice rv" aria-label="About disclaimer">
          <h3>⚠ About this meme</h3>
          <p>{e(DISC)}</p>
          <p>Broke Nigga Baddie / $BNB is a community joke coin about being broke after exchange chaos. No affiliation, endorsement, or partnership. Satire of hot-wallet hacks, withdrawal pauses and "funds are SAFU" vibes.</p>
        </aside>
      </div>
    </div>
  </div>
</section>

<!-- 4. INCIDENT REPORT -->
<section class="incident" id="incident" aria-labelledby="inc-h">
  <div class="wrap incident-head">
    <div><span class="label">02 / incident report</span><h2 id="inc-h" class="rv">How she got<br>this broke</h2></div>
    <p class="rv">A four-step post-mortem, filed by the victim herself. Root cause: vibes. Remediation: none.</p>
  </div>
  <div class="track" data-track>
    <article class="chap"><span class="stamp">03:12 AM</span><img src="/img/vault/meme-02-480.webp" alt="She sits inside a cracked-open empty vault" width="480" height="480" loading="lazy" decoding="async"><div class="body"><span class="label">step 01</span><h3>The hot wallet got cooked</h3><p>Somebody opened the vault. It wasn't her, and none of it was hers anyway. She moved in for the aesthetic.</p></div></article>
    <article class="chap"><span class="stamp">PAUSED</span><img src="/img/vault/meme-03-480.webp" alt="She waves at a teller window with a closed-for-withdrawals sign" width="480" height="480" loading="lazy" decoding="async"><div class="body"><span class="label">step 02</span><h3>"Withdrawals paused for maintenance"</h3><p>She showed up with a wallet and a smile. The window showed her a sign.</p></div></article>
    <article class="chap"><span class="stamp">SAFU?</span><img src="/img/vault/meme-04-480.webp" alt="She sips coffee calmly while the city burns behind her" width="480" height="480" loading="lazy" decoding="async"><div class="body"><span class="label">step 03</span><h3>Funds are SAFU (whose?)</h3><p>Everyone kept repeating it. The skyline was on fire. She refilled her coffee with exact change she didn't have.</p></div></article>
    <article class="chap final"><span class="stamp">STATUS: BROKE</span><img src="/img/vault/meme-08-480.webp" alt="She holds a BROKE cardboard sign and gives a thumbs up" width="480" height="480" loading="lazy" decoding="async"><div class="body"><span class="label">step 04</span><h3>Still broke. Still a baddie.</h3><p>Pockets confirm it. The sign confirms it. The thumbs up is non-negotiable.</p></div></article>
  </div>
</section>

<!-- 5. ATM TOY -->
<section class="atm-sec" id="atm" aria-labelledby="atm-h">
  <div class="wrap">
    <span class="label">03 / interactive · the baddie atm</span>
    <h2 id="atm-h" class="rv">Try to withdraw.<br>We dare you.</h2>
    <p class="intro rv">Press the buttons. She'll react, the receipt will print, and your balance will stay exactly where hers is.</p>
    <div class="atm">
      <div class="machine rv">
        <div class="machine-top">BADDIE ATM ◆ 0007 <span>● OUT OF FUNDS</span></div>
        <div class="screen">
          <div class="face" data-face><img data-face-img src="/img/poses/pose-01.webp" alt="Broke Nigga Baddie reacting" width="760" height="760" loading="lazy" decoding="async"></div>
          <div><div>AVAILABLE BALANCE</div><div class="bal" data-bal>$0.00</div><div class="msg" data-msg aria-live="polite">INSERT CARD. OR DON'T. SAME RESULT.</div></div>
        </div>
        <div class="keys">
          <button class="key" type="button" data-act="balance"><b>F1</b>Check balance</button>
          <button class="key" type="button" data-act="withdraw"><b>F2</b>Withdraw</button>
          <button class="key" type="button" data-act="shake"><b>F3</b>Shake pockets</button>
          <button class="key" type="button" data-act="safu"><b>F4</b>Ask if SAFU</button>
          <button class="key red" type="button" data-act="bailout"><b>F5</b>Request bailout</button>
          <button class="key" type="button" data-act="reset"><b>F6</b>New receipt</button>
        </div>
        <div class="slot" aria-hidden="true"></div>
      </div>
      <div class="receipt rv" aria-live="polite">
        <h3>BROKE BADDIE BANK<br>CUSTOMER COPY</h3>
        <ol data-receipt><li><span>SESSION OPENED</span><span>$0.00</span></li></ol>
        <div class="tot"><span>TOTAL WITHDRAWN</span><span data-total>$0.00</span></div>
        <div class="foot">pockets checked: <b data-pocketcount>0</b> · funds found: 0<br>parody receipt · not a real bank · not Binance</div>
      </div>
    </div>
  </div>
</section>

<!-- 6. LEDGER / HOW TO BUY -->
<section class="ledger" id="ledger" aria-labelledby="led-h">
  <div class="wrap">
    <span class="label">04 / balance sheet</span>
    <h2 id="led-h" class="rv">The ledger is<br>mostly blank</h2>
    <div class="ledger-grid">
      <div class="rv">
        <dl class="sheet">
          <div><dt>Ticker</dt><dd>$BNB<small>Broke Nigga Baddie · not Binance Coin</small></dd></div>
          <div><dt>Chain</dt><dd>Solana<small>planned</small></dd></div>
          <div><dt>Contract</dt><dd><span class="soon">TBA</span></dd></div>
          <div><dt>Supply / tax / LP</dt><dd><span class="soon">TBA</span><small>posted with the CA, not before</small></dd></div>
          <div><dt>Buy · Chart</dt><dd><span class="soon">SOON</span></dd></div>
          <div><dt>X</dt><dd><a href="{X}" target="_blank" rel="noopener">@BrokeNiggaBadd</a></dd></div>
          <div><dt>Telegram</dt><dd>None<small>there is no TG. a TG is a scam.</small></dd></div>
        </dl>
        <p class="ticker-warn">⚠ $BNB = Broke Nigga Baddie. {e(DISC)}</p>
      </div>
      <div class="rv">
        <ol class="steps">
          <li><b>Get a Solana wallet</b>Phantom, Solflare, Backpack — whatever you'll actually keep the seed phrase for.</li>
          <li><b>Fund it with SOL</b>From wherever still lets you withdraw.</li>
          <li class="locked"><b>Paste the official CA</b>CA is TBA. It will appear on this site and on @BrokeNiggaBadd at the same time.</li>
          <li class="locked"><b>Swap for $BNB</b>Buy link: Soon. Chart: Soon. Nothing to click yet, on purpose.</li>
        </ol>
        <p class="shield">ANTI-SCAM: Only trust a CA that appears on brokeniggabaddie.vip AND x.com/BrokeNiggaBadd. We never DM first. No Telegram exists. Nobody from here will ask for your seed phrase — you'd be broker than her.</p>
      </div>
    </div>
  </div>
</section>

<!-- 7. VAULT -->
<section class="vault" id="vault" aria-labelledby="v-h">
  <div class="wrap">
    <div class="vault-head">
      <div><span class="label">05 / meme vault</span><h2 id="v-h" class="rv">The only vault<br>that isn't empty</h2></div>
      <p class="rv">12 memes, live now. Tap to open, save, and post. <span class="count">12 MEMES · 6 POSES</span></p>
    </div>
    <div class="grid" data-gallery>
{tiles(MEMES,"vault","-480")}
    </div>
    <div class="posepack rv">
      <div class="posepack-head"><div><span class="label">featured</span><h3>The pose pack</h3></div><p class="mono">same girl, same fit, six ways to be broke. use as PFPs / reactions.</p></div>
      <div class="grid" data-gallery>
{tiles(POSES,"poses","-t")}
      </div>
    </div>
  </div>
</section>

<!-- 8. FAQ -->
<section class="faq" id="faq" aria-labelledby="f-h">
  <div class="wrap faq-grid">
    <div>
      <span class="label">06 / faq</span>
      <h2 id="f-h" class="rv">Questions from<br>the broke line</h2>
      <img class="sticker rv" src="/img/vault/meme-10-480.webp" alt="She hangs upside-down shaking an empty backpack" width="480" height="480" loading="lazy" decoding="async">
    </div>
    <div class="rv">
      <details open><summary>Is this Binance / BNB / BNB Chain?</summary><p>No. Broke Nigga Baddie ($BNB) is a parody meme. Not affiliated with Binance, BNB Chain, CZ, or any Binance product. Not the Binance Coin. Not financial advice.</p></details>
      <details><summary>What's the contract address?</summary><p>TBA. When it exists it will be posted here and on <a href="{X}" target="_blank" rel="noopener">@BrokeNiggaBadd</a>. Anything else is fake.</p></details>
      <details><summary>Where do I buy? Where's the chart?</summary><p>Soon. Both buttons go live when the CA does. Until then there is nothing to buy, so anyone selling you "$BNB Baddie" is selling air.</p></details>
      <details><summary>Is there a Telegram?</summary><p>No. There is no Telegram group. If someone invites you to one "for BNB Baddie," block them.</p></details>
      <details><summary>Will it go up?</summary><p>She can't even get her money out. No promises, no roadmap, no financial advice — just memes.</p></details>
      <details><summary>Can I use the memes?</summary><p>Yes. Everything in the vault is made to be posted. Tag @BrokeNiggaBadd.</p></details>
    </div>
  </div>
</section>
</main>

<!-- 9. FOOTER -->
<footer class="foot">
  <div class="wrap">
    <p class="foot-word">Broke <span>Nigga</span><br>Baddie</p>
    <div class="cta-row">
      <a class="btn" href="{X}" target="_blank" rel="noopener">{X_SVG}<span>Follow on X</span></a>
      <span class="btn btn-soon" aria-disabled="true">Buy <em>SOON</em></span>
      <span class="btn btn-soon" aria-disabled="true">Chart <em>SOON</em></span>
      <a class="btn btn-ghost" href="#top">Back to the window ↑</a>
    </div>
    <div class="disclaimer" role="note">
      <h3>⚠ Disclaimer — read this, it's the whole point</h3>
      <p><strong>{e(DISC)}</strong> Broke Nigga Baddie / $BNB is a community joke coin and satire of hot-wallet hacks, withdrawal pauses and "funds are SAFU" vibes. No affiliation, endorsement, or partnership with Binance or anyone else. Memecoins have no intrinsic value and can go to zero. CA: TBA. Only trust addresses posted on this site and x.com/BrokeNiggaBadd. No Telegram exists.</p>
    </div>
    <div class="legal"><span>© 2026 Broke Nigga Baddie · $BNB · Solana (planned)</span><span>brokeniggabaddie.vip · parody · not Binance</span></div>
  </div>
</footer>

<div class="lb" data-lb role="dialog" aria-modal="true" aria-label="Meme viewer">
  <button class="x" type="button" data-lb-close aria-label="Close">✕</button>
  <button class="nv prev" type="button" data-lb-prev aria-label="Previous">←</button>
  <figure><img data-lb-img src="data:," alt=""><figcaption><span data-lb-cap></span><a class="btn btn-sm" data-lb-dl href="#" download>Save meme</a></figcaption></figure>
  <button class="nv next" type="button" data-lb-next aria-label="Next">→</button>
</div>

<script src="/js/vendor/lenis.min.js" defer></script>
<script src="/js/vendor/gsap.min.js" defer></script>
<script src="/js/vendor/ScrollTrigger.min.js" defer></script>
<script src="/js/poses.js?v=1" defer></script>
<script src="/js/app.js?v=1" defer></script>
</body>
</html>
"""
open("index.html","w").write(page)
open("js/poses.js","w").write("window.BNB_POSES="+json.dumps([{"src":f"/img/poses/{n}.webp","line":c} for n,c in POSES])+";\n")
print("built index.html", len(page))
