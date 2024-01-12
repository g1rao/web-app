pipeline {
    agent any
    environment {
            PORT=8081
        }
    stages {
        stage('scm') {
            steps {
                sh(returnStdout: true, script: ''' 
                rm -rf web-app/
                git clone https://github.com/g1rao/web-app.git
                cd web-app/
                git checkout solution''')
            }
        }
        stage('unit-tests') {
            steps {
                sh(returnStdout: true, script: ''' 
                python3 -m venv venv/
                . venv/bin/activate
                pip3 install -r web-app/requirements.txt
                pytest . ''')
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