pipeline {
    agent any
    stages {
        stage("Cloning Code") {
            steps{
                echo "Cloning from github"
                git url:"https://github.com/dev-prashant-chouhan/mysite.git", branch:"master"
            }
        }
        stage("Build"){
            steps{
                echo "Build the project"
                sh "docker build -t mysite ."
            }
        }
        stage("Deploy to docker hub"){
            steps{
                echo "Deployment to docker hub"
                withCredentials([usernamePassword(credentialsId:"dockerHub", passwordVariable:"dockerHubPass", usernameVariable:"dockerHubUser")]){
                    sh "docker tag mysite ${env.dockerHubUser}/mysite:latest"
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker push ${env.dockerHubUser}/mysite:latest"
                }
            }
        }
        stage("Deploy"){
            steps{
                echo "Deployment"
                //sh "docker run -d -p 8000:8000 mysite"
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
}

// pipeline{
//     agent any
//     stages{
//         stage("ContinuousDownload"){
//             steps{
//                 git 'https://github.com/dev-prashant-chouhan/mysite.git'
//             }
//         }
//         stage("ContinuousBuild"){
//             steps{
//                 input message: 'Need approval of DM!', submitter: 'prashant-manager'
//                 sh 'sudo docker build . -t mysite'
//             }
//         }
//         stage("ContinuousDeployment"){
//             steps{
//                 sh 'sudo docker run -d -p 8000:8000 mysite'
//             }
//         }
//     }
// }

// node('built-in') {
//     stage("ContinuousDownload"){
//         git 'https://github.com/dev-prashant-chouhan/mysite.git'
//     }
//     stage("ContinuousBuild"){
//         sh 'sudo docker build . -t mysite'
//     }
//     stage("ContinuousDeployment"){
//         sh 'sudo docker run -d -p 8000:8000 mysite'
//     }
// }
