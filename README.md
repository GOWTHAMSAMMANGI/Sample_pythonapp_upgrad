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

###Step 1: Wrote simple 'sample-python' application <br />
###Step 2: Build Image >> $docker build -t gowthamsammangi/sample-python:1.0 .<br />
###Step 3: Push Image to Repository >>  $docker push gowthamsammangi/sample-python:1.0<br />
###Step 4: Run the docker image >> docker run -p 9000:8000 gowthamsammangi/sample-python:1.0<br />
##CLI output:<br/>
anithar@Anithas-MacBook-Pro sample-python % docker run -p 9000:8000 gowthamsammangi/sample-python:1.0<br />
 * Serving Flask app 'launch'<br />
 * Debug mode: on<br />
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.<br />
 * Running on all addresses (0.0.0.0)<br />
 * Running on http://127.0.0.1:8000<br />
 * Running on http://172.17.0.3:8000<br />
Press CTRL+C to quit<br />
 * Restarting with stat<br />
 * Debugger is active!<br />
 * Debugger PIN: 136-583-677<br />
###Step 5: Test application<br />
##CLI Test result ouput below . Same URL can be validated via browser <br />
anithar@Anithas-MacBook-Pro sample-python % curl http://127.0.0.1:9000<br />
{"message":"Hello World Python v1"}%      <br />

   




