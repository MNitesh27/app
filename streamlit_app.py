import streamlit as st

st.set_page_config(
    page_title="Shiksha · शिक्षा",
    page_icon="🪔",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Google+Sans+Display:wght@400;700&family=Noto+Sans+Devanagari:wght@400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,700;1,400&family=DM+Serif+Display:ital@0;1&family=Noto+Sans+Devanagari:wght@400;600&display=swap');

/* ── Design tokens ── */
:root {
    --orange:      #E8621A;
    --orange-soft: #F47B3A;
    --orange-pale: #FFF3EC;
    --marigold:    #F5A623;
    --saffron:     #E8732A;
    --white:       #FFFFFF;
    --off-white:   #F8F9FA;
    --surface:     #F0F0F0;
    --ink:         #202124;
    --ink-mid:     #5F6368;
    --ink-light:   #9AA0A6;
    --border:      #E8EAED;
    --card-radius: 24px;
    --pill-radius: 999px;
}

/* ── Reset ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background: var(--white);
    color: var(--ink);
    -webkit-font-smoothing: antialiased;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ════════════════════════════════
   ANIMATIONS
════════════════════════════════ */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(32px); }
    to   { opacity: 1; transform: translateY(0);    }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-12px); }
}
@keyframes shimmer-text {
    0%   { background-position: -300% center; }
    100% { background-position:  300% center; }
}
@keyframes ticker {
    0%   { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
@keyframes spin-slow {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}
@keyframes pulse-dot {
    0%, 100% { transform: scale(1);   opacity: 1; }
    50%       { transform: scale(1.4); opacity: 0.6; }
}
@keyframes card-in {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0);    }
}

/* ════════════════════════════════
   TOP NAV BAR  (Google Store style: white, thin, sticky)
════════════════════════════════ */
.topnav {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 48px;
    height: 64px;
}
.topnav-brand {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    color: var(--ink);
    letter-spacing: -0.5px;
}
.topnav-brand span {
    color: var(--orange);
}
.topnav-deva {
    font-family: 'Noto Sans Devanagari', sans-serif;
    font-size: 13px;
    color: var(--ink-light);
    margin-left: 8px;
    font-weight: 400;
}
.topnav-cta {
    background: var(--orange);
    color: white;
    border-radius: var(--pill-radius);
    padding: 10px 24px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 14px;
    text-decoration: none;
    transition: background .2s, box-shadow .2s, transform .15s;
    display: inline-block;
}
.topnav-cta:hover {
    background: var(--orange-soft);
    box-shadow: 0 4px 16px rgba(232,98,26,0.3);
    transform: translateY(-1px);
}

/* ════════════════════════════════
   FESTIVAL TICKER
════════════════════════════════ */
.ticker-outer {
    background: var(--orange);
    overflow: hidden;
    padding: 9px 0;
}
.ticker-inner {
    display: flex;
    width: max-content;
    animation: ticker 28s linear infinite;
}
.ticker-track {
    display: flex;
    gap: 0;
    white-space: nowrap;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 13px;
    letter-spacing: .5px;
    color: white;
}
.ticker-sep { margin: 0 20px; opacity: 0.5; }

/* ════════════════════════════════
   HERO  (Google Store: full bleed, big type, pale bg)
════════════════════════════════ */
.hero {
    background: var(--off-white);
    min-height: 520px;
    display: flex;
    align-items: center;
    padding: 80px 80px 80px 80px;
    position: relative;
    overflow: hidden;
}
.hero-text { max-width: 580px; z-index: 2; position: relative; }
.hero-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 13px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--orange);
    margin-bottom: 20px;
    animation: fadeUp .7s ease both;
    display: flex;
    align-items: center;
    gap: 8px;
}
.hero-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--orange);
    display: inline-block;
    animation: pulse-dot 2s ease-in-out infinite;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(48px, 6vw, 80px);
    line-height: 1.05;
    color: var(--ink);
    margin: 0 0 8px;
    letter-spacing: -1.5px;
    animation: fadeUp .7s ease .1s both;
}
.hero-title-accent {
    background: linear-gradient(90deg, var(--orange), var(--marigold), var(--saffron), var(--orange));
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer-text 4s linear infinite;
    font-style: italic;
}
.hero-deva {
    font-family: 'Noto Sans Devanagari', sans-serif;
    font-size: 20px;
    color: var(--ink-light);
    margin-bottom: 24px;
    animation: fadeUp .7s ease .2s both;
}
.hero-sub {
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    font-size: 19px;
    line-height: 1.65;
    color: var(--ink-mid);
    max-width: 480px;
    margin-bottom: 40px;
    animation: fadeUp .7s ease .3s both;
}
.hero-actions {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    animation: fadeUp .7s ease .4s both;
}
.btn-primary {
    background: var(--orange);
    color: white;
    border-radius: var(--pill-radius);
    padding: 15px 32px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 15px;
    text-decoration: none;
    display: inline-block;
    transition: background .2s, box-shadow .2s, transform .15s;
}
.btn-primary:hover {
    background: var(--orange-soft);
    box-shadow: 0 6px 20px rgba(232,98,26,0.35);
    transform: translateY(-2px);
}
.btn-ghost {
    background: transparent;
    color: var(--orange);
    border: 1.5px solid var(--orange);
    border-radius: var(--pill-radius);
    padding: 14px 32px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 15px;
    text-decoration: none;
    display: inline-block;
    transition: background .2s, transform .15s;
}
.btn-ghost:hover {
    background: var(--orange-pale);
    transform: translateY(-2px);
}

