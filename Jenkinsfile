pipeline {
    agent any 
    stages {
        stage('Build add_asset.py') { 
            steps {
                sh 'python build add_asset.py'
            }
        }
        stage('Test add_asset.py'){ 
            steps {
                echo("hello world")
                sh'python test add_asset'
            }
        }
        stage('Deploy add_asset.py') { 
            steps {
                sh 'Test deploy add_asset.py'
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
