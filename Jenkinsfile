pipeline {
    agent any 
    stages {
        stage('Build add_asset.py') { 
            steps {
                sh 'python build add_asset.py'
            }
        }
        stage('Test add_asset.py') 
            steps {
                echo("hello world")
                sh 'pythoon test add_asset'
            }
        }
        stage('Deploy add_asset.py') { 
            steps {
                sh 'python Test add_asset.py'
            }
        }
    }
}
