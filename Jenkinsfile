pipeline {
    agent any
    environment {
            PORT=8081
        }
    stages {
        stage('scm') {
            steps {
                sh(returnStdout: true, script: ''' 
                git clone https://github.com/EqualExperts-Assignments/equal-experts-intolerant-liberal-shock-1a1f281a9c27.git
                cd EqualExperts-Assignments/equal-experts-intolerant-liberal-shock-1a1f281a9c27
                git checkout solution''')
            }
        }
        stage('unit-tests') {
            steps {
                sh(returnStdout: true, script: ''' pytest . ''')
            }
        }
        stage('build-image') {
            steps {
                sh (returnStdout: true, script: """ docker build -t localhost:5000/webapp:$BUILD_NUMBER . """)
            }
        }
        stage('publish') {
            steps {
                sh "docker push localhost:5000/webapp:$BUILD_NUMBER"
            }
        }
        stage('deploy') {
            steps {
                // DOCKER_PORT=$BUILD_NUMBER+$PORT
                sh """docker run -itd -p 8081:8080 localhost:5000/webapp:$BUILD_NUMBER"""
            }
        
        }
    }
}