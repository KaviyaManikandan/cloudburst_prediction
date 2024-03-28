resource "aws_ecs_task_definition" "app_task" {
  family                   = "app-first-taskk" # Name your task
  container_definitions    = <<DEFINITION
  [
    {
      "name": "app-first-taskk",
      "image": "${aws_ecr_repository.app_ecr_repo.repository_url}",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 5000,
          "hostPort": 5000
        }
      ],
      "memory": 512,
      "cpu": 256
    }
  ]
  DEFINITION
  requires_compatibilities = ["FARGATE"] 
  network_mode             = "awsvpc"   
  memory                   = 512        
  cpu                      = 256         
  execution_role_arn       = "arn:aws:ecs:us-east-1:590183704936:task-definition/app-first-taskk:1"
}

resource "aws_ecs_service" "app_service" {
  name            = "app-first-servicee"     # Name the service
  cluster         = "${aws_ecs_cluster.my_cluster.id}"   
  task_definition = "${aws_ecs_task_definition.app_task.arn}" 
  launch_type     = "FARGATE"
  desired_count   = 3 # Set up the number of containers to 3

  load_balancer {
    target_group_arn = "${aws_lb_target_group.target_group.arn}" 
    container_name   = "${aws_ecs_task_definition.app_task.family}"
    container_port   = 5000 # Specify the container port
  }

  network_configuration {
    subnets          = ["${aws_default_subnet.default_subnet_a.id}", "${aws_default_subnet.default_subnet_b.id}"]
    assign_public_ip = true     # Provide the containers with public IPs
    security_groups  = ["${aws_security_group.service_security_group.id}"] # Set up the security group
  }
}

output "app_url" {
  value = aws_alb.application_load_balancer.dns_name
}
