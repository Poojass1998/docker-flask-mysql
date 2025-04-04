pipeline {
  agent any

  environment {
    DOCKER_IMAGE = 'poojadocker23/flask-docker-app'
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
        withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh '''
            echo "$PASS" | docker login -u "$USER" --password-stdin
            docker push $DOCKER_IMAGE
          '''
        }
      }
    }

    stage('Deploy to EC2') {
      steps {
        sshagent(['ssh-credentials']) {
          sh """
            ssh -o StrictHostKeyChecking=no ubuntu@3.110.119.150 '
              cd /home/ubuntu/docker-flask-mysql &&
	      docker pull poojadocker23/flask-docker-app &&
              docker stop flask-app || true &&
              docker rm flask-app || true &&
              docker run -d --name flask-app -p 5000:5000 --env-file /home/ubuntu/docker-flask-mysql/.env poojadocker23/flask-docker-app
            '
          """
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
 failure {
      mail to: 'poojass423@gmail.com',
           subject: '❌ Flask App Deployment Failed',
           body: 'Please check the Jenkins console output to debug the issue.'
    }
}
}
