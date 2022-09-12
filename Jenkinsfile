pipeline {
    agent any 
    stages {
        stage('Build list_asset.py'){ 
            steps {
                sh'python3 list_asset.py'
            }
        }
        stage('Test list_asset.py'){ 
            steps {
                echo("hello world")
                sh'python3 test list_asset.py'
            }
        }
        stage('Deploy list_asset.py'){ 
            steps {
                sh'python deploy list_asset.py'
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
