#Deploying Docker Container using Python 3 Image

Key Objectives:

- Build a Docker image using a base Python 3 Linux image.
- Configure the Docker image to include your Python web application and its dependencies.
- Successfully run a Docker container based on the created image.
- Gain hands-on experience with Docker and containerization concepts.

Tasks/Activities List
- Create a new project directory and navigate into it.
- Create a file named Dockerfile in the project directory. This file will define the steps to build the Docker image.
- In the Dockerfile, use the FROM instruction to specify the base image as python:3. This image is readily available on Docker Hub.
- Install any additional dependencies required by your Python application using appropriate package managers like pip or conda.
- Copy your application code into the Docker container using the COPY instruction in the Dockerfile.
- Specify any required configuration settings for your application in the Dockerfile, such as environment variables or entry point commands.
- Build the Docker image using the docker build command. Provide a suitable tag name for the image.
- Run the Docker container based on the created image using the docker run command. Specify any necessary runtime options, such as port bindings or environment variable values.
- Test the running container to ensure your web application is functioning correctly. Use appropriate methods to validate its behavior.

##LAB Solution

###Project name :sample-python
Simple Python Flask API that will return a welcome message during API call.
Refer Dockerfile for instructions under project directory

Step 1: Wrote simple 'sample-python' application 
Step 2: Build Image >> docker build -t gowthamsammangi/sample-python:v1 .
Step 3: Push Image to Repository >>  $docker push gowthamsammangi/sample-python:v1
Step 4: Run the docker image >> docker run -dit --name Phythonapp -p 9000:8000 gowthamsammangi/sample-python:v1

CLI output:
ubuntu@ip-172-31-19-64:~/pp/sample-python$ docker run -dit --name Pythonapp -p 9000:8000 gowthamsammangi/sample-python:v1

Step 5: Test application
##CLI Test result ouput below . Same URL can be validated via browser
ubuntu@ip-172-31-19-64:~/pp/sample-python$ curl http://127.0.0.1:9000
{"message":"Welcome to my Python World v1"}  

   




