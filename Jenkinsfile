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
            bat 'python backend_testing.py'
        }
    }
    stage('run frontend testing') {
        steps {
            bat 'python frontend_testing.py'
        }
    }
    stage('run combined testing') {
        steps {
            bat 'python combined_testing.py'
        }
    }
    stage('run clean environment') {
        steps {
            bat 'python clean_environment.py'
        }
    }
  }
}