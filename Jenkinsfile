pipeline { 
    agent any
        environment { 
        registry = "photop/project-3" 
        registryCredential = 'dockerhub' 
        dockerImage = 'project -3'
        }
    stages {
        stage('properties') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
                git 'https://github.com/photop33/project3.git'
            }
        }     
        stage('rest_app.py') {
            steps {
                script {
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\3\\rest_app.py'
                    bat 'echo success dockker'
                }
            }
        }
        stage('Backend_testing') {
            steps {
                script {
                    bat 'python3 C:\\Users\\l1313\\PycharmProjects\\3\\Backend_testing.py'
                    bat 'echo success Backend_testing'
                }
            }
        }
        stage('clean_environemnt') {
            steps {
                script {
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\3\\clean_environemnt.py'
                    bat 'echo success clean_environemnt'
                 }
            }
        }
        stage('build and push image') { 	
            steps { 	
                script { 
                    bat "docker build -t lior ."
                    bat "docker push photop/project-3 lior"
                    dockerImage = "project-3" + "${1}"	
                    docker.withRegistry('', registryCredential) {	
                    dockerImage.push() 	
                        }	
                   }  	
             }	
        }
        stage('set version') { 	
            steps {	
                bat "docker images"
                bat "echo IMAGE_TAG=${1} > .env"      	
              post {	
              always {	
                     bat "docker images"	
                     bat "docker rmi $registry:${1}"	
                  }	
               }	
            }	
         }
        stage ('docker compose'){
            steps {
                script{
                    bat 'docker-compuse up -d'
                    bat 'echo docker compuse up'
                    }
                }
           }       
        stage ('docker_backend_testing'){
            steps{
                script{
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\3\\docker_backend_testing.py'
                    bat 'echo success docker_backend_testing.py'
                    }
                }
            }
        stage ('clen'){
            steps{
                script{
                    bat 'start/min python3 C:\\Users\\l1313\\PycharmProjects\\3\\clean_environemnt.py'
                    bat 'echo success clean_environemnt'
                }
            }
        }
    }
}
