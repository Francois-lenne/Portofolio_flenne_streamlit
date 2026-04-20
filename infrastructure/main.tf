terraform {
  required_version = ">= 1.5"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# ── Artifact Registry ─────────────────────────────────────────────────────────

resource "google_artifact_registry_repository" "portfolio" {
  location      = var.region
  repository_id = var.repository_name
  format        = "DOCKER"
  description   = "Docker images for the portfolio"
}

# ── Cloud Run ─────────────────────────────────────────────────────────────────

resource "google_cloud_run_v2_service" "portfolio" {
  name     = var.service_name
  location = var.region

  template {
    containers {
      image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.repository_name}/${var.image_name}:latest"

      ports {
        container_port = 8080
      }

      env {
        name  = "SLACK_WEBHOOK_URL"
        value = var.slack_webhook_url
      }

      resources {
        limits = {
          cpu    = "1"
          memory = "512Mi"
        }
      }
    }

    scaling {
      min_instance_count = 0
      max_instance_count = 3
    }
  }

  depends_on = [google_artifact_registry_repository.portfolio]
}

# Allow public access (unauthenticated)
resource "google_cloud_run_v2_service_iam_member" "public" {
  project  = var.project_id
  location = var.region
  name     = google_cloud_run_v2_service.portfolio.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
