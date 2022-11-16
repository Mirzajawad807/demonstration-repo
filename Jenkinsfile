pipeline {
    agent any

    stages {
        stage('Python_version') {
            steps {
                sh 'python --version'
                sh 'python3 --version'
            }
        }
        stage('Running_python_script') {
            steps {
                sh 'python3 packer_list_creator.py'
            }
        }
    }
}
