pipeline {
    agent any 
    stages {
        stage('Build pooled_server.py'){ 
            steps {
                sh'python3 pooled_server.py'
            }
        }
        stage('Test pooled_server.py'){ 
            steps {
                echo("hello world")
                sh'python3 test pooled_server.py'
            }
        }
        stage('Deploy pooled_server.py'){ 
            steps {
                sh'python deploy pooled_server.py'
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
