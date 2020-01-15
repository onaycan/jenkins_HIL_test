pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
          docker.image.inside() {
			    PWD = sh (
			    	script: 'touch bok.txt',
			    	returnStdout: true
			    ).trim()
			    }
      }
    }
  }
}