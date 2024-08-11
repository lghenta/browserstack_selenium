pipeline {
    agent any
    
    environment {
        // Injects BrowserStack credentials as environment variables
        BROWSERSTACK_USERNAME = credentials('browserstack-username')  // Retrieves the BrowserStack username stored in Jenkins credentials
        BROWSERSTACK_ACCESS_KEY = credentials('browserstack-accesskey')  // Retrieves the BrowserStack access key stored in Jenkins credentials
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checks out the code from the source control management (SCM) repository
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                // Sets up a Python virtual environment for the project
                sh 'python3 -m venv venv'  // Creates a virtual environment in the 'venv' directory
                sh '. venv/bin/activate'   // Activates the virtual environment
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Installs the required Python dependencies from the 'requirements.txt' file
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Executes the test suite using pytest
                sh 'pytest test_browserstack.py'  // Runs tests defined in the 'test_browserstack.py' file
            }
        }
    }
    
    post {
        always {
            // Cleans up by deactivating the virtual environment after the pipeline runs
            sh 'deactivate'  // Deactivate the Python virtual environment
        }
    }
}
