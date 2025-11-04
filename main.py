from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
from datetime import datetime

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def show_weather():
    cities = ["Kyiv", "Odesa", "Lviv", "Kharkiv", "Dnipro", "Uzhhorod", "Chernihiv"]
    city = random.choice(cities)
    temperature = random.randint(-5, 35)
    conditions = random.choice(["☀️ Sunny", "🌧 Rainy", "⛅ Cloudy", "❄️ Snowy", "🌩 Stormy", "🌫 Foggy"])
    humidity = random.randint(30, 90)
    wind_speed = round(random.uniform(1.0, 12.0), 1)
    time_now = datetime.now().strftime("%H:%M:%S")

    # додаємо визначення пори року
    if temperature < 0:
        season = "❄ Winter"
    elif temperature < 15:
        season = "🌸 Spring"
    elif temperature < 25:
        season = "☀ Summer"
    else:
        season = "🍂 Autumn"

    html = f"""
    <html>
        <head>
            <title>Weather App</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(to top right, #89f7fe, #66a6ff);
                    color: #333;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    text-align: center;
                }}
                .card {{
                    background: white;
                    padding: 30px;
                    border-radius: 20px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
                    width: 320px;
                }}
                h1 {{
                    color: #0077ff;
                }}
                .temp {{
                    font-size: 40px;
                    margin: 10px 0;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Weather in {city}</h1>
                <p class="temp">{temperature}°C</p>
                <p>{conditions}</p>
                <p>{season}</p>
                <p>💧 Humidity: {humidity}%</p>
                <p>🌬 Wind: {wind_speed} m/s</p>
                <p>🕒 {time_now}</p>
            </div>
        </body>
    </html>
    """
    return html
