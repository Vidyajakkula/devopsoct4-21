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
                echo("hello world")
                sh 'test add_asset'
            }
        }
        stage('Deploy add_asset.py') { 
            steps {
                sh 'Test add_asset.py'
            }
        }
    }
}
