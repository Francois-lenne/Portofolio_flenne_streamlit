output "cloud_run_url" {
  description = "URL publique du service Cloud Run prod"
  value       = module.cloud_run.service_url
}

output "artifact_registry_url" {
  description = "URL du dépôt Artifact Registry"
  value       = "${var.region}-docker.pkg.dev/${data.google_client_config.current.project}/${var.repository_name}"
}
