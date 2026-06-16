# Day 40 – Cloud Deployment Strategy

## Deployment Target

Enterprise RAG Platform

## Architecture

User
↓
Load Balancer
↓
FastAPI Application
↓
ChromaDB Vector Store
↓
Document Storage
↓
LLM Provider (Gemini/OpenAI)

## AWS Deployment Option

Services:

* EC2
* Application Load Balancer
* S3
* CloudWatch

Container Runtime:

* Docker
* Docker Compose

Benefits:

* Full control
* Industry standard
* Scalable

## Azure Deployment Option

Services:

* Azure App Service
* Azure Container Apps
* Azure Blob Storage
* Azure Monitor

Container Runtime:

* Docker

Benefits:

* Managed deployment
* Easy CI/CD integration

## Environment Strategy

Development

* Local machine

Testing

* Docker Compose

Production

* AWS or Azure

## Deployment Steps

1. Build Docker image
2. Push image to registry
3. Provision cloud service
4. Configure environment variables
5. Deploy container
6. Configure monitoring
7. Verify application health

Status:
Deployment strategy completed.
