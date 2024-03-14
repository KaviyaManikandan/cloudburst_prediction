provider "aws" {
  region  = "us-east-1" 
}

resource "aws_ecr_repository" "app_ecr_repo" {
  name = "app-repoo"
}
