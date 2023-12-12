# Docker Server and Client Application

This project contains a Dockerized server and client application who will communicate with each other. The server generates a 1KB file with random text data and its checksum, and the client downloads this file and verifies it against the checksum.

## Project Structure

- `/server`: Contains the Dockerfile and source code for the server application.
- `/client`: Contains the Dockerfile and source code for the client application.

## Prerequisites

- Docker installed on your machine.
- Basic knowledge of Docker command-line usage.

## Getting Started

### Build & Run Server Container 

1. **Navigate to the Server Directory:**

```
cd server
```

2. **Build the Docker Image for the Server:**

```
docker build -t server-image .

```

3. **Run the Server Container:**

```
docker run -d --name server -v servervol:/serverdata -p 9000:9000 my-server-image
```

This command will start the server on host machine on port 9000.

### Build & Run the Client Container

1. **Navigate to the Client Directory:**


```
cd ../client

```


2. **Build the Docker Image for the Client:**


```
docker build -t my-client-image .

```

3. **Run the Client Container:**


```
docker run -d --name client -v clientvol:/clientdata my-client-image

```

The client will automatically connect to the server and perform its operations.

## Verify communication between client and server

To verify the checksum and ensure the file transfer was successful, check the client and server logs.

1. **Check the server status and logs:**

```
docker ps -a 
docker logs <server_container_id>

```
The server should receive response 200 for '/download' and '/checksum' requests

2. **Check the client status and logs:**

```
docker ps -a 
docker logs <client_container_id>

```
The client logs should contain the verification success message.

## Verify communication through interactive console

To verify whether the downloaded file exists in the mounted directory, you can access the shell of the client container in interactive mode.


1. **Run the Client Container in Interactive Mode:**

This will display the output from the client, including the verification result of the downloaded file's checksum.

```
docker run -it --name client-container -v clientvol:/clientdata client-image /bin/bash
```

2. **Navigate to the data directory, run the python file an verify the file:**

```
python 'client.py'
cd /clientdata
ls
cat received_file.txt  # Replace with your file name
```



## Notes

- Ensure that Docker is running on your machine before executing any Docker commands.
- The commands provided are for a basic setup. Adjust the port numbers and volume names as per your specific requirements.

