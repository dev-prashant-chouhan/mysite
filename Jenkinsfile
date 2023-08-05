pipeline{
    agent any
    stages{
        stage("ContinuousDownload"){
            steps{
                git 'https://github.com/dev-prashant-chouhan/mysite.git'
            }
        }
        stage("ContinuousBuild"){
            steps{
                input message: 'Need approval of DM!', submitter: 'prashant-manager'
                sh 'sudo docker build . -t mysite'
            }
        }
        stage("ContinuousDeployment"){
            steps{
                sh 'sudo docker run -d -p 8000:8000 mysite'
            }
        }
    }
}

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