/* Hero visual — right side */
.hero-visual {
    position: absolute;
    right: 0; top: 0; bottom: 0;
    width: 45%;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none;
}
.hero-circle-bg {
    width: 420px; height: 420px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--orange-pale) 0%, #FFE5CC 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}
.hero-emoji-main {
    font-size: 110px;
    animation: float 3.5s ease-in-out infinite;
    filter: drop-shadow(0 20px 40px rgba(232,98,26,0.2));
    display: block;
}
.hero-emoji-orbit {
    position: absolute;
    font-size: 36px;
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
}
.orbit-1 { top: 40px;  left: 50px;  animation: float 2.8s ease-in-out .3s infinite; }
.orbit-2 { top: 60px;  right: 45px; animation: float 3.2s ease-in-out .8s infinite; }
.orbit-3 { bottom: 60px; left: 40px; animation: float 3.0s ease-in-out .5s infinite; }
.orbit-4 { bottom: 50px; right: 50px; animation: float 2.6s ease-in-out 1.0s infinite; }

/* Rangoli watermark */
.rangoli-bg {
    position: absolute;
    opacity: 0.06;
    width: 300px; height: 300px;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    animation: spin-slow 60s linear infinite;
}

/* ════════════════════════════════
   STATS BAR  (Google Store: clean white strip with numbers)
════════════════════════════════ */
.stats-bar {
    background: var(--white);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: center;
    gap: 0;
    padding: 0;
}
.stat-item {
    flex: 1;
    max-width: 240px;
    text-align: center;
    padding: 36px 24px;
    border-right: 1px solid var(--border);
}
.stat-item:last-child { border-right: none; }
.stat-val {
    font-family: 'DM Serif Display', serif;
    font-size: 44px;
    color: var(--orange);
    line-height: 1;
    margin-bottom: 8px;
}
.stat-label {
    font-family: 'DM Sans', sans-serif;
    font-weight: 400;
    font-size: 13px;
    color: var(--ink-mid);
    letter-spacing: .3px;
}

/* ════════════════════════════════
   TABS  (Google Store: minimal, underline only)
════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: var(--white);
    padding: 0 48px;
    gap: 0;
    border-bottom: 1px solid var(--border);
}
.stTabs [data-baseweb="tab"] {
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 14px;
    color: var(--ink-mid) !important;
    padding: 20px 22px;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    background: transparent !important;
    transition: color .2s;
    letter-spacing: .1px;
}
.stTabs [data-baseweb="tab"]:hover { color: var(--ink) !important; }
.stTabs [aria-selected="true"] {
    color: var(--orange) !important;
    border-bottom: 2px solid var(--orange) !important;
}
.stTabs [data-baseweb="tab-panel"] { padding: 0 !important; background: var(--white); }

/* ════════════════════════════════
   PAGE SECTIONS
════════════════════════════════ */
.page-section {
    max-width: 1080px;
    margin: 0 auto;
    padding: 72px 48px;
}
.page-section-full {
    padding: 72px 48px;
}

/* Section label + heading */
.s-label {
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--orange);
    margin-bottom: 12px;
}
.s-heading {
    font-family: 'DM Serif Display', serif;
    font-size: 40px;
    color: var(--ink);
    margin: 0 0 8px;
    line-height: 1.15;
    letter-spacing: -0.5px;
}
.s-heading em { font-style: italic; color: var(--orange); }
.s-body {
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    font-size: 17px;
    line-height: 1.8;
    color: var(--ink-mid);
    max-width: 640px;
}

