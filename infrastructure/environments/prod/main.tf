terraform {
  required_version = ">= 1.5"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

data "google_client_config" "current" {}

provider "google" {
  region = var.region
  # project_id résolu automatiquement depuis le SDK gcloud
}

# ── Artifact Registry (partagé entre tous les environnements) ─────────────────

resource "google_artifact_registry_repository" "portfolio" {
  location      = var.region
  repository_id = var.repository_name
  format        = "DOCKER"
  description   = "Docker images du portfolio (partagé dev/qual/prod)"
}

# ── Cloud Run prod ─────────────────────────────────────────────────────────────

module "cloud_run" {
  source = "../../modules/cloud_run"

  region            = var.region
  service_name      = "flenne-portfolio-prod"
  image             = "${var.region}-docker.pkg.dev/${data.google_client_config.current.project}/${var.repository_name}/${var.image_name}:${var.image_tag}"
  environment       = "prod"
  slack_secret_name = var.slack_secret_name
  is_public         = true
  cpu               = "1"
  memory            = "512Mi"
  min_instances     = 0
  max_instances     = 3

  depends_on = [google_artifact_registry_repository.portfolio]
}
