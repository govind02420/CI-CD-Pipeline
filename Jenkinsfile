pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
    }

    stages {
        stage('Build') {
            steps {
                bat '"C:/Users/govin/AppData/Local/Programs/Python/Python313/Scripts/pip.exe" install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '"C:/Users/govin/AppData/Local/Programs/Python/Python313/Scripts/pytest.exe"'
            }
        }

        stage('Deploy') {
            when {
                expression {
                    return currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Deploying...'
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
