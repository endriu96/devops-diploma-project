pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/endriu96/devops-diploma-project.git'
            }
        }

        stage('List Files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }
    }
}
