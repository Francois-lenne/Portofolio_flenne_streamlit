import streamlit as st
from PIL import Image
import os
from utils.helpers import is_valid_email, send_slack_message


st.set_page_config(
    page_title="François Lenne — Data Engineer",
    page_icon=":page_with_curl:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

current_repo = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(current_repo, "assets")

st.logo(f"{assets_dir}/linkedin-svg.svg", link='https://www.linkedin.com/in/fran%C3%A7ois-lenne-5975b9174/')

st.markdown("""
<style>
/* Hide Streamlit default top padding */
.block-container { padding-top: 2rem; }

/* Hero */
.hero {
    display: flex;
    align-items: center;
    gap: 48px;
    padding: 32px 0 40px;
}
.hero-avatar {
    border-radius: 50%;
    width: 200px;
    height: 200px;
    object-fit: cover;
    flex-shrink: 0;
}
.hero-text h1 {
    font-size: 2.2rem;
    font-weight: 700;
    margin: 0 0 4px;
}
.hero-role {
    font-size: 1.05rem;
    opacity: 0.55;
    margin: 0 0 16px;
    font-weight: 400;
}
.hero-bio {
    font-size: 1rem;
    line-height: 1.65;
    max-width: 540px;
    margin: 0 0 20px;
    opacity: 0.85;
}
.hero-links {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}
.hero-links a img { display: block; }

/* Project card body */
.card-body { padding: 6px 2px 4px; }
.card-title {
    font-size: 1rem;
    font-weight: 600;
    margin: 0 0 6px;
}
.card-desc {
    font-size: 0.87rem;
    opacity: 0.65;
    line-height: 1.5;
    margin: 0 0 10px;
}
.card-link {
    font-size: 0.85rem;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)


# ── Hero ─────────────────────────────────────────────────────────────────────

avatar_url = "https://avatars.githubusercontent.com/u/114836746?v=4"

st.markdown(f"""
<div class="hero">
    <img class="hero-avatar" src="{avatar_url}" alt="François Lenne">
    <div class="hero-text">
        <h1>François Lenne</h1>
        <p class="hero-role">Data Engineer</p>
        <p class="hero-bio">
            French data engineer building reliable pipelines and data platforms.
            I work across GCP, Snowflake and AWS — and I enjoy automating the boring parts.
        </p>
        <div class="hero-links">
            <a href="https://www.linkedin.com/in/fran%C3%A7ois-lenne-5975b9174/" target="_blank">
                <img src="https://go-skill-icons.vercel.app/api/icons?i=linkedin" height="30">
            </a>
            <a href="https://github.com/Francois-lenne" target="_blank">
                <img src="https://go-skill-icons.vercel.app/api/icons?i=github" height="30">
            </a>
        </div>
        <img src="https://go-skill-icons.vercel.app/api/icons?i=py,pandas,bash,git,gcp,snowflake,aws,github,githubactions,pbi" alt="tech stack">
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()


# ── Projects ──────────────────────────────────────────────────────────────────

st.header("Projects")
st.write("")

projects = [
    {
        "image": f"{assets_dir}/playsation_illus.jpg",
        "title": "PlayStation data → BigQuery",
        "description": "Retrieving game time and play data from my PlayStation account and ingesting it into BigQuery.",
        "link": "https://github.com/Francois-lenne/play-bq-gcp",
        "icon": "https://go-skill-icons.vercel.app/api/icons?i=python,bigquery,googlecloud&titles=true",
    },
    {
        "image": f"{assets_dir}/biogaz.jpg",
        "title": "French Biomethane production → Snowflake",
        "description": "Automated CSV ingestion of French biomethane production data into Snowflake via GCP.",
        "link": "https://github.com/Francois-lenne/biomethane",
        "icon": "https://go-skill-icons.vercel.app/api/icons?i=python,googlecloud,snowflake&titles=true",
    },
    {
        "image": f"{assets_dir}/github-data.jpg",
        "title": "GitHub account data → Redshift",
        "description": "Extracting GitHub account metrics and loading them into Redshift for analysis.",
        "link": "https://github.com/Francois-lenne/data_github",
        "icon": "https://go-skill-icons.vercel.app/api/icons?i=python,redshift,aws&titles=true",
    },
    {
        "image": f"{assets_dir}/speedtest.jpg",
        "title": "Internet speed monitoring",
        "description": "Continuous monitoring of home internet speed stored in PostgreSQL and visualised.",
        "link": "https://github.com/Francois-lenne/speedtest_viz",
        "icon": "https://go-skill-icons.vercel.app/api/icons?i=python,postgresql,bash&titles=true",
    },
    {
        "image": f"{assets_dir}/portofolio.jpg",
        "title": "This portfolio",
        "description": "Building and deploying this portfolio with Streamlit on Cloud Run.",
        "link": "https://github.com/Francois-lenne/Portofolio_flenne_streamlit",
        "icon": "https://go-skill-icons.vercel.app/api/icons?i=python,streamlit&titles=true",
    },
    {
        "image": f"{assets_dir}/vehicle_electric.jpg",
        "title": "US electric vehicle fleet",
        "description": "Monitoring the electric vehicle fleet across the United States with Microsoft Fabric and Spark.",
        "link": "https://github.com/Francois-lenne/eletric_vehicle_usa",
        "icon": "https://go-skill-icons.vercel.app/api/icons?i=py,fabric,spark&titles=true",
    },
]

for i in range(0, len(projects), 3):
    cols = st.columns(3, gap="medium")
    for j, col in enumerate(cols):
        if i + j >= len(projects):
            break
        p = projects[i + j]
        with col:
            with st.container(border=True):
                st.image(Image.open(p["image"]), use_container_width=True)
                st.markdown(f"""
                <div class="card-body">
                    <p class="card-title">{p['title']}</p>
                    <p class="card-desc">{p['description']}</p>
                    <a class="card-link" href="{p['link']}" target="_blank">View on GitHub →</a>
                    <br><br>
                    <img src="{p['icon']}" alt="stack" style="max-height:28px;">
                </div>
                """, unsafe_allow_html=True)

st.divider()


# ── Contact ───────────────────────────────────────────────────────────────────

st.header("Contact me")
st.write("")

with st.form(key='contact_form'):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
    with col2:
        email = st.text_input("Email address")
    subject = st.text_input("Subject")
    message = st.text_area("Message", height=140)
    submit = st.form_submit_button("Send message", use_container_width=True)

if submit:
    errors = []
    if not name:
        errors.append("Please enter your name.")
    if not email:
        errors.append("Please enter your email address.")
    elif not is_valid_email(email):
        errors.append("Please enter a valid email address.")
    if not subject:
        errors.append("Please enter a subject.")
    if not message:
        errors.append("Please enter a message.")

    if errors:
        for err in errors:
            st.error(err)
    else:
        slack_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        try:
            if send_slack_message(slack_message):
                st.success("Message sent! I'll get back to you as soon as possible.")
            else:
                st.error("Something went wrong. Please try again later.")
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
