import streamlit as st
from groq import Groq

# 1. Connexion sécurisée
Client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODELE_IA = "llama-3.1-8b-instant"

# 2. Configuration de la page
st.set_page_config(page_title="Assistant 2SF", page_icon="🌍")

# Barre latérale avec TON LOGO officiel
with st.sidebar:
    # Utilisation du lien que tu as fourni
    logo_url = "https://ong-2sf.org/wp-content/uploads/2025/08/cropped-Logo-Romaric-SWB-04-jrjr.png"
    st.image(logo_url, width="stretch")
    
    st.title("ONG 2SF")
    st.markdown("---")
    st.info("Assistant Virtuel Officiel - Solidarité Sans Frontière")
    
    if st.button("🗑️ Effacer la discussion"):
        st.session_state.messages = []
        st.rerun()

# Titre principal
st.title("🤖 Assistant Solidaire 2SF")
st.write("Bienvenue. Posez vos questions sur nos actions humanitaires.")

# 3. Gestion de la mémoire
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Interaction
if prompt := st.chat_input("Comment l'ONG 2SF peut-elle vous aider ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            # Instructions ultra-précises basées sur le web et tes besoins
            instructions = """
            Tu es l'assistant expert de l'ONG 'Solidarité Sans Frontière' (2SF).
            
            TES MISSIONS RÉELLES :
            - ÉDUCATION : Rénovation d'écoles, parrainage d'enfants vulnérables et kits scolaires.
            - SANTÉ : Hygiène menstruelle (kits réutilisables) et prévention du cancer du sein.
            - EAU : Construction de puits et accès à l'eau potable.
            - SOCIAL : Projet 'Ô Cœur de la Rue' et aide aux orphelinats.
            
            INFOS CONTACT :
            - SITE WEB : https://www.ong-2sf.org
            - EMAIL : contact@2sf-ong.org
            
            RÈGLES : Sois professionnel, chaleureux et cite le site web pour les dons.
            """
            
            completion = client.chat.completions.create(
                model=MODELE_IA,
                messages=[
                    {"role": "system", "content": instructions},
                    *st.session_state.messages
                ]
            )
            
            reponse = completion.choices[0].message.content
            st.markdown(reponse)
            st.session_state.messages.append({"role": "assistant", "content": reponse})
            
    except Exception as e:
        st.error(f"Erreur : {e}")
