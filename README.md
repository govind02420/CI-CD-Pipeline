# Flask CI/CD Project

This project demonstrates how to use **Jenkins** and **GitHub Actions** for CI/CD.

## ✅ Jenkins Pipeline
- Automated via `Jenkinsfile`
- Runs build → test → deploy stages
- Triggers via GitHub webhook

## ✅ GitHub Actions
- Workflow in `.github/workflows/python-app.yml`
- Triggers on every push to `main`
- Runs test and deployment steps

#
# 1.Jenkins CI/CD pipeline for flask application

This project demonstrates a CI/CD pipeline for a Flask application using Jenkins, GitHub, Pytest, and Ngrok (for GitHub webhook on local machine).

## Prerequisites
- Python 3.13 installed
- Jenkins installed locally
- Git installed
- GitHub account
- Ngrok account (Free plan is fine)


## Pipeline Stages

The pipeline includes:

- **Build**: Install project dependencies using `pip`
- **Test**: Run tests using `pytest`
- **Deploy**: Simulated deploy step using `echo`


## Project Structure
```bash
CI-CD-Pipeline/
├── app.py
├── requirements.txt
├── Jenkinsfile
├── README.md
└── tests/
    └── test_app.py
```
## How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## 1. Jenkins Setup
### Step 1.1: Install Jenkins
- Download from: https://www.jenkins.io/download/
- Run and access Jenkins at: http://localhost:8080

### Step 1.2: Install Plugins
- Go to Manage Jenkins → Plugin Manager, and install:
    - Pipeline
    - Git
    - Email Extension

### Step 1.3: Install Python & Git
- Ensure Python and Git are installed and in PATH:
```bash
python --version
pip --version
git --version
```

## 2. Source Code: Connect Jenkins to GitHub Repo
### Step 2.1 Fork a Sample Flask App on GitHub
Use this sample Flask web app to fork:

### Repo to Fork:
👉 https://github.com/govind02420/CI-CD-Pipeline

1. Go to the repo link.
2. Click the Fork button at the top right (if needed).
3. This will create a copy under your GitHub account.


### Step 2.2 Clone the Repository on Jenkins Server

Jenkins will do it automatically using your pipeline but to make it work correctly, make sure Jenkins has access to Git and the repo:

✅ Inside Jenkins:
1. Go to **Dashboard** → **New Item** → **Pipeline** → **flask-cicd-pipeline**
2. In the configuration page:
    - Scroll to **Pipeline** → **Definition** → **Pipeline script from SCM**
    - Select Git
    - In the **Repository URL**, paste your GitHub repo:

    ```bash
        https://github.com/govind02420/CI-CD-Pipeline.git
    ```
    - Leave credentials empty (if public repo), or configure GitHub token if private.
    - Set Branch: main (or whatever your branch is)

## 3. Jenkins Pipeline:
Create a file named **Jenkinsfile**
```bash
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
        failure {
            echo 'Pipeline failed!'
        }
    }
}

```


## 4. Triggers: Automatically Build on main Branch Push
To trigger Jenkins pipeline builds automatically when you push code to GitHub’s main branch, follow these two parts:

### Part 1: Enable GitHub Webhook
Step-by-step:
1. Go to your forked GitHub repository
    ➤ https://github.com/govind02420/CI-CD-Pipeline

2. Click on ***Settings → Webhooks → Add webhook***

3. Fill in the webhook details:
- Payload URL:
```
        http://your_jenkins_ip:8080/github-webhook/              
```
    Example: http://192.168.1.10:8080/github-webhook/ (Use Jenkins VM IP)
    Example: https://abc123.ngrok-free.app/github-webhook/
    Note : you're running Jenkins on your local Windows laptop, you need to use ngrok to expose Jenkins to the internet.
- Content type: **application/json**
- Which events: **Choose Just the push event**
- Click **Add Webhook**

### Part 2: Configure Jenkins Job
For Pipeline Job:
1. Open Jenkins → your job → Configure
2. Scroll to "**Build Triggers**"
3. Check "**GitHub hook trigger for GITScm polling**"


