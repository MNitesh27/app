import streamlit as st

st.set_page_config(
    page_title="Shiksha · शिक्षा",
    page_icon="🪔",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700&family=Noto+Sans+Devanagari:wght@400;600&display=swap');

:root {
    --saffron:    #E8732A;
    --marigold:   #F5A623;
    --teal:       #1A7A6E;
    --terracotta: #C4593A;
    --cream:      #FDF6EC;
    --ink:        #2C1810;
    --muted:      #7A6055;
    --card-bg:    #FFFAF3;
}

html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
    background-color: var(--cream);
    color: var(--ink);
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Animations ── */
@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    33%       { transform: translateY(-18px) rotate(3deg); }
    66%       { transform: translateY(-8px) rotate(-2deg); }
}
@keyframes flicker {
    0%, 100% { opacity:1; transform: scaleY(1) scaleX(1); }
    25%       { opacity:.85; transform: scaleY(1.08) scaleX(0.95); }
    50%       { opacity:.9; transform: scaleY(0.95) scaleX(1.05); }
    75%       { opacity:.95; transform: scaleY(1.05) scaleX(0.98); }
}
@keyframes shimmer {
    0%   { background-position: -200% center; }
    100% { background-position:  200% center; }
}
@keyframes spin-slow {
    from { transform: translateY(-50%) rotate(0deg); }
    to   { transform: translateY(-50%) rotate(360deg); }
}
@keyframes pulse-ring {
    0%   { transform: scale(1); opacity:.6; }
    100% { transform: scale(1.5); opacity:0; }
}
@keyframes fadeInUp {
    from { opacity:0; transform: translateY(28px); }
    to   { opacity:1; transform: translateY(0); }
}
@keyframes ticker {
    0%   { transform: translateX(100vw); }
    100% { transform: translateX(-100%); }
}
@keyframes bounce-in {
    0%   { transform: scale(0.85); opacity:0; }
    60%  { transform: scale(1.04); }
    100% { transform: scale(1); opacity:1; }
}

/* ── Festival ticker ── */
.ticker-wrap {
    background: var(--saffron);
    overflow: hidden;
    padding: 10px 0;
    white-space: nowrap;
}
.ticker-content {
    display: inline-block;
    animation: ticker 35s linear infinite;
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 13px;
    letter-spacing: 2px;
    color: white;
    padding-left: 100%;
}

/* ── Hero ── */
.hero {
    background: linear-gradient(135deg, #1a0f08 0%, #0f3330 45%, #2C1810 100%);
    padding: 64px 60px 52px;
    position: relative;
    overflow: hidden;
    min-height: 320px;
}
.hero-rangoli {
    position: absolute;
    right: 80px;
    top: 50%;
    transform: translateY(-50%);
    width: 240px;
    height: 240px;
    opacity: 0.17;
    animation: spin-slow 40s linear infinite;
}
.hero-eyebrow {
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 11px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--marigold);
    margin-bottom: 12px;
    animation: fadeInUp .8s ease both;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(44px, 6vw, 76px);
    color: var(--cream);
    line-height: 1.1;
    margin: 0 0 6px;
    animation: fadeInUp .8s ease .15s both;
}
.hero-title span {
    background: linear-gradient(90deg, var(--saffron), var(--marigold), var(--saffron));
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
    display: inline;
}
.hero-deva {
    font-family: 'Noto Sans Devanagari', sans-serif;
    font-size: 28px;
    color: rgba(253,246,236,0.35);
    margin-bottom: 20px;
    animation: fadeInUp .8s ease .3s both;
}
.hero-tagline {
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    font-size: 18px;
    color: rgba(253,246,236,0.82);
    max-width: 520px;
    line-height: 1.7;
    animation: fadeInUp .8s ease .45s both;
}

