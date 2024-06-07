# Flask E-commerce Project (Portfolio)

This is a sample e-commerce application built with Flask, designed to showcase my skills in web development, database management, and cloud technologies. The project is containerized and orchestrated using Kubernetes (Minikube) for a single-node demonstration.

## Features

* **User Management:** Create and manage user accounts (PostgreSQL).
* **Product Catalog:** Browse and search through a catalog of items (MongoDB).
* **Shopping Cart:** Add items to cart and manage your shopping session (Redis, periodically synced to MongoDB).
* **Containerization:** All components are containerized for easy deployment and scalability.
* **Kubernetes Orchestration (Minikube):**  The application is deployed and managed using Minikube for demonstration purposes.

## Optional Features (Not included in this portfolio version)

* **Logging with ELK Stack:** Centralized logging for monitoring and troubleshooting.
* **Monitoring with Prometheus and Grafana:** Real-time monitoring of application performance and health.

## Technologies Used

* **Backend:** Flask (Python), PostgreSQL, MongoDB, Redis
* **Containerization:** Docker
* **Orchestration:** Kubernetes (Minikube)

## Getting Started

1. **Prerequisites:**
   - Docker
   - Minikube
   - Kubectl

2. **Start Minikube:**
   ```bash
   minikube start
3. **Apply K8s manifests**
   ```bash
   kubectl apply -f deployment/
4. **Access the application**
   ```bash
   minikube service flask-app
hierarchy (if it not like this for now it will be. Trust me)

    mongo-mongo-mongo/
    ├── app/
    │   ├── __init__.py 
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── user.py          # PostgreSQL models
    │   │   ├── item.py          # MongoDB models
    │   │   ├── cart.py
    │   ├── routes/ 
    │   │   ├── __init__.py
    │   │   ├── auth.py         # Authentication routes
    │   │   ├── items.py
    │   │   ├── cart.py
    │   ├── config.py
    │   ├── utils/              # Helper functions
    │   │   ├── __init__.py
    │   │   ├── database.py
    │   │   ├── cache.py
    ├── tests/                 
    │   ├── __init__.py         
    │   ├── test_auth.py
    │   ├── test_items.py       
    │   ├── test_cart.py
    ├── docker-compose.yml      # For local development with containers
    ├── logging.conf            # For ELK stack
    ├── prometheus.yml          # For Prometheus configuration
    ├── grafana/                # Grafana dashboards 
    ├── deployment/             # Kubernetes manifests
    │   ├── deployment.yaml 
    │   ├── service.yaml 
    ├── README.md  