/* ════════════════════════════════
   SUBJECT CARDS  (Google Store product cards)
════════════════════════════════ */
.subjects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 16px;
    margin-top: 40px;
}
.subject-card {
    background: var(--off-white);
    border-radius: var(--card-radius);
    padding: 32px 20px 28px;
    text-align: center;
    cursor: default;
    transition: background .25s, transform .25s cubic-bezier(.34,1.56,.64,1), box-shadow .25s;
    animation: card-in .5s ease both;
    border: 1.5px solid transparent;
}
.subject-card:hover {
    background: var(--orange-pale);
    border-color: rgba(232,98,26,0.2);
    transform: translateY(-6px);
    box-shadow: 0 12px 32px rgba(232,98,26,0.12);
}
.subject-card:hover .subject-icon { transform: scale(1.15); }
.subject-icon {
    font-size: 40px;
    margin-bottom: 14px;
    display: block;
    transition: transform .25s cubic-bezier(.34,1.56,.64,1);
}
.subject-name {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 14px;
    color: var(--ink);
    margin-bottom: 6px;
}
.subject-desc {
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    font-size: 12px;
    color: var(--ink-mid);
    line-height: 1.5;
}

/* ════════════════════════════════
   FULL-BLEED FEATURE BLOCK
   (Google Store: alternating image + text panels)
════════════════════════════════ */
.feature-block {
    background: var(--off-white);
    padding: 72px 80px;
    display: flex;
    align-items: center;
    gap: 72px;
}
.feature-block.flipped { flex-direction: row-reverse; background: var(--white); }
.feature-text { flex: 1; }
.feature-visual {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
}
.feature-emoji-wrap {
    width: 280px; height: 280px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--orange-pale), #FFD9BB);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 90px;
    animation: float 4s ease-in-out infinite;
    box-shadow: 0 20px 60px rgba(232,98,26,0.15);
}
.feature-emoji-square {
    width: 280px; height: 280px;
    border-radius: 32px;
    background: var(--orange-pale);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 80px;
    box-shadow: 0 16px 48px rgba(232,98,26,0.12);
}

/* ════════════════════════════════
   QUOTE BLOCK
════════════════════════════════ */
.quote-wrap {
    background: var(--orange);
    border-radius: var(--card-radius);
    padding: 40px 48px;
    margin: 40px 0;
    position: relative;
    overflow: hidden;
}
.quote-wrap::before {
    content: '\201C';
    position: absolute;
    right: 32px; top: -16px;
    font-size: 120px;
    font-family: 'DM Serif Display', serif;
    color: rgba(255,255,255,0.12);
    line-height: 1;
}
.quote-hindi {
    font-family: 'Noto Sans Devanagari', sans-serif;
    font-size: 24px;
    color: white;
    margin-bottom: 10px;
    font-weight: 600;
}
.quote-en {
    font-family: 'DM Serif Display', serif;
    font-style: italic;
    font-size: 16px;
    color: rgba(255,255,255,0.75);
}

/* ════════════════════════════════
   AUDIENCE CARDS
════════════════════════════════ */
.aud-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 40px;
}
.aud-card {
    background: var(--off-white);
    border-radius: var(--card-radius);
    padding: 32px;
    border: 1.5px solid var(--border);
    transition: border-color .2s, transform .2s, box-shadow .2s;
    cursor: default;
}
.aud-card:hover {
    border-color: var(--orange);
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(232,98,26,0.10);
}
.aud-emoji { font-size: 32px; margin-bottom: 14px; display: block; }
.aud-title {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
    color: var(--ink);
    margin-bottom: 10px;
}
.aud-body {
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    font-size: 15px;
    color: var(--ink-mid);
    line-height: 1.7;
}

