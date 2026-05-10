output "cloud_run_url" {
  description = "URL interne du service Cloud Run dev (non exposé publiquement)"
  value       = module.cloud_run.service_url
}
