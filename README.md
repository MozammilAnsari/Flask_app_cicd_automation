# 🚀 CI/CD Automation for Flask Application using Jenkins, Docker & AWS EC2

## 📌 Project Overview

This project demonstrates the implementation of a complete CI/CD (Continuous Integration and Continuous Deployment) pipeline for a Python Flask-based web application. The goal was to automate the build, test, and deployment process using modern DevOps tools like Jenkins, Docker, and AWS EC2, triggered via GitHub webhooks.

---

## 🛠️ Tech Stack

* **Backend:** Python Flask
* **Containerization:** Docker
* **CI/CD Tool:** Jenkins
* **Cloud Platform:** AWS EC2
* **Version Control:** Git & GitHub
* **Automation Trigger:** GitHub Webhooks

---

## ⚙️ Project Workflow

### 1. Application Development

* Developed a basic Flask web application.
* Ensured local testing and validation before deployment.
* Managed dependencies using `requirements.txt`.

---

### 2. Containerization using Docker

* Created a `Dockerfile` to containerize the Flask application.
* Built Docker image locally to verify correctness.
* Ensured portability and consistency across environments.

---

### 3. CI/CD Pipeline Setup (Jenkins)

* Installed and configured Jenkins on AWS EC2 instance.
* Created a Jenkins pipeline using a `Jenkinsfile`.
* Pipeline stages included:

  * Code checkout from GitHub
  * Build Docker image
  * Stop and remove previous container
  * Run new container with updated image

---

### 4. Cloud Deployment (AWS EC2)

* Launched an EC2 instance to host Jenkins and Docker.
* Configured security groups (opened ports like 8080 for Jenkins, 5000 for Flask).
* Installed Docker and configured permissions.

---

### 5. Webhook Integration

* Configured GitHub Webhook to trigger Jenkins automatically on code push.
* Connected webhook endpoint with Jenkins job.
* Enabled real-time automation for deployments.

---

### 6. Automated Deployment Flow

1. Developer pushes code to GitHub repository
2. GitHub Webhook triggers Jenkins pipeline
3. Jenkins pulls latest code
4. Docker image is rebuilt
5. Existing container is stopped and removed
6. New container is launched with updated code
7. Application is deployed automatically on EC2

---

## 🔁 CI/CD Pipeline Flow Diagram (Conceptual)

GitHub Push → Webhook → Jenkins Pipeline → Docker Build → Container Deployment → Live Application

---

## ✅ Key Achievements

* Fully automated deployment process with zero manual intervention
* Reduced deployment time significantly
* Ensured consistency across environments using Docker
* Enabled real-time updates via webhook integration

---

## ⚠️ Challenges Faced & Solutions

### 1. Docker Permission Issues in Jenkins

**Problem:** Jenkins was unable to run Docker commands (`docker: not found` or permission denied).
**Solution:** Added Jenkins user to Docker group and restarted services.

---

### 2. Webhook Not Triggering Pipeline

**Problem:** GitHub webhook was not triggering Jenkins job.
**Solution:**

* Verified webhook URL and payload
* Installed required Jenkins plugins (GitHub Integration)
* Opened required ports in EC2 security group

---

### 3. Port Conflicts During Deployment

**Problem:** New container failed to start due to port already in use.
**Solution:** Added step in pipeline to stop and remove existing container before running new one.

---

### 4. Docker Not Found in Jenkins Pipeline

**Problem:** Jenkins pipeline could not detect Docker installation.
**Solution:** Ensured Docker is installed on host and properly configured in Jenkins environment.

---

### 5. Debugging Blank Flask Page After Deployment

**Problem:** Application deployed but showed blank page.
**Solution:** Enabled debug mode, checked logs, verified templates and routing.

---

## 📈 Future Improvements

* Add **database integration (MySQL/PostgreSQL)**
* Implement **user authentication system**
* Integrate **monitoring tools (Prometheus + Grafana)**
* Use **Kubernetes for orchestration**
* Add **automated testing stage in pipeline**

---

## 🎯 Conclusion

This project successfully demonstrates an end-to-end CI/CD pipeline implementation using industry-standard tools. It highlights practical DevOps skills such as automation, containerization, cloud deployment, and troubleshooting real-world issues.

