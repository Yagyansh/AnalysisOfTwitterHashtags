pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        echo 'Hello POC'
      }
    }

    stage('Stage 2') {
      steps {
        tool(type: 'bash', name: 'infra-provisioner-v2')
      }
    }

  }
}