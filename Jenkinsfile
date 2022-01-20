pipeline {
    agent any

    stages {
        stage ('build') {
            steps{
                sh 'docker-compose -f /var/lib/jenkins/workspace/DB_Games_dev/docker-compose.yml up --build -d'
                export 'PYTHONPATH=$PATH_TO_MODULE:$PYTHONPATH'
                echo 'Build Stage Completed'
            }
        }

        stage ('test') {
            steps{
                echo 'Test stage executed.'
                sh 'pip install flask'
                sh 'pip install flask-mysqldb'
                sh 'python3 webapp/test_app.py'
            }
        }

        stage ('deploy') {
            steps{
                echo 'Deploy stage executed.'

            }
        }
    }
}