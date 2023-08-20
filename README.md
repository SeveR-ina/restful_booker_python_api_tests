# Restful Booker Python API Tests

This project contains automated API tests for the Restful Booker service using Python.

<img src="Screenshot_1.png" width="512"/>

## Purpose

The purpose of this project is to showcase how to automate API tests for the Restful Booker service. The tests are written in Python using the `pytest` framework and utilize the `requests` library for making HTTP requests. Docker is used to provide a consistent environment for running the tests. Additionally, two reporting tools, Allure and `pytest-html`, are integrated to provide detailed test reports.

## Tech Stack and Dependencies

- Python
- `pytest`
- `requests`
- Docker
- Allure for reporting
- `pytest-html` for additional reporting
- SonarCloud Security Scan

## How to Run the Tests

1. Install Python on your machine;
2. Clone this repository;
3. Navigate to the project directory in the terminal.

### Running Tests Locally

1. Install project dependencies:
```
pip install -r requirements.txt
```

2. Run pytest API tests locally:
```
pytest -s --log-cli-level=INFO test_auth.py
```

3. Run the tests with Allure reporting:
```
pytest --alluredir=allure-results test_auth.py
```

3.1. Run the tests with pytest-html reporting:
```
pytest --html=reports/report.html test_auth.py
```

3.2. Run the tests with both Allure and HTML reports:
```
pytest --alluredir=./allure-results --html=./reports/report.html
```
This command specifies the directory for Allure results and the file path for the HTML report. It will run your tests and generate both types of reports.

### Details about Allure Reporting and how to see html report for it

This project utilizes Allure reporting to provide comprehensive and visually appealing test reports.

#### Installation

