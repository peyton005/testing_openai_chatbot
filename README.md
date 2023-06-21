# testing_openai_chatbot

This is a simple python program which tests the `openai` API tools library recently published

## Steps for creating and deploying a **local** docker image onto a minikube kluster

1. Make sure you have properly downloaded all the necessary packages you will be using. In this case, I downloaded docker and minikube.
2. Create a directory containing your application (In this case I used a python application testing the cohere API).
3. Create a Dockerfile within the current working directory with information specifying what dependencies should be downloaded upon the creation of your local image.
4. Run the command `docker build -t [name for your image] .` in order to build your Docker image with a specified name. This image will be stored within the local machine's docker image repository.
5. Next, you can start the container using the image you just created in order to test that it runs properly with the command `docker run [image name]`.
6. Create a .yml file in your current working directory using the documentation on the kubernetes deployments web page. Make sure to add `imagePullPolicy: Never` under `containers:` to avoid pulling the image you specify from the external docker hub.
7. Finally, you can deploy the container with the specifications within the .yml file onto the cluster with the command `kubectl apply -f [file name]`
