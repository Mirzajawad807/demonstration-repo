pipeline {
    agent any

    stages {
         stage('checking awscli configuration') {
            steps {
                sh 'aws s3 ls'
            }
        }
        stage('report link fetch') {
            steps {
                sh 'pwd'
                script {
                    env.QUALYS_REPORT = sh(script: 'ls ./*.json', returnStdout: true).trim() 
                    echo "pinting env variable ${env.QUALYS_REPORT}"
                }
            }
        }
        stage('generating artifact'){
            steps {
                sh 'echo "hello" > hello.txt'
                archiveArtifacts artifacts: '**/*.txt'
            }
        }
        stage('Python_version') {
            steps {
                sh 'python --version'
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Running_python_script') {
            steps {                
                sh 'python3 capture_changelog.py'
                echo "$JENKINS_HOME/jobs/$JOB_NAME/builds/$BUILD_NUMBER/archive"
                sh 'ls "$JENKINS_HOME/jobs/$JOB_NAME/builds/$BUILD_NUMBER/archive"'
            }
        }
    }
}
