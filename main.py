import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import numpy as np

# Configuration de la page
st.set_page_config(page_title="Portfolio Data Engineer", page_icon=":bar_chart:", layout="wide")

# Partie Présentation
st.title("Portfolio Data Engineer")
st.header("Présentation")

# Ajout de la photo
# Télécharger et afficher l'image
image_url = "https://avatars.githubusercontent.com/u/114836746?v=4"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))
st.image(image, caption='Votre Nom')

# Description
st.write("""
Bonjour, je suis [Votre Nom], un Data Engineer passionné par la manipulation et l'analyse des données. 
Je suis spécialisé dans la création de pipelines de données robustes et évolutifs.
""")

# Bouton pour télécharger un PDF
# with open("path_to_your_resume.pdf", "rb") as pdf_file:
    # PDFbyte = pdf_file.read()

# st.download_button(label="Télécharger mon CV", data=PDFbyte, file_name="CV_VotreNom.pdf", mime='application/octet-stream')

# Partie Compétences
st.header("Compétences")

skills = {
    "Python": "🐍",
    "SQL": "🗄️",
    "Apache Spark": "⚡",
    "Hadoop": "🐘",
    "Docker": "🐳",
    "Kubernetes": "☸️",
    "AWS": "☁️",
    "GCP": "☁️",
    "Azure": "☁️"
}

for skill, icon in skills.items():
    st.write(f"{icon} {skill}")

# Partie Projets
st.header("Projets")



# Exemple de données pour row1 et row2
row1 = [st, st]
row2 = [st, st]
# Exemple de données pour les projets
projects = [
    {"image": "https://www.datascienceportfol.io/static/profile_pics/pr0_5F14FFB2BE1A3FA859D3.jpg", "title": "Projet 1", "description": "Description du projet 1", "link": "https://example.com/1"},
    {"image": "https://via.placeholder.com/150", "title": "Projet 2", "description": "Description du projet 2", "link": "https://example.com/2"},
    {"image": "https://via.placeholder.com/150", "title": "Projet 3", "description": "Description du projet 3", "link": "https://example.com/3"},
    {"image": "https://via.placeholder.com/150", "title": "Projet 4", "description": "Description du projet 4", "link": "https://example.com/4"},
]

# Afficher les projets deux par deux
for i in range(0, len(projects), 2):
    cols = st.columns([1, 0.1, 1])  # Ajout d'une colonne vide pour l'écart
    for j, col in enumerate([cols[0], cols[2]]):  # Utilisation des colonnes 0 et 2 pour les projets
        if i + j < len(projects):
            project = projects[i + j]
            with col:
                st.markdown(
                    f"""
                    <div style='border: 1px solid #ddd; padding: 10px; border-radius: 5px;'>
                        <img src='{project["image"]}' style='width: 100%; border-radius: 5px;'/>
                        <h2 style='text-align: center;'>{project['title']}</h2>
                        <p style='text-align: center;'>{project['description']}</p>
                        <p style='text-align: center;'><a href='{project['link']}' target='_blank'>Read more</a></p>
                        <p style='text-align: center;'><img src='https://go-skill-icons.vercel.app/api/icons?i=java,kotlin,nodejs,figma&titles=true' alt='My Skills'/></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# Partie Me Contacter
st.header("Me Contacter")

linkedin_button = """
<a href="https://www.linkedin.com/in/votreprofil" target="_blank">
    <button style="
        background-color: #0077B5; 
        color: white; 
        padding: 15px 30px; 
        font-size: 20px; 
        border: none; 
        border-radius: 5px; 
        cursor: pointer;
        transition: transform 0.3s;
    " onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width: 25px; height: 25px; vertical-align: middle; margin-right: 10px;">
        LinkedIn
    </button>
</a>
"""

github_button = """
<a href="https://github.com/votreprofil" target="_blank">
    <button style="
        background-color: #333; 
        color: white; 
        padding: 15px 30px; 
        font-size: 20px; 
        border: none; 
        border-radius: 5px; 
        cursor: pointer;
        transition: transform 0.3s;
    " onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" style="width: 50px; height: 50px; vertical-align: middle; margin-right: 10px;">
        Check my github !
    </button>
</a>
"""



email_button = """
<a href="mailto:votremail@example.com" target="_blank">
    <button style="
        background-color: #28a745; 
        color: white; 
        padding: 15px 30px; 
        font-size: 20px; 
        border: none; 
        border-radius: 5px; 
        cursor: pointer;
        transition: transform 0.3s;
    " onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email" style="width: 50px; height: 50px; vertical-align: middle; margin-right: 10px;">
        Email Me
    </button>
</a>
"""

buttons_container = f"""
<div style="display: flex; gap: 20px;">
    {linkedin_button}
    {github_button}
    {email_button}
</div>
"""

st.markdown(buttons_container, unsafe_allow_html=True)