# DevOps Diploma Project

## Author

Jędrzej Świerczyński

## Project Description

The project presents a complete DevOps environment built using modern automation, containerization, monitoring and orchestration tools.

The main objective was to design and implement a CI/CD platform that allows automatic application testing, building, deployment and monitoring in a cloud environment.

## Technologies

- Git
- GitHub
- Terraform
- AWS EC2
- Ubuntu Linux
- Docker
- Jenkins
- Ansible
- Prometheus
- Grafana
- Alertmanager
- Kubernetes
- Python
- Flask

## Architecture

```text
Git Push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Webhook
    │
    ▼
Jenkins Pipeline (CI/CD)
    │
    ├── Automated Tests
    ├── Docker Build
    └── Docker Deployment
    │
    ▼
Docker Engine (AWS EC2)
    │
    ▼
Flask Application
    │
    ├── Prometheus
    ├── Grafana
    └── Alertmanager

Kubernetes
    └── Application Orchestration and Self-Healing