/* ── Floating diyas ── */
.diya-row {
    display: flex;
    justify-content: center;
    gap: 36px;
    padding: 28px 0 14px;
    background: linear-gradient(180deg, #1a0f08 0%, var(--cream) 100%);
}
.diya { font-size: 38px; display: inline-block; filter: drop-shadow(0 0 10px rgba(245,166,35,.7)); }
.diya:nth-child(1) { animation: float 3.2s ease-in-out infinite; }
.diya:nth-child(2) { animation: float 3.8s ease-in-out .4s infinite; }
.diya:nth-child(3) { animation: float 3.0s ease-in-out .8s infinite; }
.diya:nth-child(4) { animation: float 3.5s ease-in-out 1.2s infinite; }
.diya:nth-child(5) { animation: float 3.2s ease-in-out .6s infinite; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #2C1810;
    padding: 0 60px;
    gap: 0;
    border-bottom: none;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(253,246,236,0.5) !important;
    padding: 18px 24px;
    border: none !important;
    border-bottom: 3px solid transparent !important;
    background: transparent !important;
    transition: all .25s;
}
.stTabs [aria-selected="true"] {
    color: var(--marigold) !important;
    border-bottom: 3px solid var(--saffron) !important;
}
.stTabs [data-baseweb="tab-panel"] { padding: 0 !important; background: var(--cream); }

/* ── Sections ── */
.section { max-width: 900px; margin: 0 auto; padding: 56px 40px; }
.section-label {
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--saffron);
    margin-bottom: 8px;
}
.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    color: var(--ink);
    margin: 0 0 6px;
    line-height: 1.2;
}
.section-heading em { color: var(--teal); font-style: italic; }
.prose {
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    font-size: 17px;
    line-height: 1.85;
    color: #4A3328;
    max-width: 680px;
}

/* ── Cards ── */
.cards-row {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(155px, 1fr));
    gap: 16px;
    margin-top: 34px;
}
.card {
    background: var(--card-bg);
    border: 1.5px solid rgba(232,115,42,0.15);
    border-radius: 16px;
    padding: 28px 16px 22px;
    text-align: center;
    transition: transform .25s cubic-bezier(.34,1.56,.64,1), box-shadow .25s, border-color .25s;
    animation: bounce-in .5s ease both;
    cursor: default;
}
.card:hover {
    transform: translateY(-9px) scale(1.04);
    box-shadow: 0 18px 40px rgba(44,24,16,0.13);
    border-color: var(--saffron);
}
.card-icon { font-size: 36px; margin-bottom: 12px; display: block; }
.card-title { font-family: 'Lato', sans-serif; font-weight: 700; font-size: 13px; letter-spacing: .5px; color: var(--ink); margin-bottom: 5px; }
.card-sub   { font-family: 'Lato', sans-serif; font-weight: 300; font-size: 12px; color: var(--muted); }

/* ── Quote ── */
.quote-block {
    border-left: 4px solid var(--saffron);
    padding: 22px 32px;
    margin: 40px 0;
    background: linear-gradient(135deg, rgba(245,166,35,.08), rgba(232,115,42,.04));
    border-radius: 0 12px 12px 0;
    position: relative;
    overflow: hidden;
}
.quote-block::before {
    content: '\201C';
    position: absolute;
    right: 20px; top: -10px;
    font-size: 100px;
    font-family: 'Playfair Display', serif;
    color: rgba(232,115,42,.08);
    line-height: 1;
}
.quote-hindi { font-family: 'Noto Sans Devanagari', sans-serif; font-size: 22px; color: var(--ink); margin-bottom: 8px; }
.quote-translation { font-family: 'Playfair Display', serif; font-style: italic; font-size: 15px; color: var(--muted); }

/* ── Pill ── */
.pill-row { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 28px; }
.pill {
    background: rgba(26,122,110,.10);
    border: 1px solid rgba(26,122,110,.25);
    color: var(--teal);
    border-radius: 999px;
    padding: 7px 18px;
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 13px;
    transition: background .2s, transform .2s;
    cursor: default;
}
.pill:hover { background: rgba(26,122,110,.18); transform: scale(1.05); }

