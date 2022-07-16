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
            bat 'start /min python3 Project\\rest_app.py'
        }
    }
    stage('run web server') {
        steps {
            bat 'start /min python3 Project\\web_app.py'
        }
    }
     stage('run backend testing') {
        steps {
            bat 'python3 Project\\backend_testing.py'
        }
    }
    stage('run frontend testing') {
        steps {
            bat 'python3 Project\\frontend_testing.py'
        }
    }
    stage('run combined testing') {
        steps {
            bat 'python3 Project\\combined_testing.py'
        }
    }
    stage('run clean environment') {
        steps {
            bat 'python3 Project\\clean_environment.py'
        }
    }
  }
}