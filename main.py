from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
from datetime import datetime

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return show_weather()


@app.get("/about", response_class=HTMLResponse)
def about():
    html = """
    <html>
        <head>
            <title>About | Weather App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(to top right, #89f7fe, #66a6ff);
                    color: #333;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    text-align: center;
                }
                .card {
                    background: white;
                    padding: 30px;
                    border-radius: 20px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
                    width: 400px;
                }
                a {
                    color: #0077ff;
                    text-decoration: none;
                    font-weight: bold;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>About Weather App</h1>
                <p>This app shows random weather data for different Ukrainian cities 🌦</p>
                <p>Created with ❤️ using FastAPI.</p>
                <a href="/">⬅ Back to Home</a>
            </div>
        </body>
    </html>
    """
    return html


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
                    width: 300px;
                }}
                h1 {{
                    color: #0077ff;
                }}
                .temp {{
                    font-size: 40px;
                    margin: 10px 0;
                }}
                a {{
                    color: #0077ff;
                    text-decoration: none;
                    font-weight: bold;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Weather in {city}</h1>
                <p class="temp">{temperature}°C</p>
                <p>{conditions}</p>
                <p>💧 Humidity: {humidity}%</p>
                <p>🌬 Wind: {wind_speed} m/s</p>
                <p>🕒 {time_now}</p>
                <a href="/about">ℹ About</a>
            </div>
        </body>
    </html>
    """
    return html
