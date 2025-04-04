pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "poojadocker23/flask-app:latest"
        DOCKER_CREDENTIALS = "docker-hub-credentials"
        GIT_CREDENTIALS = "github-credentials"
        GIT_REPO = "https://github.com/Poojass1998/docker-flask-mysql.git"
        GIT_BRANCH = "master"
    }

    stages {
        stage("Clone Repository") {
            steps {
                dir('workspace') {
                    withCredentials([usernamePassword(credentialsId: GIT_CREDENTIALS, usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                        sh "git clone -b ${GIT_BRANCH} https://${GIT_USER}:${GIT_PASS}@github.com/Poojass1998/docker-flask-mysql.git"
                    }
                }
            }
        }

         stage("Build Docker Image") {
            steps {
                dir('workspace/docker-flask-mysql/app') {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage("Push to Docker Hub") {
            steps {
                withDockerRegistry([credentialsId: DOCKER_CREDENTIALS, url: ""]) {
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }

        stage("Deploy on EC2") {
            steps {
                withCredentials([
                    string(credentialsId: 'ec2-public-ip', variable: 'EC2_IP'),
                    usernamePassword(credentialsId: 'ec2-ssh-credentials', usernameVariable: 'EC2_USER', passwordVariable: 'EC2_PASS')
                ]) {
                    sh '''
                    sshpass -p "${EC2_PASS}" ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} <<EOF
                        cd ~/docker-flask-mysql
                        docker pull ${DOCKER_IMAGE}
                        docker-compose down
                        docker-compose up -d
                    EOF
                    '''
                }
            }
        }
    }

    post {
        success {
            emailext(
                from: 'poojass423@gmail.com',
                to: 'poojass423@gmail.com',
                subject: 'Build Success - Flask App',
                body: 'The CI/CD pipeline executed successfully and the Flask app is deployed on EC2.'
            )
        }
        failure {
            emailext(
                from: 'poojass423@gmail.com',
                to: 'poojass423@gmail.com',
                subject: 'Build Failed - Flask App',
                body: 'The build or deployment failed. Please check Jenkins console output for details.'
            )
        }
    }
}

