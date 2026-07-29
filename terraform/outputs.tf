output "instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.devops_server.id
}

output "public_ip" {
  description = "EC2 Public IP"
  value       = aws_instance.devops_server.public_ip
}

output "security_group_id" {
  description = "Security Group ID"
  value       = aws_security_group.devops_sg.id
}
