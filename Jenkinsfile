pipeline {
    agent any

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
                sh 'pip3 install -r requirements.txt'
                sh 'pytest tests'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t devops-diploma-app:latest .'
            }
        }
    }
}