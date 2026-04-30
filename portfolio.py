import streamlit as st

# Configuration de la page web
st.set_page_config(page_title="Portfolio - Nawfal Douass", page_icon="🎓", layout="wide")

# En-tête : Informations de contact
st.title("DOUASS NAWFAL")
st.subheader("Étudiant en Réseaux et Télécoms")

col1, col2 = st.columns(2)
with col1:
    st.write("📍 **Adresse :** Rue Claessens 107, Boite 13, 1020 Laeken")
    st.write("✉️ **Email :** NAWFALZDS@GMAIL.COM")
with col2:
    st.write("🌐 **Site web :** https://portfolio-nawfal.streamlit.app")

st.divider()

# Section Résumé
st.header("👤 Résumé")
st.write("""
Étudiant en Réseaux et Télécoms, avec une expérience concrète en logistique et accueil client. 
Motivé, rigoureux et habitué au travail d'équipe, je recherche une opportunité pour mettre à profit 
mon sérieux et mes compétences linguistiques.
""")

st.divider()

# Section Éducation
st.header("🎓 Éducation")

st.markdown("### Haute école de Bruxelles ESI")
st.write("**Bachelier en réseau télécommunication** | *2025 - en cours*")

st.markdown("### INSTITUT SAINT-LOUIS")
st.write("**CESS Sciences-Math** | *2024*")
st.write("- Immersion Français-Néerlandais\n- Distinction en sciences")

st.markdown("### INSTITUT SAINT-LOUIS")
st.write("**Sciences-Math** | *2023*")
st.write("- Immersion Français-Néerlandais")
st.write("- Participation active dans des projets scolaires")
st.write("- Organisation d'événements éducatifs pour les pairs")

st.divider()

# Section Expérience Professionnelle
st.header("💼 Expérience Professionnelle")

st.markdown("### Employée | *Rock The City*")
st.write("*10/2025 - actuellement*")
st.write("- Accueillir les clients\n- Gestion d'équipe")

st.markdown("### Magasinier | *Proximus*")
st.write("*08/2024*")
st.write("- Gestion des stocks et des approvisionnements avec précision pour maximiser l'efficacité.")
st.write("- Coordination avec les équipes pour assurer un service client de qualité.")

st.markdown("### Animateur pour enfants | *IBO depuzzel laken*")
st.write("*08/2023*")
st.write("- Création et animation d'activités éducatives et ludiques pour les enfants.")
st.write("- Gestion des groupes d'enfants pour assurer la sécurité et le plaisir des participants.")

st.divider()

# Sections Compétences, Langues et Disponibilités
col3, col4, col5 = st.columns(3)

with col3:
    st.header("🗣️ Langues")
    st.write("- **Français :** Langue maternelle")
    st.write("- **Arabe :** Bilingue")
    st.write("- **Néerlandais :** Bilingue")
    st.write("- **Anglais :** Couramment")

with col4:
    st.header("🛠️ Compétences")
    st.write("- Word")
    st.write("- Excel")
    st.write("- PowerPoint")
    st.write("- Canva")
    st.write("- Python")
    st.write("- HTML/CSS/JS")

with col5:
    st.header("🕒 Disponibilité")
    st.write("- Vacances scolaires")
    st.write("- Jours fériés")
    st.write("- Week-end")

# Pied de page
st.divider()
st.caption("Portfolio généré en Python avec Streamlit - © Nawfal Douass")