# main.tf
provider "aws" {
  region  = "us-east-1" 
}
# main.tf
resource "aws_ecr_repository" "app_ecr_repo" {
  name = "app-repoo"
}