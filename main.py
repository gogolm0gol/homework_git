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

    html = f"""
    <html>
        <head>
            <title>Weather App</title>
            <link rel="stylesheet" href="/static/styles.css">
        </head>
        <body>
            <div class="card">
                <h1>Weather in {city}</h1>
                <p class="temp">{temperature}°C</p>
                <p>{conditions}</p>
                <p>💧 Humidity: {humidity}%</p>
                <p>🌬 Wind: {wind_speed} m/s</p>
                <p>🕒 {time_now}</p>
                <a href="/about" class="link">About App</a>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.get("/about", response_class=HTMLResponse)
def about():
    html = """
    <html>
        <head>
            <title>About Weather App</title>
            <link rel="stylesheet" href="/static/styles.css">
        </head>
        <body>
            <div class="card">
                <h1>About Weather App</h1>
                <p>This simple FastAPI app shows random weather conditions for different Ukrainian cities 🇺🇦.</p>
                <p>Created by Sofiya as a learning project 💻</p>
                <a href="/" class="link">← Back to Weather</a>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html)
