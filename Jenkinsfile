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
                sh 'docker-compose exec -T dbsql bash'
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