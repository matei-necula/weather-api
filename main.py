from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Replace this with your actual weather fetching logic
def get_weather_data(city: str):
    return {
        "city": city.capitalize(),
        "country": "FR",
        "temperature_c": 9.62,
        "feels_like_c": 9.62,
        "humidity_pct": 71,
        "description": "clear sky",
        "wind_speed_ms": 1.03
    }

@app.get("/weather/{city}", response_class=HTMLResponse)
async def get_weather(city: str):
    weather = get_weather_data(city)
    
    # Create a styled HTML template
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather in {weather['city']}</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .weather-card {{
                background-color: white;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                padding: 40px;
                text-align: center;
                max-width: 350px;
                width: 100%;
            }}
            .weather-card h1 {{
                margin: 0;
                color: #333;
                font-size: 2em;
            }}
            .weather-card h2 {{
                margin: 5px 0 20px;
                color: #777;
                font-size: 1.2em;
                font-weight: normal;
            }}
            .temp {{
                font-size: 4em;
                font-weight: bold;
                color: #ff7e5f;
                margin: 10px 0;
            }}
            .description {{
                font-size: 1.5em;
                color: #555;
                text-transform: capitalize;
                margin-bottom: 20px;
            }}
            .details {{
                display: flex;
                justify-content: space-between;
                border-top: 1px solid #eee;
                padding-top: 20px;
                margin-top: 20px;
            }}
            .detail-item {{
                font-size: 0.9em;
                color: #666;
            }}
            .detail-item strong {{
                display: block;
                font-size: 1.2em;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <div class="weather-card">
            <h1>{weather['city']}</h1>
            <h2>{weather['country']}</h2>
            
            <div class="temp">{weather['temperature_c']}°C</div>
            <div class="description">{weather['description']}</div>
            
            <div class="details">
                <div class="detail-item">
                    <strong>{weather['feels_like_c']}°C</strong>
                    Feels Like
                </div>
                <div class="detail-item">
                    <strong>{weather['humidity_pct']}%</strong>
                    Humidity
                </div>
                <div class="detail-item">
                    <strong>{weather['wind_speed_ms']} m/s</strong>
                    Wind
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_content
