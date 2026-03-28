import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Shiksha · शिक्षा",
    page_icon="🪔",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700&family=Noto+Sans+Devanagari:wght@400;600&display=swap');

/* ── Tokens ── */
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

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
    background-color: var(--cream);
    color: var(--ink);
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Hero banner ── */
.hero {
    background: linear-gradient(135deg, #2C1810 0%, #1A4A40 50%, #2C1810 100%);
    padding: 56px 60px 44px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "ॐ";
    font-family: 'Noto Sans Devanagari', sans-serif;
    position: absolute;
    right: 60px; top: 20px;
    font-size: 140px;
    color: rgba(232,115,42,0.12);
    line-height: 1;
    pointer-events: none;
}
.hero-eyebrow {
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--marigold);
    margin-bottom: 10px;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(42px, 6vw, 72px);
    color: var(--cream);
    line-height: 1.1;
    margin: 0 0 4px;
}
.hero-title span {
    color: var(--saffron);
    font-style: italic;
}
.hero-deva {
    font-family: 'Noto Sans Devanagari', sans-serif;
    font-size: 26px;
    color: rgba(253,246,236,0.45);
    margin-bottom: 18px;
}
.hero-tagline {
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    font-size: 18px;
    color: rgba(253,246,236,0.80);
    max-width: 560px;
    line-height: 1.6;
}
.hero-divider {
    width: 60px; height: 3px;
    background: var(--saffron);
    margin: 20px 0 0;
    border-radius: 2px;
}

/* ── Tab nav ── */
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
    color: rgba(253,246,236,0.55) !important;
    padding: 18px 24px;
    border: none !important;
    border-bottom: 3px solid transparent !important;
    background: transparent !important;
    transition: all .2s;
}
.stTabs [aria-selected="true"] {
    color: var(--marigold) !important;
    border-bottom: 3px solid var(--saffron) !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding: 0 !important;
    background: var(--cream);
}

/* ── Section wrapper ── */
.section {
    max-width: 900px;
    margin: 0 auto;
    padding: 56px 40px;
}
.section-wide {
    max-width: 1100px;
    margin: 0 auto;
    padding: 56px 40px;
}

/* ── Section headings ── */
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
.section-heading em {
    color: var(--teal);
    font-style: italic;
}
.prose {
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    font-size: 17px;
    line-height: 1.8;
    color: #4A3328;
    max-width: 680px;
}

/* ── Explore cards ── */
.cards-row {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 16px;
    margin-top: 36px;
}
.card {
    background: var(--card-bg);
    border: 1px solid rgba(232,115,42,0.15);
    border-radius: 12px;
    padding: 24px 16px 20px;
    text-align: center;
    transition: transform .2s, box-shadow .2s;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(44,24,16,0.10);
}
.card-icon { font-size: 32px; margin-bottom: 10px; }
.card-title {
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 13px;
    letter-spacing: .5px;
    color: var(--ink);
    margin-bottom: 4px;
}
.card-sub {
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    font-size: 12px;
    color: var(--muted);
}

/* ── Quote block ── */
.quote-block {
    border-left: 4px solid var(--saffron);
    padding: 20px 28px;
    margin: 36px 0;
    background: rgba(245,166,35,0.07);
    border-radius: 0 8px 8px 0;
}
.quote-hindi {
    font-family: 'Noto Sans Devanagari', sans-serif;
    font-size: 22px;
    color: var(--ink);
    margin-bottom: 6px;
}
.quote-translation {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 15px;
    color: var(--muted);
}

/* ── Info pills ── */
.pill-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 28px;
}
.pill {
    background: rgba(26,122,110,0.10);
    border: 1px solid rgba(26,122,110,0.25);
    color: var(--teal);
    border-radius: 999px;
    padding: 6px 16px;
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 13px;
}

/* ── Audience cards ── */
.aud-card {
    background: var(--card-bg);
    border-radius: 14px;
    padding: 28px 28px 24px;
    border: 1px solid rgba(196,89,58,0.12);
    margin-bottom: 16px;
}
.aud-title {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    color: var(--ink);
    margin-bottom: 8px;
}
.aud-body {
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    font-size: 15px;
    color: #4A3328;
    line-height: 1.7;
}

/* ── Practical info ── */
.info-block {
    background: var(--card-bg);
    border-radius: 14px;
    padding: 32px;
    border: 1px solid rgba(232,115,42,0.15);
    margin-bottom: 20px;
}
.info-block h3 {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    color: var(--ink);
    margin: 0 0 12px;
}
.info-block p, .info-block li {
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    font-size: 15px;
    color: #4A3328;
    line-height: 1.7;
}
.info-block ul { padding-left: 18px; }

