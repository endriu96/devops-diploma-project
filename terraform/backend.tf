terraform {
  backend "s3" {
    bucket = "jedrzej-devops-diploma-state-2026"
    key    = "terraform.tfstate"
    region = "eu-central-1"
  }
}