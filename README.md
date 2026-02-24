# Simple DevOps Learning Project

This repository contains a minimal Flask application to help you learn Docker and Kubernetes.

## Structure

- `app.py` – simple Flask web app that returns `Hello DevOps! 🚀`.
- `Dockerfile` – builds a container image for the app.
- `requirements.txt` – Python dependencies.
- `k8s/` – Kubernetes manifests (Deployment & Service).

## Getting Started

### Prerequisites

- Docker (or Docker Desktop)
- kubectl
- A Kubernetes cluster (e.g. [Minikube](https://minikube.sigs.k8s.io/), Docker Desktop, or GKE/EKS/AKS)

### Build & Run with Docker

1. Build the image:
   ```sh
   docker build -t devops-flask:latest .
   # or tag with your registry: docker build -t <username>/devops-flask:latest .
   ```
2. Run container locally:
   ```sh
   docker run --rm -p 5000:5000 devops-flask:latest
   ```
3. Visit <http://localhost:5000> to see the message.

### Push to a Registry

1. Tag and push:
   ```sh
   docker tag devops-flask:latest <username>/devops-flask:latest
   docker push <username>/devops-flask:latest
   ```
2. Update `k8s/deployment.yaml` image field to match the pushed image.

### Deploy to Kubernetes

```sh
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check pods and service status:
```sh
kubectl get pods
kubectl get svc
```

### Cleanup

```sh
kubectl delete -f k8s/service.yaml -f k8s/deployment.yaml
```