# Containerized Weather API

A RESTful weather API built with Python and FastAPI, containerized with Docker, and automatically deployed via GitHub Actions. Built as a first-year DevOps project to demonstrate the full software lifecycle: write, version, containerize, and automate.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python + FastAPI | API framework |
| Docker | Containerization |
| GitHub Actions | CI/CD pipeline |
| Git | Version control |
| OpenWeatherMap API | Weather data source |

---

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| GET | `/weather/{city}` | Current weather for a city |
| GET | `/docs` | Interactive Swagger UI |

**Example response** for `/weather/London`:
```json
{
  "city": "London",
  "country": "GB",
  "temperature_c": 12.3,
  "feels_like_c": 10.1,
  "humidity_pct": 82,
  "description": "overcast clouds",
  "wind_speed_ms": 4.6
}
```

---

## Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/matei-necula/weather-api.git
cd weather-api
```

**2. Create a `.env` file**
```bash
OPENWEATHER_API_KEY=your_api_key_here
```

**3. Install dependencies and run**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` to explore the API.

---

## Run with Docker

```bash
docker pull matei-necula/weather-api:latest

docker run -p 8000:8000 \
  -e OPENWEATHER_API_KEY=your_api_key_here \
  matei-necula/weather-api:latest
```

---

## CI/CD Pipeline

Every push to `main` triggers a GitHub Actions workflow that:
1. Checks out the code
2. Logs in to Docker Hub using repository secrets
3. Builds the Docker image
4. Pushes it to Docker Hub automatically

---

## Project Structure

```
weather-api/
├── main.py               # FastAPI application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container definition
├── .env                  # API key (not committed)
├── .gitignore            # Ignored files
└── .github/
    └── workflows/
        └── docker.yml    # GitHub Actions pipeline
```

---

## Getting an API Key

1. Create a free account at [openweathermap.org](https://openweathermap.org)
2. Go to **API Keys** in your account dashboard
3. Copy your key and paste it into `.env`
