pipeline {
    agent any

    environment {
        DOCKER_INSTANCE_IP = credentials('ec2-public-ip')
    }

    stages {
        stage('Clone Repository') {
            steps {
                dir('workspace') {
                    withCredentials([usernamePassword(credentialsId: 'github-credentials', passwordVariable: 'GIT_PASS', usernameVariable: 'GIT_USER')]) {
                        sh 'git clone -b master https://${GIT_USER}:${GIT_PASS}@github.com/Poojass1998/docker-flask-mysql.git'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('workspace/docker-flask-mysql/app') {
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
                     subject: "Build Successful - Flask App",
                     body: "Your Docker Flask App build and deployment completed successfully!"
        }
        failure {
            emailext to: 'poojass423@gmail.com',
                     subject: "Build Failed - Flask App",
                     body: "Something went wrong. Please check Jenkins pipeline logs."
        }
    }
}

