pipeline {
    agent any

    stages {
         stage('checking awscli configuration') {
            steps {
                sh 'aws s3 ls'
            }
        }
        stage('Python_version') {
            steps {
                sh 'python --version'
                sh 'python3 --version'
            }
        }
        stage('Running_python_script') {
            steps {
                sh 'capture_changelog.py'
            }
        }
    }
}
