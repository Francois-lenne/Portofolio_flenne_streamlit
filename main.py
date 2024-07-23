import streamlit as st
from streamlit_space import space

# Configuration de la page
st.set_page_config(page_title="Portfolio Francois Lenne", page_icon=":page_with_curl:", layout="wide")


space(lines = 4)

# Titre au milieu de la page

st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <h1> Welcome to my portfolio </h1>
    </div>
    """,
    unsafe_allow_html=True
)


# URL de l'image
image_url = "https://avatars.githubusercontent.com/u/114836746?v=4"

# CSS pour l'image ronde et le conteneur
st.markdown(
    """
    <style>
    .round-img {
        border-radius: 50%;
        width: 400px; /* Ajustez la taille selon vos besoins */
        height: 400px; /* Ajustez la taille selon vos besoins */
        object-fit: cover;
    }
    .container {
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .text-container {
        display: flex;
        flex-direction: column;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Conteneur principal
st.markdown(
    f"""
    <div class="container">
        <img src="{image_url}" class="round-img">
        <div class="text-container">
            <h1>Francois Lenne</h1>
            <p>Bonjour, je suis Francois Lenne, un Data Engineer passionné par la manipulation et l'analyse des données. 
            Je suis spécialisé dans la création de pipelines de données robustes et évolutifs.</p>
            <p align="center">
              <a href="https://go-skill-icons.vercel.app/">
                <img src="https://go-skill-icons.vercel.app/api/icons?i=py,js,pandas,r,bash,git,gcp,snowflake,github,githubactions,pbi,vscode,githubcopilot" />
              </a>
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


space(lines = 8)


st.header("Skills")

st.subheader("Soft Skills")

# CSS pour centrer le conteneur principal
st.markdown(
    """
    <style>
    .center-container {
        display: flex;
        justify-content: center;
    }
    .center-content {
        width: 100%;
        max-width: 800px; /* Ajustez cette largeur selon vos besoins */
        display: grid;
        grid-template-columns: repeat(3, 1fr); /* Trois colonnes */
        gap: 20px; /* Ajustez cet écart selon vos besoins */
        justify-items: center; /* Centre les éléments horizontalement */
        align-items: center; /* Centre les éléments verticalement */
    }
    .grid-item {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Conteneur principal centré
st.markdown('<div class="center-container"><div class="center-content">', unsafe_allow_html=True)

skills = ["Curious", "team player", "adaptability", "problem solver", "Relational Skills", "Organize"]
image_path = ["C:/Users/flenne/Portofolio_flenne_streamlit/assets/curious.png", "C:/Users/flenne/Portofolio_flenne_streamlit/assets/team-player.png", "C:/Users/flenne/Portofolio_flenne_streamlit/assets/adaptability.png", "C:/Users/flenne/Portofolio_flenne_streamlit/assets/problem-solver.png", "C:/Users/flenne/Portofolio_flenne_streamlit/assets/communication.png", "C:/Users/flenne/Portofolio_flenne_streamlit/assets/organize.png"]

# Affichage des skills en trois colonnes
for i in range(0, len(skills), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(skills):
            with col:
                st.image(image_path[i+j], width=160)
                st.markdown(f"<p style='font-size: 30px; font-weight: bold;'>{skills[i + j]}</p>", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

st.subheader("Hard Skills")




# CSS pour centrer le conteneur principal
st.markdown(
    """
    <style>
    .center-container {
        display: flex;
        justify-content: center;
    }
    .center-content {
        width: 100%;
        max-width: 800px; /* Ajustez cette largeur selon vos besoins */
        display: grid;
        grid-template-columns: repeat(3, 1fr); /* Trois colonnes */
        gap: 20px; /* Ajustez cet écart selon vos besoins */
        justify-items: center; /* Centre les éléments horizontalement */
        align-items: center; /* Centre les éléments verticalement */
    }
    .grid-item {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Conteneur principal centré
st.markdown('<div class="center-container"><div class="center-content">', unsafe_allow_html=True)

skills = ["Quering data", "ETL", "data modeling", "data quality", "write code", "cloud computing"]
image_path = ["C:/Users/flenne/Portofolio_flenne_streamlit/assets/interact-data.png", "C:/Users/flenne/Portofolio_flenne_streamlit/assets/etl.png", "C:/Users/flenne/Portofolio_flenne_streamlit/assets/data-modeling.png", "C:/Users/flenne/Portofolio_flenne_streamlit/assets/quality.png", "C:/Users/flenne/Portofolio_flenne_streamlit/assets/code.png", "C:/Users/flenne/Portofolio_flenne_streamlit/assets/cloud-computing.png"]

# Affichage des skills en trois colonnes
for i in range(0, len(skills), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(skills):
            with col:
                st.image(image_path[i+j], width=160)
                st.markdown(f"<p style='font-size: 30px; font-weight: bold;'>{skills[i + j]}</p>", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)



# Partie Projets
st.header("Projets")


description_play = "This project is about retriving data from my playstation account (time and game play) and store it in Bigquery"


description_biomethan = "This project is about retriving data from the french production of Biomethan and store it in Snowflake using GCP and snowflake tools to ingest csv automatically"

description_github = "This project is about retriving data from the github account and store it in Redshift"


Speedtest = "This project is about monitoring the speedtest of my internet connection and store it in postgresql"


# Exemple de données pour les projets
projects = [
    {"image": "C:/Users/flenne/Portofolio_flenne_streamlit/assets/playstation.jpg", "title": "Retriving Playsation data in Bigquery", "description": description_play, "link": "https://github.com/Francois-lenne/play-bq-gcp"},
    {"image": "C:/Users/flenne/Portofolio_flenne_streamlit/assets/biomethane.jpg", "title": "Retriving the french production of Biomethan in Snowflake", "description": description_biomethan, "link": "https://github.com/Francois-lenne/biomethane"},
    {"image": "C:/Users/flenne/Portofolio_flenne_streamlit/assets/github.png", "title": "Retrieve the Github data account in Redshift", "description": description_github, "link": "https://github.com/Francois-lenne/data_github"},
    {"image": "C:/Users/flenne/Portofolio_flenne_streamlit/assets/speedtest.jpg", "title": "Speedtest monitoring", "description": Speedtest, "link": "https://github.com/Francois-lenne/speedtest_viz"},
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
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <style>
                    .project-image {{
                                        max-height: 100px;  /* Définir la hauteur maximale souhaitée */
                                        width: auto;
                                        display: block;
                                        margin-left: auto;
                                        margin-right: auto;
                                    }}
                                    </style>
                                    """,
                                    unsafe_allow_html=True
                    )
                                
                st.image(project["image"], use_column_width=True, caption=project['title'], output_format='auto')

                st.markdown(
                    f"""
                        <h2 style='text-align: center;'>{project['title']}</h2>
                        <p style='text-align: center;'>{project['description']}</p>
                        <p style='text-align: center;'><a href='{project['link']}' target='_blank'>Github</a></p>
                        <p style='text-align: center;'><img src='https://go-skill-icons.vercel.app/api/icons?i=java,kotlin,nodejs,figma&titles=true' alt='My Skills'/></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# Partie Me Contacter
st.header("Me Contacter")

linkedin_button = """
<a href="https://www.linkedin.com/in/fran%C3%A7ois-lenne-5975b9174/" target="_blank">
    <button style="
        background-color: #f5987e; 
        color: white; 
        padding: 15px 30px; 
        font-size: 20px; 
        border: none; 
        border-radius: 5px; 
        cursor: pointer;
        transition: transform 0.3s;
    " onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="GitHub" style="width: 50px; height: 50px; vertical-align: middle; margin-right: 10px;">
        Add me on linkedin !
    </button>
</a>
"""

github_button = """
<a href="https://github.com/Francois-lenne" target="_blank">
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
<a href="mailto:francois.lenne@hotmail.fr" target="_blank">
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
<div style="display: flex; justify-content: center; gap: 60px;">
    {linkedin_button}
    {github_button}
    {email_button}
</div>
"""

st.markdown(buttons_container, unsafe_allow_html=True)