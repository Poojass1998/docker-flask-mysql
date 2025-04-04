pipeline {
  agent any

  environment {
    DOCKER_IMAGE = 'poojass1998/flask-docker-app'
  }

  stages {
    stage('Clone') {
      steps {
        git 'https://github.com/Poojass1998/docker-flask-mysql.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE ./app'
      }
    }

    stage('Push to DockerHub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh '''
            echo "$PASS" | docker login -u "$USER" --password-stdin
            docker push $DOCKER_IMAGE
          '''
        }
      }
    }

    stage('Deploy to EC2') {
      steps {
        sshagent(['ec2-key']) {
          sh '''
            ssh -o StrictHostKeyChecking=no ubuntu@<EC2-IP> '
              docker pull $DOCKER_IMAGE &&
              docker stop flask-app || true &&
              docker rm flask-app || true &&
              docker run -d --name flask-app -p 5000:5000 --env-file .env $DOCKER_IMAGE
            '
          '''
        }
      }
    }
  }
}
