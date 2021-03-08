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
	stage ('Deploy helm'){
            steps{
                script{
                    bat """
		          minikube start
                          cd lior
                          helm install test --debug --set image.repostitory=photop33/Project3,image.tag=${BUILD_NUMBER}  lior-0.1.0.tgz 
		          //helm install project-4-lior --dry-run  --debug --set image.repostitory=photop33/Project3,image.tag=${BUILD_NUMBER} lior'
		          helm list --all
		          minikube service list 
			  echo success Deploy helm
		        """
		    }  
                }
            }
	 stage ('Deploy > k8s_url.txt'){
            steps{
                script{
                   bat """ 
		    start /min /b minikube service test-lior --url >  k8s_url-test.txt
		    ping -n 10 127.0.0.1 
                    (type  k8s_url-test.txt | findstr "^http") >  k8s_url.txt
                    type k8s_url.txt
		    echo success Deploy k8s_url.txt
		    """		   
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
	stage ('extra-secret'){
	    steps{
                script{ 
	            bat 'start/min kubectl create secret generic project-4-secret --from-literal=usr=fFFGNbw0b0 --from-literal=pwd=66VHtH6ctH '
		    bat 'kubectl get secrets '
		    bat 'kubectl apply -f https://raw.githubusercontent.com/photop33/Project3/master/lior/templates/username.txt'
		    bat 'kubectl get secret mysecret -o yaml'
		    bat 'echo succes secret'
		   }
                } 
	    } 
	stage ('extra config-map'){
	    steps{
                script{ 
		   //bat 'kubectl apply -f https://raw.githubusercontent.com/photop33/Project3/master/lior/templates/extra.yaml'
		   //bat 'kubectl describe secret mariadb-root-password'
		   bat 'echo next config-map '
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
		    bat 'start/min kubectl run -it --rm --image=mysql:5.6 --restart=Never mysql-client -- mysql -h mysql -ppassword'

		   }
                } 
	    }  
	stage('clean_environemnt-3') {
            steps {
                script {
		    bat 'helm list --all'
                    bat 'start/min python3 clean_environemnt.py'
                    bat 'echo success clean_environemnt-3'
	            bat 'helm delete test '
                    bat 'del k8s_url-test.txt'
                    bat 'del k8s_url.txt'
		    bat 'kubectl delete deployment,svc mysql'
                    bat 'kubectl delete pvc mysql-pv-claim'
                    bat 'kubectl delete pv mysql-pv-volume'
		    bat 'helm list --all'
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
