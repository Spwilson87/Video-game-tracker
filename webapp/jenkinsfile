pipeline {
    agent any

    stages {
        stage ('build') {
            steps{
                sh 'docker-compose -f /var/lib/jenkins/workspace/finally_main/webapp/docker-compose.yml up --build -d'
            }
        }

        stage ('test') {
            steps{
                echo 'Test stage executed.'
                sh 'docker exec -it dbsql bash -l'
                sh 'mysql -u root -proot'
                sh 'use database_games'
                sh 'show tables;'
                sh 'describe Games;'
            }
        }

        stage ('deploy') {
            steps{
                echo 'Deploy stage executed.'

            }
        }
    }
}