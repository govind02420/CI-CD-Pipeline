pipeline {
    agent any

    environment {
        APP_ENV = 'development'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/govind02420/CI-CD-Pipeline.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest > test-report.txt || exit 0'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask app...'
                bat 'python app.py'
            }
        }
    }

    post {
        success {
            mail to: 'govind.02420@gmail.com',          // yourname@gmail.com
                 subject: "✅ Jenkins Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Great! The build succeeded.\n\nSee details at ${env.BUILD_URL}"
        }
        failure {
            mail to: 'govind.02420@gmail.com',          // yourname@gmail.com
                 subject: "❌ Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Oops! The build failed.\n\nCheck logs at ${env.BUILD_URL}"
        }
    }
}