/* ── Thin rule ── */
.rule {
    border: none;
    border-top: 1px solid rgba(44,24,16,0.10);
    margin: 40px 0;
}

/* ── Footer ── */
.footer {
    background: #2C1810;
    text-align: center;
    padding: 28px 20px;
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    font-size: 13px;
    color: rgba(253,246,236,0.45);
    letter-spacing: .5px;
}
.footer span { color: var(--saffron); }
</style>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">शिक्षा · A Space to Learn &amp; Belong</div>
    <div class="hero-title">Welcome to <span>Shiksha</span></div>
    <div class="hero-deva">शिक्षा</div>
    <div class="hero-tagline">
        A warm, personal journey into Indian culture — language, festivals, 
        food, traditions &amp; stories — for children and families wherever they are.
    </div>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tabs = st.tabs(["🏠 Home", "🪔 About Shiksha", "🌸 About the Author", "👨‍👩‍👧 For Who", "📋 Practical Information"])

# ════════════════════════════════════════════════════════════════════════════
# HOME
# ════════════════════════════════════════════════════════════════════════════
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
            <div class="card">
                <div class="card-icon">🗣️</div>
                <div class="card-title">Hindi</div>
                <div class="card-sub">Words, scripts &amp; simple conversation</div>
            </div>
            <div class="card">
                <div class="card-icon">🎉</div>
                <div class="card-title">Festivals</div>
                <div class="card-sub">Diwali, Holi, Eid, Navratri &amp; more</div>
            </div>
            <div class="card">
                <div class="card-icon">🕌</div>
                <div class="card-title">Traditions</div>
                <div class="card-sub">Rituals, customs &amp; their meaning</div>
            </div>
            <div class="card">
                <div class="card-icon">🙏</div>
                <div class="card-title">Religion</div>
                <div class="card-sub">Stories &amp; values from India's faiths</div>
            </div>
            <div class="card">
                <div class="card-icon">🍛</div>
                <div class="card-title">Cuisine</div>
                <div class="card-sub">Flavours, spices &amp; food stories</div>
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:rgba(26,122,110,0.07); padding: 0;">
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
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# ABOUT SHIKSHA
# ════════════════════════════════════════════════════════════════════════════
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
        <div class="cards-row" style="margin-top:28px;">
            <div class="card">
                <div class="card-icon">🗣️</div>
                <div class="card-title">Hindi Language</div>
                <div class="card-sub">Devanagari script, vocabulary, songs &amp; conversation starters</div>
            </div>
            <div class="card">
                <div class="card-icon">🎊</div>
                <div class="card-title">Festivals</div>
                <div class="card-sub">The calendar of celebrations &amp; the stories behind them</div>
            </div>
            <div class="card">
                <div class="card-icon">🙏</div>
                <div class="card-title">Religions</div>
                <div class="card-sub">Hinduism, Islam, Sikhism, Buddhism &amp; Jainism — values &amp; stories</div>
            </div>
            <div class="card">
                <div class="card-icon">🏺</div>
                <div class="card-title">Traditions</div>
                <div class="card-sub">Weddings, seasons, daily rituals &amp; their meaning</div>
            </div>
            <div class="card">
                <div class="card-icon">🍛</div>
                <div class="card-title">Cuisine</div>
                <div class="card-sub">Spices, regional dishes &amp; the stories food carries</div>
            </div>
            <div class="card">
                <div class="card-icon">🎨</div>
                <div class="card-title">Arts &amp; Crafts</div>
                <div class="card-sub">Rangoli, mehendi, music &amp; classical dance forms</div>
            </div>
        </div>

        <hr class="rule"/>

        <div class="prose">
            Sessions are designed to be <strong>hands-on and playful</strong>. 
            A lesson about Diwali might end with making a paper diya. 
            A Hindi session might begin with learning the names of family members 
            through a silly game. The goal is for children to leave each session 
            with something they want to share at home.
        </div>

    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# ABOUT AUTHOR
# ════════════════════════════════════════════════════════════════════════════
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
            <span class="pill">🍳 Amateur cook of South/North Indian food</span>
            <span class="pill">🎵 Big fan of Bollywood classics</span>
            <span class="pill">🌸 Mother / Parent / Aunt — storyteller</span>
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
            over a cup of chai before signing up — I'd love that.
        </div>

    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# FOR WHO
