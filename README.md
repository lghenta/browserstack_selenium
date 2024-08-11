
# BrowserStack Automation Project

## Overview

This project is designed to automate the testing of a web application using Selenium WebDriver and BrowserStack. The tests are written in Python and utilize the `pytest` framework to perform browser-based testing across different environments, including desktop browsers (Chrome, Firefox) and a mobile device (Samsung Galaxy S22).

The project is set up to run in a continuous integration/continuous deployment (CI/CD) environment using Jenkins, where tests are executed in parallel across different browser and device configurations. The project is configured to securely handle credentials using environment variables.

## Prerequisites

Before setting up and running the project, ensure you have the following prerequisites:

### Software Requirements

- **Python 3.x**: The project is written in Python and requires Python 3.x to run.
- **Pip**: Python's package installer is required to install the project dependencies.
- **Selenium**: Selenium WebDriver is used for browser automation.
- **BrowserStack Account**: A BrowserStack account is required to run the tests on different browser environments in the cloud.
- **Jenkins**: If you intend to run the project in a CI/CD pipeline, Jenkins is required.

### Python Dependencies

The required Python packages are listed in the `requirements.txt` file and will be installed in the setup process.

### Jenkins Configuration

- **Credentials**: You need to store your BrowserStack username and access key as credentials in Jenkins. The credentials should be named `browserstack-username` and `browserstack-accesskey`.
- **Python Environment**: Ensure Jenkins agents have Python 3.x installed.

## Project Structure

- **`config.yml`**: Contains the configuration for BrowserStack, including credentials (injected from Jenkins), the BrowserStack hub URL, test capabilities, and the test site details.
- **`conftest.py`**: Sets up the test environment, loads configurations, and defines the WebDriver capabilities and test data.
- **`test_browserstack.py`**: Contains the test cases that perform various actions on the test site, such as logging in, selecting a product, favoriting it, and verifying it in the favorites list.
- **`Jenkinsfile`**: Defines the Jenkins pipeline, including stages for checking out the code, setting up the Python environment, installing dependencies, and running the tests.

## Setup Instructions

### Step 1: Clone the Repository

First, clone the repository to your local machine:

### Step 2: Set Up the Python Environment

Create and activate a Python virtual environment:

\`\`\`bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
\`\`\`

### Step 3: Install Dependencies

Install the required Python packages using pip:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Step 4: Configure BrowserStack Credentials

Ensure your `config.yml` is correctly configured. The `username` and `access_key` fields should be automatically populated using environment variables or Jenkins credentials:

\`\`\`yaml
browserstack:
  username: \${BROWSERSTACK_USERNAME}
  access_key: \${BROWSERSTACK_ACCESS_KEY}
\`\`\`

If you're running the tests locally, you can manually set the environment variables:

\`\`\`bash
export BROWSERSTACK_USERNAME=your_username
export BROWSERSTACK_ACCESS_KEY=your_access_key
\`\`\`

### Step 5: Run Tests Locally

You can run the tests locally using the following command:

\`\`\`bash
pytest test_browserstack.py
\`\`\`

This command will execute the test cases defined in `test_browserstack.py` across the different capabilities specified in `config.yml`.

### Step 6: Running Tests in Jenkins

If you're using Jenkins for CI/CD, ensure your Jenkins pipeline is configured correctly with the provided `Jenkinsfile`. The pipeline will:

1. Check out the latest code from the repository.
2. Set up a Python virtual environment.
3. Install the necessary dependencies.
4. Run the tests using `pytest`.

The credentials for BrowserStack will be injected automatically from Jenkins' credentials store.

### Step 7: Post-Run Cleanup

The pipeline and local run scripts include a cleanup step that deactivates the Python virtual environment after the tests have completed.

## Project Details

### BrowserStack Integration

This project integrates with BrowserStack to execute tests across various browsers and devices, allowing you to ensure that your application works consistently across different environments. The `config.yml` file specifies the test capabilities, including browser versions, operating systems, and mobile devices.

### Test Scenarios

The main test scenarios include:

- Logging into the test site with provided credentials.
- Selecting a product (Samsung Galaxy S20+).
- Favoriting the product and verifying it in the favorites list.

These scenarios help ensure that key functionalities of the application are working as expected across different platforms.

### CI/CD Pipeline

The Jenkins pipeline ensures that the tests are run automatically whenever there is a new commit or a scheduled build. The results of the tests are available in Jenkins, and any failures will be reported, helping maintain the quality of the application over time.

## Troubleshooting

- **Credential Issues**: Ensure that the BrowserStack credentials are correctly set in Jenkins or your environment variables.
- **Dependency Issues**: If you encounter issues with dependencies, ensure that the virtual environment is correctly set up and that all packages in `requirements.txt` are installed.
- **BrowserStack Issues**: If the tests fail on BrowserStack, check the logs provided by BrowserStack to identify the root cause.

## Resources used:

https://www.browserstack.com/docs/automate/selenium/getting-started/python/pytest
https://www.browserstack.com/docs/automate/capabilities
https://www.browserstack.com/docs/automate/selenium/jenkins
https://www.jenkins.io/doc/book/installing/macos/
https://www.jenkins.io/doc/book/managing/
https://www.jenkins.io/solutions/python/
https://stackoverflow.com/questions/45986494/getting-python3-to-work-in-jenkins
https://uilicious.com/blog/how-to-click-a-button-using-selenium/
https://thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python?utm_content=cmp-true

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
