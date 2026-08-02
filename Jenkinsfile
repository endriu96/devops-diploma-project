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

        stage('Docker Build') {
            steps {
                sh 'docker build -t devops-diploma-app:latest .'
            }
        }
    }
}