pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Build') {
            steps {
                bat 'python -m venv %VENV_DIR%'
                bat '%VENV_DIR%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '%VENV_DIR%\\Scripts\\pip install pytest'
                bat '%VENV_DIR%\\Scripts\\pytest tests'
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                bat 'echo Deploying to staging environment...'
                // Add your Windows deploy script here
            }
        }
    }

    post {
        success {
            mail to: 'govind.02420@gmail.com',
                 subject: "✅ Jenkins Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Great! The build succeeded.\n\nSee details at ${env.BUILD_URL}"
        }

        failure {
            mail to: 'govind.02420@gmail.com',
                 subject: "❌ Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Oops! The build failed.\n\nCheck logs at ${env.BUILD_URL}"
        }
    }
}
