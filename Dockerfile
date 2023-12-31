# Use the official Python image as the base image
FROM python:3.11.5

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set an environment variable to indicate that we are running inside Docker
ENV RUNNING_IN_DOCKER=true

# Run the tests and generate Allure report
RUN python -m pytest --alluredir=allure_result_folder ./tests