/* ── Audience cards ── */
.aud-card {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 28px 30px 24px;
    border: 1.5px solid rgba(196,89,58,.10);
    margin-bottom: 16px;
    transition: transform .2s, box-shadow .2s, border-color .2s;
}
.aud-card:hover {
    transform: translateX(7px);
    box-shadow: -4px 0 0 var(--saffron), 6px 10px 28px rgba(44,24,16,.09);
    border-color: rgba(232,115,42,.28);
}
.aud-title { font-family: 'Playfair Display', serif; font-size: 20px; color: var(--ink); margin-bottom: 10px; }
.aud-body  { font-family: 'Lato', sans-serif; font-weight: 300; font-size: 15px; color: #4A3328; line-height: 1.75; }

/* ── Fun strip ── */
.fun-strip {
    background: var(--teal);
    color: white;
    padding: 40px;
    text-align: center;
}
.fun-strip-title {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 22px;
    color: rgba(255,255,255,.88);
    margin-bottom: 28px;
}
.fun-nums { display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; }
.fun-num-val   { font-family: 'Playfair Display', serif; font-size: 52px; color: var(--marigold); line-height: 1; margin-bottom: 6px; }
.fun-num-label { font-family: 'Lato', sans-serif; font-weight: 300; font-size: 12px; letter-spacing: 2px; color: rgba(255,255,255,.65); text-transform: uppercase; }

/* ── Info blocks ── */
.info-block {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 32px;
    border: 1.5px solid rgba(232,115,42,.12);
    margin-bottom: 20px;
    transition: transform .2s, box-shadow .2s;
}
.info-block:hover { transform: translateY(-4px); box-shadow: 0 14px 36px rgba(44,24,16,.09); }
.info-block h3 { font-family: 'Playfair Display', serif; font-size: 20px; color: var(--ink); margin: 0 0 12px; }
.info-block p, .info-block li { font-family: 'Lato', sans-serif; font-weight: 300; font-size: 15px; color: #4A3328; line-height: 1.7; }
.info-block ul { padding-left: 18px; }

.rule { border: none; border-top: 1px solid rgba(44,24,16,.10); margin: 44px 0; }

/* ── Footer ── */
.footer {
    background: #2C1810;
    text-align: center;
    padding: 30px 20px;
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    font-size: 13px;
    color: rgba(253,246,236,.4);
    letter-spacing: .5px;
}
.footer span { color: var(--saffron); }
.footer-diyas { font-size: 22px; margin-bottom: 8px; letter-spacing: 8px; }
</style>
""", unsafe_allow_html=True)

# ── Festival ticker ───────────────────────────────────────────────────────────
st.markdown("""
<div class="ticker-wrap">
  <span class="ticker-content">
    🪔 Diwali — Festival of Lights &nbsp;·&nbsp;
    🌈 Holi — Festival of Colours &nbsp;·&nbsp;
    🌙 Eid Mubarak &nbsp;·&nbsp;
    🌸 Navratri — Nine Nights of Dance &nbsp;·&nbsp;
    🥁 Baisakhi — Harvest Celebration &nbsp;·&nbsp;
    🪁 Makar Sankranti — Kite Festival &nbsp;·&nbsp;
    🐘 Ganesh Chaturthi &nbsp;·&nbsp;
    🌺 Pongal — Tamil New Year &nbsp;·&nbsp;
    🎋 Onam — Kerala's Grand Harvest &nbsp;·&nbsp;
    🎊 Raksha Bandhan &nbsp;·&nbsp;
    🎵 Janmashtami &nbsp;·&nbsp;
  </span>
</div>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <svg class="hero-rangoli" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <circle cx="100" cy="100" r="95" stroke="#F5A623" stroke-width="1.5" fill="none"/>
    <circle cx="100" cy="100" r="75" stroke="#E8732A" stroke-width="1"   fill="none"/>
    <circle cx="100" cy="100" r="55" stroke="#F5A623" stroke-width="1.5" fill="none"/>
    <circle cx="100" cy="100" r="35" stroke="#E8732A" stroke-width="1"   fill="none"/>
    <circle cx="100" cy="100" r="14" fill="#F5A623"   fill-opacity="0.5"/>
    <ellipse cx="100" cy="18"  rx="8" ry="18" fill="#F5A623" fill-opacity="0.55"/>
    <ellipse cx="100" cy="182" rx="8" ry="18" fill="#F5A623" fill-opacity="0.55"/>
    <ellipse cx="18"  cy="100" rx="18" ry="8" fill="#F5A623" fill-opacity="0.55"/>
    <ellipse cx="182" cy="100" rx="18" ry="8" fill="#F5A623" fill-opacity="0.55"/>
    <ellipse cx="43"  cy="43"  rx="8" ry="18" transform="rotate(45 43 43)"   fill="#E8732A" fill-opacity="0.45"/>
    <ellipse cx="157" cy="43"  rx="8" ry="18" transform="rotate(-45 157 43)" fill="#E8732A" fill-opacity="0.45"/>
    <ellipse cx="43"  cy="157" rx="8" ry="18" transform="rotate(-45 43 157)" fill="#E8732A" fill-opacity="0.45"/>
    <ellipse cx="157" cy="157" rx="8" ry="18" transform="rotate(45 157 157)" fill="#E8732A" fill-opacity="0.45"/>
    <polygon points="100,62 107,88 134,88 113,104 121,130 100,115 79,130 87,104 66,88 93,88"
             fill="#F5A623" fill-opacity="0.35"/>
  </svg>

  <div class="hero-eyebrow">शिक्षा · A Space to Learn &amp; Belong</div>
  <div class="hero-title">Welcome to <span>Shiksha</span></div>
  <div class="hero-deva">शिक्षा</div>
  <div class="hero-tagline">
    A warm, personal journey into Indian culture — language, festivals,
    food, traditions &amp; stories — for children and families wherever they are.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Floating diyas ────────────────────────────────────────────────────────────
st.markdown("""
<div class="diya-row">
  <span class="diya">🪔</span>
  <span class="diya">🪔</span>
  <span class="diya">🪔</span>
  <span class="diya">🪔</span>
  <span class="diya">🪔</span>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tabs = st.tabs(["🏠 Home", "🪔 About Shiksha", "🌸 About the Author", "👨‍👩‍👧 For Who", "📋 Practical Information"])

# ════════ HOME ════════════════════════════════════════════════════════════════
with tabs[0]:
    st.markdown("""
    <div class="section">
        <div class="section-label">A Little Corner of India</div>
        <div class="section-heading">Where every child can find <em>their roots</em></div>
        <br/>
        <div class="prose">
            Whether your family grew up lighting diyas at Diwali, or you're discovering
            the beauty of India's traditions for the very first time — Shiksha is here for you.
            <br/><br/>
            This is not a classroom. It's a gathering. A place where children can hear a Hindi
            story, taste the name of a spice, and understand <em>why</em> we celebrate the way we do.
            Learning happens when it feels like belonging.
        </div>

        <div class="quote-block">
            <div class="quote-hindi">ज्ञान ही शक्ति है।</div>
            <div class="quote-translation">"Knowledge is power." — Indian proverb</div>
        </div>

        <div class="section-label" style="margin-top:40px;">What We Explore Together</div>
        <div class="cards-row">
            <div class="card" style="animation-delay:.0s"><span class="card-icon">🗣️</span><div class="card-title">Hindi</div><div class="card-sub">Words, scripts &amp; simple conversation</div></div>
            <div class="card" style="animation-delay:.1s"><span class="card-icon">🎉</span><div class="card-title">Festivals</div><div class="card-sub">Diwali, Holi, Eid, Navratri &amp; more</div></div>
            <div class="card" style="animation-delay:.2s"><span class="card-icon">🏺</span><div class="card-title">Traditions</div><div class="card-sub">Rituals, customs &amp; their meaning</div></div>
            <div class="card" style="animation-delay:.3s"><span class="card-icon">🙏</span><div class="card-title">Religion</div><div class="card-sub">Stories &amp; values from India's faiths</div></div>
            <div class="card" style="animation-delay:.4s"><span class="card-icon">🍛</span><div class="card-title">Cuisine</div><div class="card-sub">Flavours, spices &amp; food stories</div></div>
            <div class="card" style="animation-delay:.5s"><span class="card-icon">🎨</span><div class="card-title">Arts &amp; Crafts</div><div class="card-sub">Rangoli, mehendi &amp; music</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="fun-strip">
        <div class="fun-strip-title">India in numbers — a taste of how rich this culture is</div>
        <div class="fun-nums">
            <div><div class="fun-num-val">22+</div><div class="fun-num-label">Official languages</div></div>
            <div><div class="fun-num-val">40+</div><div class="fun-num-label">Festivals a year</div></div>
            <div><div class="fun-num-val">5000</div><div class="fun-num-label">Years of history</div></div>
            <div><div class="fun-num-val">6</div><div class="fun-num-label">Major religions</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
        <div class="section-label">Why Shiksha?</div>
        <div class="section-heading">Culture isn't just <em>history</em></div>
        <br/>
        <div class="prose">
            For many families raising children outside India — or for families
            new to Indian culture — it can feel hard to know where to start.
            How do you pass on something as vast and rich as Indian heritage
            in a way that feels alive, not like homework?
            <br/><br/>
            Shiksha starts small: one festival, one dish, one word at a time.
            The goal is never to overwhelm — it's to spark curiosity and give
            children a sense of pride in where they come from, or where they belong.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ════════ ABOUT SHIKSHA ═══════════════════════════════════════════════════════
with tabs[1]:
    st.markdown("""
    <div class="section">
        <div class="section-label">The Project</div>
        <div class="section-heading">What is <em>Shiksha</em>?</div>
        <br/>
        <div class="prose">
            Shiksha (शिक्षा) is the Sanskrit and Hindi word for <em>education</em>.
            It felt like the right name for a project that believes learning about
            culture is one of the most profound gifts we can give a child.
            <br/><br/>
            This is a small, personal tutorship — not a school, not a business.
            It's a series of gentle sessions where children aged 5 to 14 can explore
            Indian culture through stories, activities, cooking, crafts, and language.
        </div>

        <hr class="rule"/>

        <div class="section-label">The Subjects</div>
        <div class="section-heading">Six threads of <em>one rich fabric</em></div>
        <div class="cards-row">
            <div class="card" style="animation-delay:.0s"><span class="card-icon">🗣️</span><div class="card-title">Hindi Language</div><div class="card-sub">Devanagari script, vocabulary &amp; songs</div></div>
            <div class="card" style="animation-delay:.1s"><span class="card-icon">🎊</span><div class="card-title">Festivals</div><div class="card-sub">The calendar &amp; stories behind each celebration</div></div>
            <div class="card" style="animation-delay:.2s"><span class="card-icon">🙏</span><div class="card-title">Religions</div><div class="card-sub">Hinduism, Islam, Sikhism, Buddhism &amp; Jainism</div></div>
            <div class="card" style="animation-delay:.3s"><span class="card-icon">🏺</span><div class="card-title">Traditions</div><div class="card-sub">Weddings, seasons &amp; daily rituals</div></div>
            <div class="card" style="animation-delay:.4s"><span class="card-icon">🍛</span><div class="card-title">Cuisine</div><div class="card-sub">Spices, regional dishes &amp; food stories</div></div>
            <div class="card" style="animation-delay:.5s"><span class="card-icon">🎨</span><div class="card-title">Arts &amp; Crafts</div><div class="card-sub">Rangoli, mehendi, music &amp; dance</div></div>
        </div>

        <hr class="rule"/>

        <div class="quote-block">
            <div class="quote-hindi">पढ़ना लिखना सीखो, ओ मेहनत करने वालों।</div>
            <div class="quote-translation">"Learn to read and write, O hardworking ones." — folk saying</div>
        </div>

        <div class="prose">
            Sessions are designed to be <strong>hands-on and playful</strong>.
            A lesson about Diwali might end with making a paper diya.
            A Hindi session might begin with learning the names of family members
            through a silly game. The goal is for children to leave each session
            with something they want to share at home.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ════════ ABOUT AUTHOR ════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown("""
    <div class="section">
        <div class="section-label">The Person Behind Shiksha</div>
        <div class="section-heading">A little bit <em>about me</em></div>
        <br/>
        <div class="prose">
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

        <div class="quote-block">
            <div class="quote-hindi">संस्कृति वो है जो हम अगली पीढ़ी को देते हैं।</div>
            <div class="quote-translation">"Culture is what we pass on to the next generation."</div>
        </div>

        <div class="section-label">A little more about me</div>
        <div class="pill-row">
            <span class="pill">🇮🇳 Grew up in [City], India</span>
            <span class="pill">🌍 Living in [Your Country] since [Year]</span>
            <span class="pill">📚 Background in [Your Field]</span>
            <span class="pill">🍳 Amateur cook of Indian food</span>
            <span class="pill">🎵 Big fan of Bollywood classics</span>
            <span class="pill">🌸 Storyteller at heart</span>
        </div>

        <hr class="rule"/>

        <div class="prose">
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

# ════════ FOR WHO ═════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown("""
    <div class="section">
        <div class="section-label">Who is this for?</div>
        <div class="section-heading">For curious children <em>everywhere</em></div>
        <br/>
        <div class="prose">
            Shiksha was designed with a few families in mind — and chances are,
            you'll recognise yourself in one of them.
        </div>
        <br/>

        <div class="aud-card">
            <div class="aud-title">🏡 Families of Indian heritage living abroad</div>
            <div class="aud-body">Your children were born here, but you want them to understand where
            your family comes from — the language your parents spoke, the festivals you grew up celebrating,
            the food that makes you feel at home. Shiksha is a gentle bridge between two worlds.</div>
        </div>

        <div class="aud-card">
            <div class="aud-title">🌍 Mixed-heritage and multicultural families</div>
            <div class="aud-body">One parent is Indian, one is not — or your family has woven together
            multiple cultures. Indian culture is one colourful thread in your child's identity,
            and Shiksha helps them hold it with pride and understanding.</div>
        </div>

        <div class="aud-card">
            <div class="aud-title">✨ Families new to Indian culture</div>
            <div class="aud-body">You have Indian friends, neighbours, or colleagues. Or perhaps your child
            is curious after learning about Diwali at school. You don't need to be Indian to appreciate
            the richness of this culture — everyone is welcome.</div>
        </div>

        <div class="aud-card">
            <div class="aud-title">👧 Children aged 5 to 14</div>
            <div class="aud-body">Sessions are tailored to age groups. Younger children (5–8) will love
            stories, songs and crafts. Older children (9–14) can go deeper into language, history and meaning.
            No prior knowledge needed — just an open mind and a healthy appetite (we do talk about food a lot 🍛).</div>
        </div>

        <hr class="rule"/>

        <div class="section-label">What parents can expect</div>
        <div class="prose">
            After each session, your child will come home with something:
            a word, a story, a small craft, a question to ask you.
            Sessions are never heavy. There are no grades, no pressure.
            I want children to leave feeling like they've been part of something warm —
            like visiting a family friend's home where something delicious was always on the stove.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ════════ PRACTICAL INFO ══════════════════════════════════════════════════════
with tabs[4]:
    st.markdown("""
    <div class="section">
        <div class="section-label">Everything you need to know</div>
        <div class="section-heading">Practical <em>Information</em></div>
        <br/>
        <div class="prose">
            I've tried to keep things simple and flexible.
            If you have questions not answered here, please just reach out —
            I'm always happy to have a conversation first. ☕
        </div>
        <br/>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("""
        <div style="padding:0 20px 0 40px;">
        <div class="info-block">
            <h3>📅 Sessions</h3>
            <ul>
                <li>Sessions run <strong>weekly</strong>, on weekends</li>
                <li>Duration: <strong>60–90 minutes</strong> per age group</li>
                <li>Small groups of <strong>4–6 children</strong> maximum</li>
                <li><strong>In-person</strong> at [Location] or online via video call</li>
            </ul>
        </div>
        <div class="info-block">
            <h3>🎒 What to bring</h3>
            <ul>
                <li>Curiosity — that's really all!</li>
                <li>For in-person: a small notebook</li>
                <li>Occasionally: a simple ingredient for cooking activities (I'll always let you know in advance)</li>
            </ul>
        </div>
        <div class="info-block">
            <h3>🗓️ How to sign up</h3>
            <p>Drop me an email or a WhatsApp message. I'll suggest a free 20-minute introductory chat so we
            can meet and I can understand what your child is curious about. No commitment needed at that stage.</p>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="padding:0 40px 0 20px;">
        <div class="info-block">
            <h3>💰 Pricing</h3>
            <ul>
                <li>Single session: <strong>[Price]</strong></li>
                <li>Monthly bundle (4 sessions): <strong>[Price]</strong></li>
                <li>Sibling discount available</li>
                <li>First introductory session: <strong>free</strong></li>
            </ul>
            <p style="font-size:13px;color:#7A6055;margin-top:10px;">
                I want these sessions to be accessible. If pricing is a barrier, please reach out — let's talk.
            </p>
        </div>
        <div class="info-block">
            <h3>🌐 Languages</h3>
            <p>Sessions are conducted in <strong>English</strong>, with Hindi woven in naturally.
            No Hindi knowledge needed to participate.</p>
        </div>
        <div class="info-block">
            <h3>📬 Get in touch</h3>
            <p>📧 <strong>[your@email.com]</strong><br/>
               📱 <strong>[Your phone / WhatsApp]</strong><br/>
               📍 <strong>[Your city / neighbourhood]</strong></p>
            <p style="font-size:13px;color:#7A6055;margin-top:10px;">
                I usually reply within 24 hours. WhatsApp messages are very welcome!
            </p>
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-diyas">🪔 🌸 🪔 🌸 🪔</div>
    Made with <span>♥</span> &nbsp;·&nbsp; Shiksha · शिक्षा &nbsp;·&nbsp;
    Sharing Indian culture, one story at a time
</div>
""", unsafe_allow_html=True)
