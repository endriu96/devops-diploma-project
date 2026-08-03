pipeline {
    agent {
        label 'docker-agent'
        }

    stages {

        stage('List Files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Python Check') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Tests') {
   
         steps {
            sh 'python3 -m venv venv'
            sh './venv/bin/pip install -r requirements.txt'
            sh './venv/bin/pytest tests'
             }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t devops-diploma-app:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop devops-app || true'
                sh 'docker rm devops-app || true'
                sh 'docker run -d --name devops-app -p 5000:5000 devops-diploma-app:latest'
                }
        }
    }
}