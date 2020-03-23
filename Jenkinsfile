pipeline {
  environment {
      Namespace = "default"
      ImageName = "saifrahm/flask-app"
      Creds = "615cfb48-e44f-4b51-85ca-5c6a8ab22b8e"
  }

  stages {
    stage('Checkout') {
      steps {
        git credentialsId: 'fe19aa42-87d3-4f37-8f83-90415a0a8684', url: 'https://github.com/saif-cl0ud/flask-app.git'
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
    stage('Deploy Canary') {
      // Canary branch
      when { branch 'canary' }
      steps {

    sh "/usr/local/bin/helm --kubeconfig /var/cluster218/admin.conf upgrade flaskapp /var/demochart --set image.tag=${imageTag} --install --namespace ${Namespace} --wait"
        }
      }
    
    stage('Deploy Production') {
      // Production branch
      when { branch 'master' }
      steps{
        echo 'To access your environment run'
      }
    }
    stage('Deploy Dev') {
      // Developer Branches
      when {
        not { branch 'master' }
        not { branch 'canary' }
      }
      steps {
        echo 'To access your environment run `kubectl proxy`'
          
      }
    }
  }
}
