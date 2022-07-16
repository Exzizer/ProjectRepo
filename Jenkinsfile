pipeline {
  agent any
  stages {
    stage('poll') {
      steps {
        git(url: 'https://github.com/Exzizer/ProjectRepo', branch: 'master', poll: true)
      }
    }
    stage('run backend server') {
        steps {
            bat 'start /min python rest_app.py'
        }
    }
    stage('run backend server') {
        steps {
            bat 'start /min python web_app.py'
        }
    }
     stage('run backend testing') {
        steps {
            bat 'python <PYTHON FILE>.py'
        }
    }
  }
}