pipeline {
    agent any

    stages {
        stage ('build') {
            steps{
                sh 'docker-compose -f /var/lib/jenkins/workspace/DB_Games2/docker-compose.yml up --build -d'
                echo 'Build Stage Completed'
            }
        }

        stage ('test') {
            steps{
                echo 'Test stage executed.'
                sh 'pip install flask'
                sh 'python3  -m unittest webapp/test_app.py'
            }
        }

        stage ('deploy') {
            steps{
                echo 'Deploy stage executed.'

            }
        }
    }
}