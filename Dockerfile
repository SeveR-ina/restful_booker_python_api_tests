# Use the official Python image as the base image
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the test script when the container starts
CMD ["python", "test_auth.py"]