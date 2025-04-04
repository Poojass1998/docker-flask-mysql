pipeline {
    agent any

    environment {
        DOCKER_INSTANCE_IP = credentials('ec2-public-ip') // secret text
        DOCKER_HUB_PASS = credentials('dockerhub-pass')   // secret text
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sshagent(['ec2-ssh-credentials']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@$DOCKER_INSTANCE_IP '
                        cd ~/docker-flask-mysql/app &&
                        docker build -t poojadocker23/flask-app:latest .
                    '
                    """
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sshagent(['ec2-ssh-credentials']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@$DOCKER_INSTANCE_IP '
                        echo "$DOCKER_HUB_PASS" | docker login -u poojadocker23 --password-stdin &&
                        docker push poojadocker23/flask-app:latest
                    '
                    """
                }
            }
        }

        stage('Deploy on EC2') {
            steps {
                sshagent(['ec2-ssh-credentials']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@$DOCKER_INSTANCE_IP '
                        cd ~/docker-flask-mysql &&
                        docker-compose down &&
                        docker-compose up -d
                    '
                    """
                }
            }
        }
    }

    post {
        success {
            emailext to: 'poojass423@gmail.com',
                     subject: "✅ Build Successful - Flask App",
                     body: "Hi Pooja,\n\nYour Docker Flask App build and deployment completed successfully! 🎉\n\n- Jenkins"
        }
        failure {
            emailext to: 'poojass423@gmail.com',
                     subject: "❌ Build Failed - Flask App",
                     body: "Hi Pooja,\n\nThe build failed. Please check the Jenkins console output for more details.\n\n- Jenkins"
        }
    }
}

