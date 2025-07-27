pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh './$VENV_DIR/bin/pip install pytest'
                sh './$VENV_DIR/bin/pytest tests'
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                sh 'echo "Deploying to staging environment..."'
                // Add your deploy command here
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
