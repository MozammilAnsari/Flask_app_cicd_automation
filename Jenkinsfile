pipeline {
    agent any
    stages {
        stage('Test'){
            steps {
                echo 'Test is successful'
            }
        }
        stage('Repo Cloning'){
            steps {
               git branch: 'main',
            url: 'https://github.com/MozammilAnsari/Flask_app_cicd_automation.git'
            }
        }
        stage('Docker Login'){
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'Docker',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }
        stage('Iamge build & push'){
            steps{
            sh '''
            echo 'Image building step'
            docker build -t modassir7488/ecom_app:lts .
            echo 'Image push step'
            docker push modassir7488/ecom_app:lts
            echo 'Image pulling from dockerhub'
            docker pull modassir7488/ecom_app:lts
            '''
            }
        }
        stage('Stop and Run Image'){
            steps{
            sh '''
            echo "Stopping old container (if exists)"
            docker rm -f ecom_app || true
            echo 'Running docker container'
            docker run -p 5000:5000 --name ecom_app -d modassir7488/ecom_app:lts
            '''
            }
        }
    }
}