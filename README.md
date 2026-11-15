
# CI/CD Demo Application

## Project Overview
A containerised Flask web application deployed
automatically to Google Cloud Run using GitHub Actions.

## Technologies
- Python 3.12
- Flask
- Docker
- GitHub
- GitHub Actions
- Google Artifact Registry
- Google Cloud Run
- Pytest
- Postman

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Homepage |
| GET | /health | Health check |
| GET | /api/info | Application information |
| POST | /api/echo | JSON echo API |

## Local Installation

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest -v

Start application:

python app.py

Application URL:

http://localhost:8080
