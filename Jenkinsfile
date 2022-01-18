pipeline {
    agent any

    stages {
        stage ('build') {
            steps{
                sh 'docker-compose -f /var/lib/jenkins/workspace/DB_Games_dev/docker-compose.yml up --build -d'
            }
        }

        stage ('test') {
            steps{
                echo 'Test stage executed.'
                sh 'docker exec -i dbsql bash -l'
                   'mysql -u root -proot'
                   'use database_games'
                   'show tables;'
                   'describe Games;'
            }
        }

        stage ('deploy') {
            steps{
                echo 'Deploy stage executed.'

            }
        }
    }
}