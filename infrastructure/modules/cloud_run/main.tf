data "google_client_config" "current" {}
data "google_project" "current" {}

locals {
  project_id = data.google_client_config.current.project
}

resource "google_cloud_run_v2_service" "service" {
  name     = var.service_name
  location = var.region

  # Seule la prod est ouverte sur internet
  ingress = var.is_public ? "INGRESS_TRAFFIC_ALL" : "INGRESS_TRAFFIC_INTERNAL_ONLY"

  template {
    containers {
      image = var.image

      ports {
        container_port = 8080
      }

      env {
        name  = "ENV"
        value = var.environment
      }

      env {
        name = "SLACK_WEBHOOK_URL"
        value_source {
          secret_key_ref {
            secret  = var.slack_secret_name
            version = "latest"
          }
        }
      }

      resources {
        limits = {
          cpu    = var.cpu
          memory = var.memory
        }
      }
    }

    scaling {
      min_instance_count = var.min_instances
      max_instance_count = var.max_instances
    }
  }
}

# Autoriser Cloud Run à lire le secret (compte de service Compute par défaut)
resource "google_secret_manager_secret_iam_member" "cloud_run_slack" {
  secret_id = var.slack_secret_name
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${data.google_project.current.number}-compute@developer.gserviceaccount.com"
}

# IAM public uniquement pour la prod
resource "google_cloud_run_v2_service_iam_member" "public" {
  count    = var.is_public ? 1 : 0
  project  = local.project_id
  location = var.region
  name     = google_cloud_run_v2_service.service.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