Before using Allure reporting, you need to have the Allure command-line tool installed on your machine. You can follow the installation instructions provided on the Allure website: [Allure Installation Guide](https://docs.qameta.io/allure/#_installing_a_commandline)

#### Generating Allure Report

1. After running your tests, Allure results will be generated automatically. These results are stored in the `allure-results` directory.

2. To generate an Allure report from the results, open a terminal and navigate to your project directory.

3. Run the following command to generate the Allure report:
```
allure generate allure-results -o allure-report --clean
```

#### Viewing the Allure Report

1. Once the report is generated, you can view it using the Allure command-line tool. Run the following command:
```
allure open allure-report
```

2. This will open the Allure report in your default web browser. The report provides detailed insights into your test execution, including steps, attachments, assertions, and more. You can explore the report to analyze the results visually.

#### Cleaning Up

You can clean up the generated Allure results and report directories if needed. Simply delete the `allure-results` and `allure-report` directories from your project.


### Running Tests with Docker

1. Install Docker on your machine.

2. Make sure that Docker is running.

3. Build the Docker image:
```
docker-compose build
```

4. Run the tests in a Docker container:
```
docker-compose up
```

### Running Tests through Pycharm configurations:
1. Open Your Project: Open your project in PyCharm.
2. Create a Run Configuration:
* Click on "Run" in the top menu.
* Select "Edit Configurations..."
3. Add a New Configuration:
* Click the "+ Add New Configuration" button (the plus sign icon).
* Select "Python tests" > "pytest" from the dropdown.
4. Configure the Run Configuration:
* Set the "Name" field to something descriptive, like "Run Pytest Tests."
* In the "Target" field, select "Custom" and specify the path to your test file, which is test_auth.py.
* In the "Working directory" field, specify the directory where your project is located.
5. Add Environment Variables:
* In the "Environment variables" section, click the "..." button to add environment variables.
* Add the environment variables for your test data. For example:
    * Name: BASE_URL, Value: https://restful-booker.herokuapp.com
    * Name: AUTH_DATA, Value: {"username": "admin", "password": "password123"}
    * Name: WRONG_AUTH_DATA, Value: {"username": "111", "password": "111"}

6. Apply and Save the Configuration: Click the "Apply" button and then the "OK" button to save the configuration.

## CI/CD
With main.yml file, CI/CD workflow will perform the following steps:

- Checkout the repository.
- Install Python and dependencies.
- Install pytest.
- Run tests again using pytest-html for HTML reports.
- Archive the HTML report.

Runner starts every time when you push changes to master brunch and creates new workflow. Results and artifacts are available in Actions tab of the repository.

## Purpose of Test Files

- `test_auth.py`: Contains a test case to authenticate and check the success of the authentication.
- `test_data.py`: Contains test data such as authentication credentials and base URLs.
## SonarCloud Security Scan

We have integrated SonarCloud into our CI/CD pipeline to perform security scans on our codebase. SonarCloud is a powerful tool that helps us identify and address potential security vulnerabilities, code smells, and maintainability issues in our code.

### How It Works

When changes are pushed to the `master` branch, our CI/CD pipeline automatically triggers a SonarCloud security scan. Here's a high-level overview of the process:

1. The CI/CD pipeline sets up the environment and runs our tests.
2. After the tests are executed successfully, SonarCloud is invoked to perform the security scan.
3. SonarCloud analyzes the codebase, identifies vulnerabilities, and provides detailed reports.
4. The results of the scan are accessible through the SonarCloud dashboard and also integrated into our GitHub repository.

### Why It's Important

By incorporating SonarCloud security scans into our CI/CD pipeline, we can proactively detect and address security risks, maintain code quality, and ensure that our application is developed and deployed with the highest standards of security and reliability.

### Accessing Reports

The reports generated by SonarCloud are available both within our SonarCloud dashboard and as part of our GitHub repository. You can view the detailed analysis, identified vulnerabilities, and recommendations directly on the SonarCloud platform.

## Troubleshooting

### "No pytest runner found in the selected interpreter" warning

If you encounter the "No pytest runner found in the selected interpreter" warning when trying to run tests using a PyCharm configuration, follow these steps to resolve it:

1. **Install pytest in Your Virtual Environment**:
   
   Ensure pytest is installed within your project's virtual environment. To do this:
   
   - Create a virtual environment using `python -m venv venv`.
   - Activate the virtual environment (`venv\Scripts\activate` on Windows, `source venv/bin/activate` on macOS and Linux).
   - Install pytest using `pip install pytest`.

2. **Configure the Python Interpreter in PyCharm**:

   Verify that the correct Python interpreter from your virtual environment is selected in PyCharm:
   
   - Go to "File" > "Settings" (or "PyCharm" > "Preferences" on macOS).
   - Navigate to "Project: YourProjectName" > "Python Interpreter."
   - Choose the Python interpreter located within your virtual environment.

3. **Recreate the Run Configuration**:

   After ensuring pytest is available in your virtual environment and the correct Python interpreter is configured in PyCharm, recreate your test run configuration as described earlier.

4. **Run the Tests Again**:

   With the pytest installation in your virtual environment and the correct interpreter selected, try running your tests using the newly created configuration.

### Permission Denied when Creating a Virtual Environment

If you encounter a "Permission denied" error when attempting to create a virtual environment using `python -m venv venv`, follow these steps to resolve the issue:

1. **Run as Administrator (Windows)**: If you're on Windows, close any open Command Prompt windows, right-click the Command Prompt icon in the Start menu, select "Run as administrator," and navigate to your project directory before running the command again.

2. **Choose a Different Directory**: You can specify a different location for creating the virtual environment where you have write permissions. Use a command like `python -m venv C:\path\to\desired\location\venv`, replacing the path with your preferred directory.

3. **Consider Using Anaconda or Miniconda**: If you continue to encounter permission problems, consider using Anaconda or Miniconda to manage environments. These tools offer an alternative approach to creating and managing virtual environments and may help avoid permission issues.

By following one of these approaches, you should be able to create a virtual environment without encountering permission errors.

