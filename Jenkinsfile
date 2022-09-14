pipeline {
    agent any 
    stages {
        stage('Build python3.py') { 
            steps {
                sh 'build python python3.py'
            }
        }
        stage('Test python3.py'){ 
            steps {
                sh 'test python3.py'
            }
        }
        stage('Deploy python3.py') { 
            steps {
                sh 'deploy python3.py'
            }
        }
    }
}