/* ════════════════════════════════
   PILLS
════════════════════════════════ */
.pill-row { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 24px; }
.pill {
    background: var(--orange-pale);
    color: var(--orange);
    border: 1.5px solid rgba(232,98,26,0.25);
    border-radius: var(--pill-radius);
    padding: 8px 18px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 13px;
    cursor: default;
    transition: background .2s, transform .15s;
}
.pill:hover { background: #FFE0CC; transform: scale(1.04); }

/* ════════════════════════════════
   INFO CARDS (Practical)
════════════════════════════════ */
.info-card {
    background: var(--off-white);
    border-radius: var(--card-radius);
    padding: 36px;
    border: 1.5px solid var(--border);
    margin-bottom: 20px;
    transition: border-color .2s, transform .2s, box-shadow .2s;
}
.info-card:hover {
    border-color: rgba(232,98,26,0.4);
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(232,98,26,0.08);
}
.info-card h3 {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
    color: var(--ink);
    margin: 0 0 14px;
}
.info-card p, .info-card li {
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    font-size: 15px;
    color: var(--ink-mid);
    line-height: 1.75;
}
.info-card ul { padding-left: 18px; }
.info-card strong { color: var(--ink); font-weight: 500; }

/* ════════════════════════════════
   CTA BANNER (Google Store: orange full-bleed)
════════════════════════════════ */
.cta-banner {
    background: linear-gradient(135deg, var(--orange) 0%, var(--marigold) 100%);
    padding: 72px 80px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.cta-banner::before {
    content: 'शिक्षा';
    position: absolute;
    font-family: 'Noto Sans Devanagari', sans-serif;
    font-size: 200px;
    color: rgba(255,255,255,0.06);
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    white-space: nowrap;
    pointer-events: none;
}
.cta-banner-title {
    font-family: 'DM Serif Display', serif;
    font-size: 40px;
    color: white;
    margin-bottom: 14px;
    position: relative;
}
.cta-banner-sub {
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    font-size: 18px;
    color: rgba(255,255,255,0.85);
    margin-bottom: 36px;
    position: relative;
}
.btn-white {
    background: white;
    color: var(--orange);
    border-radius: var(--pill-radius);
    padding: 15px 36px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 15px;
    text-decoration: none;
    display: inline-block;
    transition: box-shadow .2s, transform .15s;
    position: relative;
}
.btn-white:hover {
    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    transform: translateY(-2px);
}

/* ════════════════════════════════
   DIVIDER
════════════════════════════════ */
.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 0;
}

/* ════════════════════════════════
   FOOTER
════════════════════════════════ */
.site-footer {
    background: var(--ink);
    padding: 40px 80px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
}
.footer-brand {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
    color: white;
}
.footer-brand span { color: var(--orange); font-style: italic; }
.footer-copy {
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    font-size: 13px;
    color: rgba(255,255,255,0.4);
}
.footer-diyas { font-size: 20px; letter-spacing: 6px; }
</style>
""", unsafe_allow_html=True)

# ── Top Nav ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topnav">
  <div>
    <span class="topnav-brand">Shi<span>ksha</span> <span style="font-family:'Noto Sans Devanagari',sans-serif;font-size:18px;color:var(--orange);">शिक्षा</span></span>
  </div>
  <a class="topnav-cta" href="#">Get in touch</a>
</div>
""", unsafe_allow_html=True)

