pipeline {
    agent any

    stages {
        stage ('build') {
            steps{
                sh 'docker-compose -f /var/lib/jenkins/workspace/DB_Games_dev/docker-compose.yml up --build -d'
                echo 'Build Stage Completed'
            }
        }

        stage ('test') {
            steps{
                echo 'Test stage executed.'
                sh 'python3  -m unittest webapp/test_app.py'
            }
        }

        stage ('deploy') {
            steps{
                sh 'docker-compose -f /var/lib/jenkins/workspace/DB_Games_dev/docker-compose.yml down'
                echo 'Deploy stage executed.'

            }
        }
    }
}