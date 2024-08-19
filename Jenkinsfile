pipeline {
    // The 'agent any' directive tells Jenkins to execute the pipeline on any available agent.
    agent any

    environment {
        // Set up environment variables
        // 'SSH_KEY' stores the SSH key credential ID from Jenkins to be used for SSH access to the EC2 instance
        SSH_KEY = credentials('da24dc2c-341a-4367-914d-75fb5a2dd387')

        // 'PROJECT_DIR' specifies the directory on the EC2 instance where the project is located
        PROJECT_DIR = "/home/ubuntu/SendMyCoords"

        // 'ENV_DIR' specifies the directory on the EC2 instance where the Python virtual environment is located
        ENV_DIR = "${PROJECT_DIR}/flask-project-env"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository from the 'raghu' branch of the specified GitHub URL
                git branch: 'raghu', url: 'https://github.com/9394113857/SendMyCoords.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Use the SSH key stored in 'SSH_KEY' to SSH into the EC2 instance
                sshagent(['SSH_KEY']) {
                    sh """
                    // Connect to the EC2 instance and navigate to the project directory
                    ssh -o StrictHostKeyChecking=no ubuntu@52.91.56.85 '
                        cd ${PROJECT_DIR} &&

                        // Activate the Python virtual environment
                        source ${ENV_DIR}/bin/activate &&

                        // Install the required Python packages from 'requirements.txt'
                        pip install -r requirements.txt
                    '
                    """
                }
            }
        }

        stage('Run Application') {
            steps {
                // Use the SSH key stored in 'SSH_KEY' to SSH into the EC2 instance
                sshagent(['SSH_KEY']) {
                    sh """
                    // Connect to the EC2 instance and navigate to the project directory
                    ssh -o StrictHostKeyChecking=no ubuntu@52.91.56.85 '
                        cd ${PROJECT_DIR} &&

                        // Activate the Python virtual environment
                        source ${ENV_DIR}/bin/activate &&

                        // Kill any existing gunicorn processes (if any) to prevent port conflicts
                        pkill gunicorn || true &&

                        // Start the Flask application using gunicorn, binding it to all IP addresses on port 5000
                        gunicorn --bind 0.0.0.0:5000 run:app &
                    '
                    """
                }
            }
        }
    }
}
