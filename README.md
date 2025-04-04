# Docker Flask MySQL Project with Jenkins CI/CD

## Overview
This project is a **Flask** web application that connects to a **MySQL database** inside a **Docker container**. The setup uses **Docker Compose** to manage the containers and integrates **Jenkins CI/CD** for automated deployment.

## Features
- Flask web application with a simple UI
- MySQL database integration
- Dockerized setup using `docker-compose`
- Data persistence with Docker volumes
- Jenkins pipeline for CI/CD automation

## Project Structure
```
docker-flask-mysql/
│── app/
│   ├── app.py                   # Flask application
│   ├── templates/
│   │   ├── index.html           # HTML UI page
│   ├── requirements.txt         # Dependencies
│   ├── Dockerfile               # Docker image for Flask app
│── docker-compose.yml           # Docker Compose file
│── .env                         # Environment variables
│── jenkins/
│   ├── Jenkinsfile              # Jenkins pipeline script
│── README.md                    # Project documentation
```

## Prerequisites
Make sure you have the following installed:
- **Docker**
- **Docker Compose**
- **Jenkins** (with necessary plugins)
- **Git**
- **MySQL client** (optional, for debugging)

## Installation and Setup
### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd <repo_name>

### Step 2: Set Up Environment Variables
Create a `.env` file

### Step 3: Create the Flask Application
Inside `app/app.py`, create a basic Flask app:

### Step 4: Create the Dockerfile for Flask
Inside `app/Dockerfile`:

### Step 5: Define Services in Docker Compose
Create `docker-compose.yml

### Step 6: Build and Run the Docker Containers
```bash
docker-compose up --build -d
```
This will start the Flask app and MySQL database in the background.

### Step 7: Verify the Setup
Check running containers:
```bash
docker ps
```
Access the Flask app at: `http://<your-ec2-ip>:5000`

### Step 8: Connect to MySQL (Optional)
```bash
docker exec -it <mysql-container-id> mysql -u <user> -p <password> mydb
```

## Jenkins CI/CD Setup
### Step 1: Install Jenkins Plugins
Ensure the following Jenkins plugins are installed:
- **Docker Pipeline**
- **Pipeline**
- **Git**
- **Docker Build and Publish**

### Step 2: Configure Jenkins Pipeline
1. Open Jenkins and create a new **Pipeline** project.
2. In the project settings, set the **Git repository URL**.
3. Add a **Jenkinsfile** inside the repository to automate build and deployment.
4. save the pipeline and run the build.

## Stopping the Containers
To stop the containers, run:
```bash
docker-compose down
```

## Testing the Application
After deployment, test the API using:
```bash
curl http://<your-ec2-ip>:5000
```

## Conclusion
This project demonstrates how to build a **Flask + MySQL** application using **Docker** and automate deployments with **Jenkins CI/CD**.
