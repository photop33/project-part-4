pipeline { 
    agent any
    environment { 
        registry = "photop/project-3" 
        registryCredential = 'docker_hub'
        dockerImage = ""
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
                    bat 'start /min python rest_app.py'
                    bat 'echo success rest_app.py'
                }
            }
        }
        stage('Backend_testing') {
            steps {
                script {
                    bat 'python3 Backend_testing.py'
                    bat 'echo success Backend_testing'
                }
            }
        }
	stage('clean_environemnt-1') {
            steps {
                script {
                    bat 'start/min python3 clean_environemnt.py'
                    bat 'echo success clean_environemnt-1'
                 }
            }
        }    

        stage ('Build Docker image - locally'){
            steps {
                script{
                    bat "docker build -t \"$BUILD_NUMBER\" ."
                    bat "start/min docker run \"$BUILD_NUMBER\""
                }
            }
        }
        stage('build and push image') { 	
            steps { 	
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry('', registryCredential) {	
                    dockerImage.push() 	
                    }	
                }  	
            }	
        }	
        stage('set version') { 	
            steps {	
                bat "echo IMAGE_TAG=${BUILD_NUMBER} > .env"   
			    bat "more .env"
            }	
         }
        stage ('docker-compose'){
            steps {
                script{
                    bat 'docker-compose up -d'
                    bat 'echo success docker-compose'
                    }
                }
           }       
        stage ('docker_backend_testing'){
            steps{
                script{
                    bat 'python3 docker_backend_testing.py'
                    bat 'echo success docker_backend_testing.py'
                    }
                }
            }
        stage('docker-compose down & delete image') { 
            steps {
                script{
                bat 'docker-compose down '
                bat "docker image rm  ${BUILD_NUMBER}"      		
                bat 'echo docker-compose down + delete image'
                }
            }
        }  
	stage('clean_environemnt-2') {
            steps {
                script {
                    bat 'start/min python3 clean_environemnt.py'
                    bat 'echo success clean_environemnt-2'  
		}
	    }
	}
	stage ('Deploy HM'){
            steps{
                script{
		    bat 'helm repo list ' 
                    //bat 'helm install lior photop/project-3 --set image.version=photop33/project_4":${BUILD_NUMBER}"'
		    //bat 'helm repo update'
                    //bat 'helm install itay itayzrihan1/helmproject --set image.version=itayzrihan/project3":${BUILD_NUMBER}"'
		    //bat 'helm repo add lior https://photop33.github.io/Project3/lior'
		    //bat 'helm repo update'
		    }  
                }
            }			
	stage ('Deploy HELM'){
            steps{
                script{
		    bat 'minikube start'
                    //bat 'kubectl apply -f https://raw.githubusercontent.com/photop33/Project3/master/lior/templates/deployment.yaml'
	            //bat 'kubectl apply -f https://raw.githubusercontent.com/photop33/Project3/master/lior/templates/service.yaml'
		    //bat 'kubectl get deployments'  
		    //bat 'kubectl get service'
		    bat 'start/min minikube service test-service --url'
                    bat 'echo succes Deploy HELM'
		    }  
                }
            }
	stage ('extra-secret'){
	    steps{
                script{ 
		    bat 'kubectl apply -f https://raw.githubusercontent.com/photop33/Project3/master/lior/templates/username.txt'
		    bat 'kubectl get secret mysecret -o yaml'
		    bat 'kubectl get pod secret-envars-test-pod'
		    bat 'echo succes secret'
		   }
                } 
	    }  
	stage ('extra-mysql'){
	    steps{
                script{ 
		    bat 'kubectl apply -f https://raw.githubusercontent.com/photop33/Project3/master/EXTRA-mysql/mysql-deployment2.yaml'
		    bat 'kubectl apply -f https://raw.githubusercontent.com/photop33/Project3/master/EXTRA-mysql/mysql-pv.yaml'
		    bat 'kubectl describe deployment mysql'
		    bat 'kubectl get pods -l app=mysql'
		    bat 'kubectl describe pvc mysql-pv-claim'
		    bat 'kubectl run -it --rm --image=mysql:5.6 --restart=Never mysql-client -- mysql -h mysql -ppassword'
		   }
                } 
	    }  
	stage ('extra.py'){
	    steps{
                script{ 
		   //bat 'kubectl apply -f https://raw.githubusercontent.com/photop33/Project3/master/lior/templates/extra.yaml'
		   //bat 'kubectl describe secret mariadb-root-password'
		   bat 'echo next '
		   }
                }
	    }   
	stage ('K8S_backend_testing.py'){
	    steps{
                script{
		    bat 'python3 K8S_backend_testing.py'
		    bat 'echo succes K8S_backend_testing.py'
		   }
                }
	    }
	stage('clean_environemnt-3') {
            steps {
                script {
                    bat 'start/min python3 clean_environemnt.py'
                    bat 'echo success clean_environemnt-3'
                   }
              }
          }
      }
	    
  post {	
      always {	
             bat "docker rmi $registry:${BUILD_NUMBER}"	
          }	
     }
}
