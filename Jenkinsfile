pipeline {
    agent any

    environment {
        DOCKER_INSTANCE_IP = credentials('ec2-public-ip') // Secret text (e.g., 54.xx.xx.xx)
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sshagent(['ec2-ssh-credentials']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@$DOCKER_INSTANCE_IP '
                        cd ~/docker-flask-mysql/app &&
                        docker build -t poojadocker23/flask-app:latest .
                    '
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sshagent(['ec2-ssh-credentials']) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no ubuntu@$DOCKER_INSTANCE_IP '
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin &&
                            docker push "$DOCKER_USER"/flask-app:latest
                        '
                        '''
                    }
                }
            }
        }

        stage('Deploy on EC2') {
            steps {
                sshagent(['ec2-ssh-credentials']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@$DOCKER_INSTANCE_IP '
                        cd ~/docker-flask-mysql &&
                        docker-compose down &&
                        docker-compose pull &&
                        docker-compose up -d
                    '
                    '''
                }
            }
        }
    }

    post {
        always {
            emailext (
                to: 'poojass423@gmail.com',
                subject: "Jenkins Pipeline: Build ${currentBuild.currentResult} for Job '${env.JOB_NAME}' #${env.BUILD_NUMBER}",
                body: """Hi Pooja,

The Jenkins build has completed with status: ${currentBuild.currentResult}.

Check console output at: ${env.BUILD_URL}

- Jenkins"""
            )
        }
    }
}

