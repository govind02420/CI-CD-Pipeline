pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '"C:\\Users\govin\AppData\Local\Programs\Python\Python313\Scripts\pip.exe" install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to staging environment...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
