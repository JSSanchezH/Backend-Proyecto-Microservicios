# Backend-Proyecto-Microservicios

This project is a simple **Human Resources Management System (HRMS)** backend prototype built using [FastAPI](https://fastapi.tiangolo.com/) and [SQLAlchemy](https://www.sqlalchemy.org/).  
The goal is to manage companies, employees, departments, roles, payroll, and absences — all inside a scalable Python API.

---

## 🏗️ Project Structure

├── fastapi/ │ ├── Dockerfile # Docker configuration for the FastAPI app │ ├── main.py # The entire FastAPI application logic │ └── requirements.txt # Python dependencies ├── traefik/ │ └── traefik.yml # Reverse proxy and routing rules ├── docker-compose.yml # Docker orchestration file └── README.md # This documentation

---

## 🚀 Quick Start

1️⃣ **Clone the repository**

```bash
git clone https://github.com/JSSanchezH/Backend-Proyecto-Microservicios
cd Backend-Proyecto-Microservicios

2️⃣ Run the stack using Docker Compose

docker-compose up --build

⚙️ Tech Stack

FastAPI — high-performance Python web framework for APIs.

SQLAlchemy — ORM to handle relational database models.

MySQL — Database (used with Docker container).

Traefik — Reverse proxy and load balancer.

Docker — For containerized deployment.

🧠 Models Overview
This prototype includes these data models:

Company — stores company details.

UserCompany — login data linked to companies.

Location — continent, country, state, city.

Department — company departments.

Employee — personal and job info.

Evaluation — performance evaluation metrics.

History — records employee exit reasons.

Schedule — working hours.

Payroll — salary and payment data.

PaymentMethod — defines how payments are processed.

AbsenceType — types of absences.

WorkAbsence — records employee absences.
```

🐳 Docker Commands
To rebuild containers after changes:

docker-compose down
docker-compose up --build

To stop services:

docker-compose down
