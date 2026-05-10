variable "region" {
  description = "GCP region"
  type        = string
  default     = "europe-west1"
}

variable "repository_name" {
  description = "Artifact Registry repository name"
  type        = string
  default     = "streamlit"
}

variable "image_name" {
  description = "Docker image name"
  type        = string
  default     = "streamlit-portfolio"
}

variable "image_tag" {
  description = "Tag de l'image Docker à déployer"
  type        = string
}

variable "slack_secret_name" {
  description = "Nom du secret Secret Manager contenant le Slack webhook URL"
  type        = string
  default     = "slack-webhook-url"
}

variable "custom_domain" {
  description = "Nom de domaine custom à mapper sur Cloud Run prod"
  type        = string
  default     = "francoislenne.io"
}
