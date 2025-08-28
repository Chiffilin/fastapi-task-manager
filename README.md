# 🚀 FastAPI Task Manager

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Docker](https://img.shields.io/badge/Docker-✓-blue)
![Tests](https://img.shields.io/badge/Tests-Passing-green)
![Coverage](https://codecov.io/gh/your-username/fastapi-task-manager/branch/main/graph/badge.svg)

A modern, production-ready Task Management API built with FastAPI, PostgreSQL, and Docker.

## ✨ Features

- ✅ RESTful API with CRUD operations
- ✅ PostgreSQL database with SQLAlchemy ORM
- ✅ JWT Authentication & Authorization
- ✅ Docker containerization
- ✅ Automated testing with pytest
- ✅ CI/CD with GitHub Actions
- ✅ Code coverage with Codecov
- ✅ Interactive API documentation

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.12+
- Docker and Docker Compose
- UV package manager

### Development
```bash
# Clone the repository
git clone https://github.com/Chiffilin/fastapi-task-manager.git
cd fastapi-task-manager
```
```bash
# Install dependencies
uv sync
```
```bash
# Run with Docker
docker-compose up --build
```

```bash
# Or run locally
uvicorn app.main:app --reload
```

### API Documentation
Once running, access the interactive docs:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📚 API Endpoints
| Method    | Endpoint          | Description           
|-----------|-------------------|-----------------------|
| GET       | /tasks            | Get all tasks         |
| POST      | 	/tasks          | 	Create new task   |
| GET       | /tasks/{id}	    | Get task by ID        |
| PUT	    | /tasks/{id}       | 	Update task       |
| DELETE	| /tasks/{id}       | 	Delete task       |

## 🧪 Testing
```bash
# Run tests
uv run pytest -v
```
```bash
# Run with coverage
uv run pytest --cov=app --cov-report=html
```
```bash
# Run in Docker
docker-compose run app uv run pytest -v
```
## 🛠️ Development
```Project Structure
app/
├── api/
│   └── routers/          # API endpoints
├── core/                 # Configuration
├── db/                   # Database setup
├── models/               # SQLAlchemy models
├── schemas/              # Pydantic schemas
└── tests/                # Test cases
```

## 📦 Deployment

The application is Docker-ready and can be deployed to:
 - AWS ECS/EKS
- Google Cloud Run
- Heroku
- Railway

## 🤝 Contributing
1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](https://license/) file for details.

## 🙏 Acknowledgments
- FastAPI team for the excellent framework
- PostgreSQL for reliable database
- Docker for containerization
- Pytest for testing framework
