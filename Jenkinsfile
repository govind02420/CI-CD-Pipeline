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
                 subject: "✅ Jenkins Build Successful",
                 body: "Great! The build succeeded."
        }

        failure {
            mail to: 'govind.02420@gmail.com',          // yourname@gmail.com
                 subject: "❌ Jenkins Build Failed",
                 body: "Oops! The build failed."
        }
    }
}
