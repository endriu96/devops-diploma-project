pipeline {
    agent any

    stages {

        stage('List Files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Environment Info') {
            steps {
                sh 'whoami'
                sh 'hostname'
                sh 'env | sort'
            }
        }
    }
}