# ════════════════════════════════════════════════════════════════════════════
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
            <div class="aud-body">
                Your children were born here, but you want them to understand where 
                your family comes from — the language your parents spoke, the festivals 
                you grew up celebrating, the food that makes you feel at home. 
                Shiksha is a gentle bridge between two worlds.
            </div>
        </div>

        <div class="aud-card">
            <div class="aud-title">🌍 Mixed-heritage and multicultural families</div>
            <div class="aud-body">
                One parent is Indian, one is not — or your family has woven together 
                multiple cultures. Indian culture is one colourful thread in your 
                child's identity, and Shiksha helps them hold it with pride and understanding.
            </div>
        </div>

        <div class="aud-card">
            <div class="aud-title">✨ Families new to Indian culture</div>
            <div class="aud-body">
                You have Indian friends, neighbours, or colleagues. Or perhaps your child 
                is curious after learning about Diwali at school. You don't need to be 
                Indian to appreciate the richness of this culture — everyone is welcome.
            </div>
        </div>

        <div class="aud-card">
            <div class="aud-title">👧 Children aged 5 to 14</div>
            <div class="aud-body">
                Sessions are tailored to age groups. Younger children (5–8) will love 
                stories, songs and crafts. Older children (9–14) can go deeper into 
                language, history and meaning. No prior knowledge needed — just an 
                open mind and a healthy appetite (we do talk about food a lot).
            </div>
        </div>

        <hr class="rule"/>

        <div class="section-label">What parents can expect</div>
        <div class="prose">
            After each session, your child will come home with something: 
            a word, a story, a small craft, a question to ask you. 
            Sessions are never heavy. There are no grades, no pressure. 
            I want children to leave feeling like they've been part of something warm — 
            like visiting a family friend's home where something delicious was 
            always on the stove.
        </div>

    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# PRACTICAL INFO
# ════════════════════════════════════════════════════════════════════════════
with tabs[4]:
    st.markdown("""
    <div class="section">

        <div class="section-label">Everything you need to know</div>
        <div class="section-heading">Practical <em>Information</em></div>
        <br/>
        <div class="prose">
            I've tried to keep things simple and flexible. 
            If you have questions not answered here, please just reach out — 
            I'm always happy to have a conversation first.
        </div>
        <br/>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div style="padding: 0 20px 0 40px;">

        <div class="info-block">
            <h3>📅 Sessions</h3>
            <ul>
                <li>Sessions run <strong>weekly</strong>, on weekends</li>
                <li>Duration: <strong>60–90 minutes</strong> depending on age group</li>
                <li>Small groups of <strong>4–6 children</strong> maximum</li>
                <li>Sessions held <strong>in-person</strong> at [Location] or online via video call</li>
            </ul>
        </div>

        <div class="info-block">
            <h3>🎒 What to bring</h3>
            <ul>
                <li>Curiosity — that's really all!</li>
                <li>For in-person sessions: a small notebook</li>
                <li>Occasionally: a simple ingredient for cooking activities 
                    (I'll always let you know in advance)</li>
            </ul>
        </div>

        <div class="info-block">
            <h3>🗓️ How to sign up</h3>
            <p>
                Drop me an email or fill in the contact form below. 
                I'll suggest a free 20-minute introductory chat so we 
                can meet and I can understand what your child is curious about. 
                No commitment needed at that stage.
            </p>
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="padding: 0 40px 0 20px;">

        <div class="info-block">
            <h3>💰 Pricing</h3>
            <ul>
                <li>Single session: <strong>[Price]</strong></li>
                <li>Monthly bundle (4 sessions): <strong>[Price]</strong></li>
                <li>Sibling discount available</li>
                <li>First introductory session: <strong>free</strong></li>
            </ul>
            <p style="font-size:13px; color:#7A6055; margin-top:10px;">
                I want these sessions to be accessible. If pricing is a barrier, 
                please reach out — let's talk.
            </p>
        </div>

        <div class="info-block">
            <h3>🌐 Languages</h3>
            <p>Sessions are conducted in <strong>English</strong>, 
            with Hindi woven in naturally. No Hindi knowledge is needed to participate.</p>
        </div>

        <div class="info-block">
            <h3>📬 Get in touch</h3>
            <p>
                📧 <strong>[your@email.com]</strong><br/>
                📱 <strong>[Your phone / WhatsApp]</strong><br/>
                📍 <strong>[Your city / neighbourhood]</strong>
            </p>
            <p style="font-size:13px; color:#7A6055; margin-top:10px;">
                I usually reply within 24 hours. 
                WhatsApp messages are also very welcome!
            </p>
        </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Made with <span>♥</span> &nbsp;·&nbsp; Shiksha · शिक्षा &nbsp;·&nbsp; 
    Sharing Indian culture, one story at a time
</div>
""", unsafe_allow_html=True)
