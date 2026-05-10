variable "region" {
  description = "GCP region"
  type        = string
  default     = "europe-west1"
}

variable "service_name" {
  description = "Cloud Run service name"
  type        = string
}

variable "image" {
  description = "Docker image URL (full path with tag)"
  type        = string
}

variable "environment" {
  description = "Nom de l'environnement (dev, qual, prod)"
  type        = string
}

variable "slack_secret_name" {
  description = "Nom du secret Secret Manager contenant le Slack webhook URL"
  type        = string
  default     = "slack-webhook-url"
}

variable "is_public" {
  description = "Ouvre le service sur internet (true = prod uniquement)"
  type        = bool
  default     = false
}

variable "cpu" {
  description = "CPU limit"
  type        = string
  default     = "1"
}

variable "memory" {
  description = "Memory limit"
  type        = string
  default     = "512Mi"
}

variable "min_instances" {
  description = "Nombre minimum d'instances (0 = scale to zero)"
  type        = number
  default     = 0
}

variable "max_instances" {
  description = "Nombre maximum d'instances"
  type        = number
  default     = 3
}
