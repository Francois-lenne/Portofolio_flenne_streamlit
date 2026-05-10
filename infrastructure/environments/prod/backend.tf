terraform {
  backend "gcs" {
    bucket = "flenne-portfolio-tfstate"
    prefix = "env/prod"
  }
}
