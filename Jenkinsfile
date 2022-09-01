pipeline {
    agent any 
    stages {
        stage('Build add_asset.py'){ 
            steps {
                sh'python3 build add_asset.py'
            }
        }
        stage('Test add_asset.py'){ 
            steps {
                echo("hello world")
                sh'python3 test add_asset.py'
            }
        }
        stage('Deploy add_asset.py'){ 
            steps {
                sh'python deploy add_asset.py'
            }
            post{
                success{
                    echo'Now Archiving...'
                    archiveArtifacts artifacts:
'**/target/*.war'
                }
            }
        }
    }
}
