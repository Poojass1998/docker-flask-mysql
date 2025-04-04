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
    sh 'docker build -t poojass1998/flask-docker-app ./app'
  }
}

    stage('Push to DockerHub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh '''
            echo "$PASS" | docker login -u "$USER" --password-stdin
            docker push $DOCKER_IMAGE
          '''
        }
      }
    }

    stage('Deploy to EC2') {
      steps {
        sshagent(['ec2-ssh-credentials']) {
          sh '''
            ssh -o StrictHostKeyChecking=no ubuntu@<3.110.119.150> '
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
  post {
  success {
    mail to: 'poojass423@gmail.com',
         subject: 'Flask Docker App Deployed ',
         body: 'Your Flask app is deployed on EC2 at http://3.110.119.150:5000'
  }
}
}
