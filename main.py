import streamlit as st
from streamlit_space import space
import requests
from PIL import Image
import os
import re
import json


# define function 

# email validation

def is_valid_email(email):
    # Regex pour valider une adresse email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


# send slack message

def send_slack_message(message):
    """
    Send a plain text message to Slack using a webhook URL.
    
    :param message: The message to send
    :return: True if successful, False otherwise
    """
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    headers = {'Content-Type': 'application/json'}
    data = {'text': message}
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
        if response.status_code != 200:
            print(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")
            return False
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

# Configuration de la page


st.set_page_config(
    page_title="Portfolio Francois Lenne",
    page_icon=":page_with_curl:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



current_repo = os.path.dirname(os.path.abspath(__file__))



st.logo(f"{current_repo}/assets/linkedin-svg.svg", link= 'https://www.linkedin.com/in/fran%C3%A7ois-lenne-5975b9174/' )


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
            <p> Hi, i'am a french data engineer  Don't hesitate to take a look of my projects or my skills and contact me if you want to reach me ! </p>
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
image_path = [
    f"{current_repo}/assets/curious.png",
    f"{current_repo}/assets/team-player.png",
    f"{current_repo}/assets/adaptability.png",
    f"{current_repo}/assets/problem-solver.png",
    f"{current_repo}/assets/communication.png",
    f"{current_repo}/assets/organize.png"
]

# Affichage des skills en trois colonnes
for i in range(0, len(skills), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(skills):
            with col:
                st.image(image_path[i+j], width=160)
                space(lines = 1)
                st.markdown(f"<p style='font-size: 30px; font-weight: bold;'>{skills[i + j]}</p>", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)


space(lines = 5)

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
image_path = [
    f"{current_repo}/assets/interact-data.png",
    f"{current_repo}/assets/etl.png",
    f"{current_repo}/assets/data-modeling.png",
    f"{current_repo}/assets/quality.png",
    f"{current_repo}/assets/code.png",
    f"{current_repo}/assets/cloud-computing.png"
]


# Affichage des skills en trois colonnes
for i in range(0, len(skills), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(skills):
            with col:
                st.image(image_path[i+j], width=160)
                st.markdown(f"<p style='font-size: 30px; font-weight: bold;'>{skills[i + j]}</p>", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)



space(lines = 5)


# Partie Projets
st.header("Projects")

space(lines = 3)

# variable contenant la description des projets

description_play = "This project is about retriving data from my playstation account (time and game play) and store it in Bigquery"


description_biomethan = "This project is about retriving data from the french production of Biomethan and store it in Snowflake using GCP and snowflake tools to ingest csv automatically"

description_github = "This project is about retriving data from the github account and store it in Redshift"


Speedtest = "This project is about monitoring the speedtest of my internet connection and store it in postgresql"

portofolio = "This project is about creating my portofolio using streamlit"


vehicles = "This project is about monitoring the electric vehicle fleet in the us"


# Exemple de données pour les projets
projects = [
    {"image": f"{current_repo}/assets/playsation_illus.jpg", "title": "Retriving Playsation data in Bigquery", "description": description_play, "link": "https://github.com/Francois-lenne/play-bq-gcp", "icon": "https://go-skill-icons.vercel.app/api/icons?i=python,bigquery,googlecloud&titles=true"},
    {"image": f"{current_repo}/assets/biogaz.jpg", "title": "Retriving the french production of Biomethan in Snowflake", "description": description_biomethan, "link": "https://github.com/Francois-lenne/biomethane", "icon": "https://go-skill-icons.vercel.app/api/icons?i=python,googlecloud,snowflake&titles=true"},
    {"image": f"{current_repo}/assets/github-data.jpg", "title": "Retrieve the Github data account in Redshift", "description": description_github, "link": "https://github.com/Francois-lenne/data_github", "icon": "https://go-skill-icons.vercel.app/api/icons?i=python,redshift,aws&titles=true"},
    {"image": f"{current_repo}/assets/speedtest.jpg", "title": "Speedtest monitoring", "description": Speedtest, "link": "https://github.com/Francois-lenne/speedtest_viz" , "icon": "https://go-skill-icons.vercel.app/api/icons?i=python,postgresql,bash&titles=true"},
    {"image": f"{current_repo}/assets/portofolio.jpg", "title": "My Portfolio", "description": portofolio, "link": "https://github.com/Francois-lenne/Portofolio_flenne_streamlit" , "icon": "https://go-skill-icons.vercel.app/api/icons?i=python,streamlit&titles=true"},
    {"image": f"{current_repo}/assets/vehicle_electric.jpg", "title": "Amaerica's electric vehicle fleet", "description": vehicles, "link": "https://github.com/Francois-lenne/eletric_vehicle_usa" , "icon": "https://go-skill-icons.vercel.app/api/icons?i=py,fabric,spark&titles=true"},
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
                                        max-height: 13px;  /* Définir la hauteur maximale souhaitée */
                                        width: auto;
                                        display: block;
                                        margin-left: auto;
                                        margin-right: auto;
                                    }}
                                    </style>
                                    """,
                                    unsafe_allow_html=True
                    )
                
                # Open the image
                image = Image.open(project["image"])

                # Display the image
                st.image(image, use_column_width=True, output_format='png')

                st.markdown(
                    f"""
                        <h2 style='text-align: center;'>{project['title']}</h2>
                        <p style='text-align: center;'>{project['description']}</p>
                        <p style='text-align: center;'><a href='{project['link']}' target='_blank'>Github</a></p>
                        <p style='text-align: center;'><img src='{project['icon']}'  alt='My Skills'/></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

space(lines = 5)

# Partie Me Contacter
st.header("Contact me")

space(lines = 3)

# Formulaire de contact
with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Your email adress") 
    subject = st.text_input("Subject")
    message = st.text_area("Message")
    
    submit_button = st.form_submit_button(label='Send')

if submit_button:
    if len(name) == 0:
        st.error("Enter your name.")
    if len(email) == 0:
        st.error("Enter an email adress.")
    elif not is_valid_email(email):
        st.error("Enter a valid adress email")
    if len(subject) == 0:
        st.error("Enter the subject of your message.")
    if len(message) == 0:
        st.error("Enter a message.")
    else:
        # Envoyer le message à Slack
        slack_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        
        try:
            success = send_slack_message(slack_message)
            if success:
                st.success("Your message is send ! I will contact you as soon as possible.")
            else:
                st.error("theres a problem with the message. Please try again later.")
        except Exception as e:
            st.error(f"theres a problem with the message. {str(e)}. please try again later.")


