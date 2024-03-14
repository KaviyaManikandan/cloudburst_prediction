# Cloudburst Prediction Project Setup

Welcome to the Cloudburst Prediction project! This guide will walk you through the setup process to deploy your prediction model on AWS using Terraform.


## Prerequisites

Before you begin, make sure you have the following:

- An AWS account
- AWS CLI installed and configured
- Terraform installed
- Basic knowledge of AWS services like EC2, ECS, and ALB

## Setup Instructions

1. **Clone the Repository:**
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/your-username/cloudprediction.git
     cd cloudburst_prediction
     ```

2. **AWS Credentials:**
   - Make sure your AWS credentials are configured either through AWS CLI or environment variables.

3. **Terraform Configuration:**
   - Navigate to the `terraform_code` directory:
     ```bash
     cd terraform_code
     ```
   - Update the '.tf' files with your desired configurations such as region, instance type, etc.

4. **Initialize Terraform:**
   - Run the following command to initialize Terraform:
     ```bash
     terraform init
     ```

5. **Plan Deployment:**
   - Generate an execution plan to review what Terraform will do:
     ```bash
     terraform plan
     ```

6. **Apply Changes:**
   - If the plan looks good, apply the changes to provision the infrastructure:
     ```bash
     terraform apply -auto-approve
     ```

7. **Access the Application:**
   - Once Terraform has finished provisioning, you will receive the URL of the load balancer. Access this URL in your web browser to view the deployed application.

8. **Cleanup:**
   - To destroy the infrastructure and avoid additional costs, run:
     ```bash
     terraform destroy -auto-approve
     ```

## Contributing

If you would like to contribute to this project, please follow the standard GitHub workflow:
- Fork the repository
- Make your changes
- Submit a pull request

## Issues and Feedback

If you encounter any issues or have feedback, please open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

Happy predicting!
