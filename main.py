import os
import requests
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

load_dotenv()  # reads your .env file

app = FastAPI(title="Weather API", version="1.0.0")

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.get("/")
def root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Weather API is running"}


@app.get("/weather/{city}")
def get_weather(city: str):
    """Get current weather for a city."""
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API key not configured")

    response = requests.get(BASE_URL, params={
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # celsius
    })

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail=f"City '{city}' not found")

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Weather service error")

    data = response.json()

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature_c": data["main"]["temp"],
        "feels_like_c": data["main"]["feels_like"],
        "humidity_pct": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind_speed_ms": data["wind"]["speed"]
    }
