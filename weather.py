import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_weather(city="Kyiv"):
    if not API_KEY:
        return {"error": "API key not found. Please set API_KEY in .env"}

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ua"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Не вдалося отримати дані. Перевірте назву міста."}

    data = response.json()
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"].capitalize(),
    }
