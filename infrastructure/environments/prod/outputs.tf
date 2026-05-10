output "cloud_run_url" {
  description = "URL publique du service Cloud Run prod"
  value       = module.cloud_run.service_url
}

output "artifact_registry_url" {
  description = "URL du dépôt Artifact Registry"
  value       = "${var.region}-docker.pkg.dev/${data.google_client_config.current.project}/${var.repository_name}"
}

output "domain_mapping_records" {
  description = "Enregistrements DNS à configurer dans Squarespace"
  value       = google_cloud_run_domain_mapping.prod.status[0].resource_records
}
