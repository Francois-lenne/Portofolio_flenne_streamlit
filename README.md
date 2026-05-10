# François Lenne — Portfolio

Personal portfolio built with Streamlit and deployed on GCP Cloud Run.

<p align="center">
  <a href="https://go-skill-icons.vercel.app/">
    <img src="https://go-skill-icons.vercel.app/api/icons?i=py,streamlit,gcp,docker,terraform" />
  </a>
</p>

## Overview

A single-page Streamlit app that presents my data engineering projects and includes a contact form that forwards messages to a Slack channel via webhook.

## Features

- **Hero section** — bio, tech stack badges, links to LinkedIn & GitHub
- **Project cards** — 6 data engineering projects with images, descriptions, and GitHub links
- **Contact form** — validates input and sends messages to Slack via incoming webhook

## Stack

| Layer | Technology |
|---|---|
| App | Python 3.11, Streamlit |
| Containerisation | Docker, uv |
| Registry | GCP Artifact Registry |
| Hosting | GCP Cloud Run |
| CI/CD | Cloud Build |
| Infrastructure | Terraform |
| Notifications | Slack incoming webhook |

## Architecture

```
User → Cloud Run (Streamlit app)
              ↓
         Slack Webhook  (contact form)
```

The Docker image is built and pushed to Artifact Registry by Cloud Build, then deployed to Cloud Run. Infrastructure (Artifact Registry repository, Cloud Run service, IAM) is managed with Terraform.

## Project structure

```
.
├── src/
│   ├── main.py          # Streamlit app
│   ├── assets/          # Images and icons
│   └── utils/
│       └── helpers.py   # Email validation, Slack webhook helper
├── infrastructure/
│   ├── main.tf          # Artifact Registry + Cloud Run + IAM
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars.example
├── dockerfile
├── cloudbuild.yaml
└── pyproject.toml
```

## Local setup

**Prerequisites:** Python 3.11+, [uv](https://github.com/astral-sh/uv)

```bash
# Install dependencies
uv sync

# Run the app (no Slack notifications without the webhook)
uv run streamlit run src/main.py
```

To enable the contact form, set the environment variable:

```bash
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."
```

## Deploy

### Infrastructure (first time)

```bash
cd infrastructure
cp terraform.tfvars.example terraform.tfvars
# Fill in your values
terraform init
terraform apply
```

### CI/CD

Cloud Build is triggered on push. It builds the Docker image, pushes it to Artifact Registry, and deploys to Cloud Run automatically via `cloudbuild.yaml`.

### Manual deploy

```bash
docker build -t <region>-docker.pkg.dev/<project>/<repo>/streamlit-portfolio:latest .
docker push <region>-docker.pkg.dev/<project>/<repo>/streamlit-portfolio:latest
gcloud run deploy flenne-portfolio --image <image> --region europe-west1
```
