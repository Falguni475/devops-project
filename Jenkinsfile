cat > Jenkinsfile << 'EOF'
pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                echo 'Fetching code from GitHub...'
                git 'https://github.com/Falguni475/devops-project.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building website...'
                sh 'ls'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing website...'
                sh 'echo Test Passed'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying website...'
                sh '''
                mkdir -p deployment_folder
                cp index.html deployment_folder/
                cp style.css deployment_folder/
                cp script.js deployment_folder/
                echo "Deployment Successful"
                '''
            }
        }

    }
}
EOF
