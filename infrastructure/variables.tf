variable "project_id" {
  description = "GCP project ID"
  type        = string
}

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

variable "service_name" {
  description = "Cloud Run service name"
  type        = string
  default     = "flenne-portfolio"
}

variable "slack_webhook_url" {
  description = "Slack webhook URL for contact form"
  type        = string
  sensitive   = true
  default     = ""
}
