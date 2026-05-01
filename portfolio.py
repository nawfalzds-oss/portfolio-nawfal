import streamlit as st

st.set_page_config(page_title="Portfolio - Nawfal Douass", page_icon="🎓", layout="wide")

# CSS global + animations 100% CSS (sans Javascript)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="fade-section delay-1" style="padding: 1.5rem 0 1rem;">
    <div class="hero-name">Douass Nawfal</div>
    <div class="hero-subtitle">Étudiant en Réseaux et Télécommunications · Haute école de Bruxelles ESI</div>
    <div class="badge-row">
        <span class="badge">📍 Laeken, Bruxelles</span>
        <span class="badge">✉️ NAWFALZDS@GMAIL.COM</span>
        <span class="badge">🌐 portfolio-nawfal.streamlit.app</span>
    </div>
    <p style="color:#555; font-size:0.95rem; max-width:600px; line-height:1.7;">
        Motivé, rigoureux et habitué au travail d'équipe — je recherche une opportunité pour 
        mettre à profit mon sérieux et mes compétences linguistiques.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── FORMATION ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="fade-section delay-2">
    <div class="section-label">🎓 Formation</div>
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-title">Bachelier en Réseaux et Télécommunications</div>
            <div class="timeline-org">Haute école de Bruxelles ESI</div>
            <div class="timeline-date">2025 — en cours</div>
        </div>
        <div class="timeline-item past">
            <div class="timeline-title">CESS Sciences-Math</div>
            <div class="timeline-org">Institut Saint-Louis</div>
            <div class="timeline-date">2023 - 2024</div>
            <div class="timeline-desc">Immersion Français–Néerlandais · Distinction en sciences</div>
        </div>
        <div class="timeline-item past">
            <div class="timeline-title">CE2D Sciences-économie</div>
            <div class="timeline-org">Institut Saint-Louis</div>
            <div class="timeline-date">2021-2022</div>
            <div class="timeline-desc">Immersion Fr/Nl · Projets scolaires · Organisation d'événements éducatifs</div>
        </div>
        <div>
            <div class="timeline-item past">
            <div class="timeline-title">CE1D Langue moderne</div>
            <div class="timeline-org">Institut Saint-Louis</div>
            <div class="timeline-date">2019 - 2020</div>
            <div class="timeline-desc">Immersion Fr/Nl</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── EXPÉRIENCE ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="fade-section delay-3">
    <div class="section-label">💼 Expérience professionnelle</div>
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-title">Employé — Rock The City</div>
            <div class="timeline-org">Accueil client · Gestion d'équipe</div>
            <div class="timeline-date">Oct. 2025 — actuellement</div>
        </div>
        <div class="timeline-item past">
            <div class="timeline-title">Magasinier — Proximus</div>
            <div class="timeline-org">Gestion des stocks et approvisionnements · Coordination inter-équipes</div>
            <div class="timeline-date">Août 2024</div>
        </div>
        <div class="timeline-item past">
            <div class="timeline-title">Animateur pour enfants — IBO Depuzzel Laken</div>
            <div class="timeline-org">Activités éducatives et ludiques · Encadrement de groupes</div>
            <div class="timeline-date">Août 2023</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── BÉNÉVOLAT ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="fade-section delay-4">
    <div class="section-label">🤝 Engagements & Bénévolat</div>
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-title">Responsable associatif</div>
            <div class="timeline-org">symfuny'Art</div>
            <div class="timeline-date">2018 — actuellement</div>
            <div class="timeline-desc">Gestion des activités, prise d'initiatives, sens des responsabilités et coordination.</div>
        </div>
        <div class="timeline-item">
            <div class="timeline-title">Bénévole — Pôle soutien scolaire</div>
            <div class="timeline-org">Solidarité réussite</div>
            <div class="timeline-date">2023 — actuellement</div>
            <div class="timeline-desc">Accompagnement pédagogique des élèves, transmission de connaissances et écoute active.</div>
        </div>
        <div class="timeline-item past">
            <div class="timeline-title">Membre du comité des jeunes</div>
            <div class="timeline-org">1001 schakels</div>
            <div class="timeline-date">2019 — 2025</div>
            <div class="timeline-desc">Participation aux décisions stratégiques, co-création de projets pour la jeunesse et travail en équipe.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── COMPÉTENCES ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="fade-section delay-4">
    <div class="section-label">🛠️ Compétences techniques</div>
    <div class="skill-row"><span class="skill-name">Python</span>
        <div class="skill-bar-bg"><div class="skill-bar" style="--target-width: 90%;"></div></div></div>
    <div class="skill-row"><span class="skill-name">HTML / CSS / JS</span>
        <div class="skill-bar-bg"><div class="skill-bar" style="--target-width: 80%;"></div></div></div>
    <div class="skill-row"><span class="skill-name">Excel</span>
        <div class="skill-bar-bg"><div class="skill-bar" style="--target-width: 70%;"></div></div></div>
    <div class="skill-row"><span class="skill-name">Word</span>
        <div class="skill-bar-bg"><div class="skill-bar" style="--target-width: 65%;"></div></div></div>
    <div class="skill-row"><span class="skill-name">PowerPoint</span>
        <div class="skill-bar-bg"><div class="skill-bar" style="--target-width: 78%;"></div></div></div>
    <div class="skill-row"><span class="skill-name">Canva</span>
        <div class="skill-bar-bg"><div class="skill-bar" style="--target-width: 75%;"></div></div></div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── LANGUES & DISPONIBILITÉ ───────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="fade-section delay-5">
        <div class="section-label">🗣️ Langues</div>
        <div class="lang-grid">
            <div class="lang-card"><div class="lang-name">Français</div><div class="lang-level">Langue maternelle</div></div>
            <div class="lang-card"><div class="lang-name">Arabe</div><div class="lang-level">Bilingue</div></div>
            <div class="lang-card"><div class="lang-name">Néerlandais</div><div class="lang-level">Bilingue</div></div>
            <div class="lang-card"><div class="lang-name">Anglais</div><div class="lang-level">Courant</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="fade-section delay-5">
        <div class="section-label">🕒 Disponibilité</div>
        <div class="dispo-grid">
            <span class="dispo-pill">Vacances scolaires</span>
            <span class="dispo-pill">Jours fériés</span>
            <span class="dispo-pill">Week-ends</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("Portfolio généré en Python avec Streamlit · © Nawfal Douass")
