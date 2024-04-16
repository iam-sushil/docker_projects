# Get base image with openjdk
FROM openjdk:23-slim-bullseye

# Creating a working directory to run and compile the code
WORKDIR /app

# Copy source code to docker container
COPY Hello.java .

# Compile the code
RUN javac Hello.java


# run the java app
CMD ["java", "Hello"]
