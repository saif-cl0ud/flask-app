pipeline {
  environment {
      Namespace = "default"
      ImageName = "saifrahm/flask-app"
      Creds = "615cfb48-e44f-4b51-85ca-5c6a8ab22b8e"
  }
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh 'printenv'
        sh "git rev-parse --short HEAD > .git/commit-id"
        imageTag= readFile('.git/commit-id').trim()
      }
    }
    stage('Build and push image with Container Builder') {
      steps {
        withDockerRegistry([credentialsId: "${Creds}", url: 'https://index.docker.io/v1/']) {
        sh "docker build -t ${ImageName}:${imageTag} ."
        sh "docker push ${ImageName}:${imageTag}"
      }
    }
    stage('Deploy Production') {
      // Production branch
      when { branch 'master' }
      steps{
        sh 'printenv'
        echo 'To access your environment run'
      }
    }
    }
  }
