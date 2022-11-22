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
                env.QUALYS_REPORT = report(script: 'ls ./*.json', returnStdout: true).trim() 
                sh 'echo $QUALYS_REPORT'
                }
            }
        }
        //stage('generating artifact'){
          //  steps {
            //    archiveArtifacts artifacts: '**/*.json'

            //}
        //}
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
            }
        }
    }
}
