pipeline {
    agent any 
    stages {
        stage('Build add_asset.py') { 
            steps {
                sh 'build add_asset.py'
            }
        }
        stage('Test add_asset.py') 
            steps {
            }
        }
        stage('Deploy add_asset.py') { 
            steps {
                sh 'Test add_asset.py'
            }
        }
    }
}