# ── Festival ticker ───────────────────────────────────────────────────────────
st.markdown("""
<div class="ticker-outer">
  <div class="ticker-inner">
    <div class="ticker-track">
      <span>🪔 Diwali</span><span class="ticker-sep">·</span>
      <span>🌈 Holi</span><span class="ticker-sep">·</span>
      <span>🌙 Eid Mubarak</span><span class="ticker-sep">·</span>
      <span>🌸 Navratri</span><span class="ticker-sep">·</span>
      <span>🥁 Baisakhi</span><span class="ticker-sep">·</span>
      <span>🪁 Makar Sankranti</span><span class="ticker-sep">·</span>
      <span>🐘 Ganesh Chaturthi</span><span class="ticker-sep">·</span>
      <span>🌺 Pongal</span><span class="ticker-sep">·</span>
      <span>🎋 Onam</span><span class="ticker-sep">·</span>
      <span>🎊 Raksha Bandhan</span><span class="ticker-sep">·</span>
      <span>🎵 Janmashtami</span><span class="ticker-sep">·</span>
      <span>🪔 Diwali</span><span class="ticker-sep">·</span>
      <span>🌈 Holi</span><span class="ticker-sep">·</span>
      <span>🌙 Eid Mubarak</span><span class="ticker-sep">·</span>
      <span>🌸 Navratri</span><span class="ticker-sep">·</span>
      <span>🥁 Baisakhi</span><span class="ticker-sep">·</span>
      <span>🪁 Makar Sankranti</span><span class="ticker-sep">·</span>
      <span>🐘 Ganesh Chaturthi</span><span class="ticker-sep">·</span>
      <span>🌺 Pongal</span><span class="ticker-sep">·</span>
      <span>🎋 Onam</span><span class="ticker-sep">·</span>
      <span>🎊 Raksha Bandhan</span><span class="ticker-sep">·</span>
      <span>🎵 Janmashtami</span><span class="ticker-sep">·</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-text">
    <div class="hero-eyebrow">
      <span class="hero-dot"></span>
      Cultural tutorship for children
    </div>
    <div class="hero-title">
      Learn India.<br>
      <span class="hero-title-accent">Love the story.</span>
    </div>
    <div class="hero-deva">शिक्षा — Education</div>
    <div class="hero-sub">
      A warm, personal journey into Indian culture — language, festivals,
      food, traditions &amp; stories — for children and families wherever they are.
    </div>
    <div class="hero-actions">
      <a class="btn-primary" href="#">Start your journey</a>
      <a class="btn-ghost" href="#">Learn more</a>
    </div>
  </div>

  <div class="hero-visual">
    <div class="hero-circle-bg">
      <svg class="rangoli-bg" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <circle cx="100" cy="100" r="95" stroke="#E8621A" stroke-width="2" fill="none"/>
        <circle cx="100" cy="100" r="70" stroke="#F5A623" stroke-width="1.5" fill="none"/>
        <circle cx="100" cy="100" r="45" stroke="#E8621A" stroke-width="2" fill="none"/>
        <ellipse cx="100" cy="12" rx="9" ry="20" fill="#E8621A" fill-opacity="0.6"/>
        <ellipse cx="100" cy="188" rx="9" ry="20" fill="#E8621A" fill-opacity="0.6"/>
        <ellipse cx="12" cy="100" rx="20" ry="9" fill="#E8621A" fill-opacity="0.6"/>
        <ellipse cx="188" cy="100" rx="20" ry="9" fill="#E8621A" fill-opacity="0.6"/>
        <ellipse cx="40" cy="40" rx="9" ry="20" transform="rotate(45 40 40)" fill="#F5A623" fill-opacity="0.5"/>
        <ellipse cx="160" cy="40" rx="9" ry="20" transform="rotate(-45 160 40)" fill="#F5A623" fill-opacity="0.5"/>
        <ellipse cx="40" cy="160" rx="9" ry="20" transform="rotate(-45 40 160)" fill="#F5A623" fill-opacity="0.5"/>
        <ellipse cx="160" cy="160" rx="9" ry="20" transform="rotate(45 160 160)" fill="#F5A623" fill-opacity="0.5"/>
        <circle cx="100" cy="100" r="12" fill="#E8621A" fill-opacity="0.7"/>
      </svg>
      <span class="hero-emoji-main">🪔</span>
      <span class="hero-emoji-orbit orbit-1">🎉</span>
      <span class="hero-emoji-orbit orbit-2">🍛</span>
      <span class="hero-emoji-orbit orbit-3">🗣️</span>
      <span class="hero-emoji-orbit orbit-4">🎨</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Stats bar ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-bar">
  <div class="stat-item"><div class="stat-val">22+</div><div class="stat-label">Official languages in India</div></div>
  <div class="stat-item"><div class="stat-val">40+</div><div class="stat-label">Festivals celebrated yearly</div></div>
  <div class="stat-item"><div class="stat-val">5000</div><div class="stat-label">Years of living history</div></div>
  <div class="stat-item"><div class="stat-val">6</div><div class="stat-label">Major religions &amp; traditions</div></div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tabs = st.tabs(["Home", "About Shiksha", "About the Author", "For Who", "Practical Information"])

# ════════════════════════════════════════════════════════════════════════════
# HOME
# ════════════════════════════════════════════════════════════════════════════
with tabs[0]:
    # What we explore
    st.markdown("""
    <div class="page-section">
      <div class="s-label">What we explore</div>
      <div class="s-heading">Six windows into <em>India</em></div>
      <div class="s-body" style="margin-top:12px;">
        From the alphabet to the spice rack — each subject is a doorway into something
        rich and alive. Children pick favourites, follow their curiosity, and build
        a genuine connection to Indian culture.
      </div>
      <div class="subjects-grid">
        <div class="subject-card" style="animation-delay:.05s"><span class="subject-icon">🗣️</span><div class="subject-name">Hindi</div><div class="subject-desc">Words, Devanagari script &amp; simple conversation</div></div>
        <div class="subject-card" style="animation-delay:.10s"><span class="subject-icon">🎉</span><div class="subject-name">Festivals</div><div class="subject-desc">Diwali, Holi, Eid, Navratri &amp; more</div></div>
        <div class="subject-card" style="animation-delay:.15s"><span class="subject-icon">🏺</span><div class="subject-name">Traditions</div><div class="subject-desc">Rituals, customs &amp; their deeper meaning</div></div>
        <div class="subject-card" style="animation-delay:.20s"><span class="subject-icon">🙏</span><div class="subject-name">Religion</div><div class="subject-desc">Stories &amp; values from India's great faiths</div></div>
        <div class="subject-card" style="animation-delay:.25s"><span class="subject-icon">🍛</span><div class="subject-name">Cuisine</div><div class="subject-desc">Flavours, spices &amp; the stories food carries</div></div>
        <div class="subject-card" style="animation-delay:.30s"><span class="subject-icon">🎨</span><div class="subject-name">Arts &amp; Crafts</div><div class="subject-desc">Rangoli, mehendi, music &amp; dance</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

    # Feature block 1
    st.markdown("""
    <div class="feature-block">
      <div class="feature-text">
        <div class="s-label">A little corner of India</div>
        <div class="s-heading">Not a classroom.<br><em>A gathering.</em></div>
        <div class="s-body" style="margin-top:16px;">
          Whether your family grew up lighting diyas at Diwali, or you're discovering
          the beauty of India's traditions for the very first time — Shiksha is here for you.
          <br/><br/>
          A place where children can hear a Hindi story, taste the name of a spice,
          and understand <em>why</em> we celebrate the way we do. Learning happens
          when it feels like belonging.
        </div>
      </div>
      <div class="feature-visual">
        <div class="feature-emoji-wrap">🏡</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Feature block 2
    st.markdown("""
    <div class="feature-block flipped">
      <div class="feature-text">
        <div class="s-label">Why Shiksha?</div>
        <div class="s-heading">Culture isn't just <em>history</em></div>
        <div class="s-body" style="margin-top:16px;">
          For many families raising children outside India, it can feel hard to know
          where to start. How do you pass on something as vast as Indian heritage
          in a way that feels alive, not like homework?
          <br/><br/>
          Shiksha starts small: one festival, one dish, one word at a time.
          The goal is to spark curiosity — and give children a sense of pride
          in where they come from, or where they belong.
        </div>
      </div>
      <div class="feature-visual">
        <div class="feature-emoji-square">✨</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # CTA banner
    st.markdown("""
    <div class="cta-banner">
      <div class="cta-banner-title">Ready to start the conversation?</div>
      <div class="cta-banner-sub">First introductory session is always free. No commitment needed.</div>
      <a class="btn-white" href="#">Get in touch ✉️</a>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# ABOUT SHIKSHA
# ════════════════════════════════════════════════════════════════════════════
with tabs[1]:
    st.markdown("""
    <div class="page-section">
      <div class="s-label">The project</div>
      <div class="s-heading">What is <em>Shiksha</em>?</div>
      <div class="s-body" style="margin-top:16px;">
        Shiksha (शिक्षा) is the Sanskrit and Hindi word for <em>education</em>.
        It felt like the right name for a project that believes learning about
        culture is one of the most profound gifts we can give a child.
        <br/><br/>
        This is a small, personal tutorship — not a school, not a business.
        A series of gentle sessions where children aged 5 to 14 can explore
        Indian culture through stories, activities, cooking, crafts, and language.
      </div>

      <div class="quote-wrap" style="margin-top:48px;">
        <div class="quote-hindi">पढ़ना लिखना सीखो, ओ मेहनत करने वालों।</div>
        <div class="quote-en">"Learn to read and write, O hardworking ones." — folk saying</div>
      </div>

      <div class="s-label" style="margin-top:56px;">The subjects</div>
      <div class="s-heading">Six threads of <em>one rich fabric</em></div>
      <div class="subjects-grid" style="margin-top:32px;">
        <div class="subject-card" style="animation-delay:.05s"><span class="subject-icon">🗣️</span><div class="subject-name">Hindi Language</div><div class="subject-desc">Devanagari script, vocabulary, songs &amp; conversation</div></div>
        <div class="subject-card" style="animation-delay:.10s"><span class="subject-icon">🎊</span><div class="subject-name">Festivals</div><div class="subject-desc">The calendar &amp; the stories behind each celebration</div></div>
        <div class="subject-card" style="animation-delay:.15s"><span class="subject-icon">🙏</span><div class="subject-name">Religions</div><div class="subject-desc">Hinduism, Islam, Sikhism, Buddhism &amp; Jainism</div></div>
        <div class="subject-card" style="animation-delay:.20s"><span class="subject-icon">🏺</span><div class="subject-name">Traditions</div><div class="subject-desc">Weddings, seasons &amp; daily rituals</div></div>
        <div class="subject-card" style="animation-delay:.25s"><span class="subject-icon">🍛</span><div class="subject-name">Cuisine</div><div class="subject-desc">Spices, regional dishes &amp; food stories</div></div>
        <div class="subject-card" style="animation-delay:.30s"><span class="subject-icon">🎨</span><div class="subject-name">Arts &amp; Crafts</div><div class="subject-desc">Rangoli, mehendi, music &amp; classical dance</div></div>
      </div>

      <div class="s-body" style="margin-top:48px;">
        Sessions are designed to be <strong style="color:var(--ink);">hands-on and playful</strong>.
        A lesson about Diwali might end with making a paper diya. A Hindi session might begin
        with learning family member names through a silly game. The goal is for children to
        leave each session with something they want to share at home.
      </div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# ABOUT AUTHOR
# ════════════════════════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown("""
    <div class="feature-block" style="background:var(--off-white);">
      <div class="feature-text">
        <div class="s-label">The person behind Shiksha</div>
        <div class="s-heading">A little bit <em>about me</em></div>
        <div class="s-body" style="margin-top:16px;">
          Hello! I'm [Your Name] — and I started Shiksha because I kept asking myself:
          <em>how do we pass this on?</em>
          <br/><br/>
          I grew up surrounded by the sounds of Hindi film songs in the kitchen,
          the smell of incense on festival mornings, and the wonderful chaos of a
          joint family. Somewhere along the way, I realised how precious those
          memories were — and how easy it is for them to quietly fade when children
          grow up far from their extended families or from India itself.
          <br/><br/>
          I'm not a professional teacher. I'm someone who loves Indian culture deeply,
          speaks Hindi, has cooked dal from scratch more times than I can count,
          and believes children learn best when they're having fun.
        </div>
      </div>
      <div class="feature-visual">
        <div class="feature-emoji-wrap">🌸</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="page-section">
      <div class="quote-wrap">
        <div class="quote-hindi">संस्कृति वो है जो हम अगली पीढ़ी को देते हैं।</div>
        <div class="quote-en">"Culture is what we pass on to the next generation."</div>
      </div>

      <div class="s-label" style="margin-top:48px;">A little more about me</div>
      <div class="pill-row">
        <span class="pill">🇮🇳 Grew up in [City], India</span>
        <span class="pill">🌍 Living in [Country] since [Year]</span>
        <span class="pill">📚 Background in [Your Field]</span>
        <span class="pill">🍳 Amateur cook of Indian food</span>
        <span class="pill">🎵 Bollywood classics fan</span>
        <span class="pill">🌸 Storyteller at heart</span>
      </div>

      <div class="s-body" style="margin-top:48px;">
        I started these sessions with my own children's friends, and I was amazed
        at how curious kids are — how they want to understand, not just memorise.
        A child asking <em>"but why do we burst crackers?"</em> is more exciting
        to me than any exam result.
        <br/><br/>
        Shiksha is small by design. I see small groups, I take my time,
        and I get to know each child's curiosity. If you'd like to meet
        over a cup of chai before signing up — I'd love that. ☕
      </div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# FOR WHO
# ════════════════════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown("""
    <div class="page-section">
      <div class="s-label">Who is this for?</div>
      <div class="s-heading">For curious children <em>everywhere</em></div>
      <div class="s-body" style="margin-top:12px;">
        Shiksha was designed with a few families in mind — chances are,
        you'll recognise yourself in one of them.
      </div>

      <div class="aud-grid">
        <div class="aud-card">
          <span class="aud-emoji">🏡</span>
          <div class="aud-title">Families of Indian heritage living abroad</div>
          <div class="aud-body">Your children were born here, but you want them to understand where your family comes from — the language your parents spoke, the festivals you grew up celebrating. Shiksha is a gentle bridge between two worlds.</div>
        </div>
        <div class="aud-card">
          <span class="aud-emoji">🌍</span>
          <div class="aud-title">Mixed-heritage &amp; multicultural families</div>
          <div class="aud-body">One parent is Indian, one is not — or your family has woven together multiple cultures. Indian culture is one colourful thread in your child's identity, and Shiksha helps them hold it with pride.</div>
        </div>
        <div class="aud-card">
          <span class="aud-emoji">✨</span>
          <div class="aud-title">Families new to Indian culture</div>
          <div class="aud-body">You have Indian friends, neighbours, or colleagues. Or perhaps your child is curious after learning about Diwali at school. You don't need to be Indian to appreciate the richness of this culture — everyone is welcome.</div>
        </div>
        <div class="aud-card">
          <span class="aud-emoji">👧</span>
          <div class="aud-title">Children aged 5 to 14</div>
          <div class="aud-body">Younger children (5–8) love stories, songs and crafts. Older children (9–14) go deeper into language, history and meaning. No prior knowledge needed — just an open mind and a healthy appetite 🍛.</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-block" style="background:var(--off-white);">
      <div class="feature-text">
        <div class="s-label">What parents can expect</div>
        <div class="s-heading">Something to <em>take home</em></div>
        <div class="s-body" style="margin-top:16px;">
          After each session, your child will come home with something:
          a word, a story, a small craft, a question to ask you.
          <br/><br/>
          Sessions are never heavy. There are no grades, no pressure.
          I want children to leave feeling like they've been part of something warm —
          like visiting a family friend's home where something delicious was always on the stove.
        </div>
      </div>
      <div class="feature-visual">
        <div class="feature-emoji-wrap">🎁</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# PRACTICAL INFO
# ════════════════════════════════════════════════════════════════════════════
with tabs[4]:
    st.markdown("""
    <div class="page-section">
      <div class="s-label">Everything you need to know</div>
      <div class="s-heading">Practical <em>Information</em></div>
      <div class="s-body" style="margin-top:12px;">
        I've tried to keep things simple and flexible. If you have questions not
        answered here, just reach out — I'm always happy to chat first. ☕
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("""
        <div style="padding:0 16px 48px 48px;">
          <div class="info-card">
            <h3>📅 Sessions</h3>
            <ul>
              <li>Sessions run <strong>weekly</strong>, on weekends</li>
              <li>Duration: <strong>60–90 minutes</strong> per age group</li>
              <li>Small groups of <strong>4–6 children</strong> maximum</li>
              <li><strong>In-person</strong> at [Location] or online via video call</li>
            </ul>
          </div>
          <div class="info-card">
            <h3>🎒 What to bring</h3>
            <ul>
              <li>Curiosity — that's really all!</li>
              <li>For in-person: a small notebook</li>
              <li>Occasionally: a simple ingredient for cooking activities (I'll always let you know in advance)</li>
            </ul>
          </div>
          <div class="info-card">
            <h3>🗓️ How to sign up</h3>
            <p>Drop me an email or a WhatsApp message. I'll suggest a free 20-minute introductory chat so we can meet and understand what your child is curious about. No commitment needed.</p>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="padding:0 48px 48px 16px;">
          <div class="info-card">
            <h3>💰 Pricing</h3>
            <ul>
              <li>Single session: <strong>[Price]</strong></li>
              <li>Monthly bundle (4 sessions): <strong>[Price]</strong></li>
              <li>Sibling discount available</li>
              <li>First introductory session: <strong>free</strong></li>
            </ul>
            <p style="font-size:13px;color:var(--ink-light);margin-top:12px;">
              I want these sessions to be accessible. If pricing is a barrier, please reach out — let's talk.
            </p>
          </div>
          <div class="info-card">
            <h3>🌐 Languages</h3>
            <p>Sessions are conducted in <strong>English</strong>, with Hindi woven in naturally. No Hindi knowledge needed to participate.</p>
          </div>
          <div class="info-card">
            <h3>📬 Get in touch</h3>
            <p>📧 <strong>[your@email.com]</strong><br/>
               📱 <strong>[Your phone / WhatsApp]</strong><br/>
               📍 <strong>[Your city / neighbourhood]</strong></p>
            <p style="font-size:13px;color:var(--ink-light);margin-top:12px;">
              I usually reply within 24 hours. WhatsApp very welcome!
            </p>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cta-banner">
      <div class="cta-banner-title">Let's start with a cup of chai ☕</div>
      <div class="cta-banner-sub">Free 20-minute intro chat. No commitment. Just a conversation.</div>
      <a class="btn-white" href="#">Get in touch</a>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="site-footer">
  <div>
    <div class="footer-brand">Shi<span>ksha</span></div>
    <div style="font-family:'Noto Sans Devanagari',sans-serif;font-size:14px;color:rgba(255,255,255,0.3);margin-top:4px;">शिक्षा — Sharing Indian culture, one story at a time</div>
  </div>
  <div class="footer-diyas">🪔 🌸 🪔 🌸 🪔</div>
  <div class="footer-copy">Made with ♥ · [Your city] · [Year]</div>
</div>
""", unsafe_allow_html=True)