## 5. Notifications: Email Notification Setup
- Set up a notification system to alert via email when the build process fails or succeeds.

### Step 5.1: Use App Password (Gmail)
- Enable 2FA from: https://myaccount.google.com/security
- Generate App Password for "Mail" → copy it

### Step 5.2: Configure Jenkins Email
- Go to Manage Jenkins → System → Email Notification
- SMTP Server: smtp.gmail.com
- Use SMTP Authentication: ✅
- Username: your_email@gmail.com
- Password: Your App Password
- Use TLS: ✅
- Port: 587
- Default Recipients: your email

### Step 5.3: Add Email in Job Pipeline
Edit your **Jenkinsfile** and add a post section like this:

```bash
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

```
## Outcome
1. ✅ Jenkins fetches the latest code from GitHub repository on every push to main branch.
2. ✅ Build stage installs all required Python dependencies using pip.
3. ✅ Test stage runs unit tests using pytest.
4. ✅ Deploy stage is triggered after successful tests (can be extended to real deployment).
5. ✅ Email notifications are sent on both build success and failure.
6. ✅ GitHub Webhook integrated via ngrok to enable automatic builds on local Jenkins after every GitHub push.


## Screenshots

### Jenkins_Dashboard
![Jenkins_Dashboard](Screenshots/Jenkins_Dashboard.png)

### Source_Code
#### Connect_1
![Source_Code_Connect_1](Screenshots/Source_Code_Connect_Jenkins_to_GitHub_Repo_1.png)
#### Connect_2
![Source_Code_Connect_2](Screenshots/Source_Code_Connect_Jenkins_to_GitHub_Repo_2.png)

### Triggers
#### Git_Webhook
![Triggers_Git_Webhook](Screenshots/Triggers_Part_1_Automatically_Manage_Webhook.png)
#### Jenkins_Job
![Triggers_Jenkins_Job](Screenshots/Triggers_Part_2_Configure_Jenkins_Job.png)

### Jenkins_Build_Sucess
![Jenkins_Build_Sucess](Screenshots/Jenkins_Build_Sucess.png)

### Email_Notification_Setup
![Email_Notification_Setup](Screenshots/Email_Notification_Setup.png)

### Notification_Alert_via_Email
![Notification_Alert_via_Email](Screenshots/Notification_Alert_via_Email.png)


#
# 2.GitHub Actions CI/CD Pipeline Flask App

This repository includes a CI/CD workflow using GitHub Actions.


## Step 1: Create the GitHub Actions folder
- Create workflows directory::
```bash
mkdir -p .github/workflows
```

### Create Workflow Directory
- Inside your repo, structure like this:
```bash
.github/
└── workflows/
    └── python-app.yml
```

### New Project Structure
```bash
CI-CD-Pipeline/
├── app.py
├── requirements.txt
├── Jenkinsfile
├── README.md
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── python-app.yml
```

## SStep 2: Create Workflow File
- Create a file named:
    - .github/workflows/python-app.yml

```bash
name: Flask CI/CD

on:
  push:
    branches: [ "main" ]     # or use "master" if that’s your default branch
  pull_request:
    branches: [ "main" ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: 🔃 Checkout code
      uses: actions/checkout@v3

    - name: 🐍 Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: 📦 Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: 🧪 Run tests
      run: |
        pytest


```

##  Step 3: Push to GitHub
- Once the file is created, push the changes:
```bash
git add .github/workflows/python-app.yml
git commit -m "Add GitHub Actions CI workflow"
git push origin main

```
## Step 4: View the Workflow on GitHub
- Go to your repository on GitHub:
    - Click on the "Actions" tab
    - You’ll see a new workflow named Flask CI/CD
    - It runs automatically after you push



## Screenshots for Submission

### All_workflows.png
![All_workflows](Screenshots/All_workflows.png)

### Test_Session
![Test_Session](Screenshots/Test_Session.png)

