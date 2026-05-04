# Weather API App - README 🌤️

Here's a clean, complete README file for your project:

```markdown
# 🌤️ Weather API App

A Python command-line app that fetches real-time weather data
for any city using the OpenWeatherMap API.

---

## 📋 Description

Enter any city name and instantly get live weather information
including temperature, humidity, wind speed, and a short
weather description — all pulled from a real weather API.

---

## 🚀 Features

- 🔍 Search weather by any city name
- 🌡️ Displays temperature in Celsius
- 💧 Shows humidity percentage
- 💨 Shows wind speed (m/s)
- 🌥️ Gives a weather description (e.g. "light rain")
- ⚠️ Handles invalid city names gracefully

---

## 🛠️ Requirements

- Python 3.x
- `requests` library
- Free OpenWeatherMap API key

---

## 📦 Installation

1. Clone or download this repository:
   git clone https://github.com/yourname/weather-api-app.git
   cd weather-api-app

2. Install the required library:
   pip install requests

3. Get your free API key:
   - Go to https://openweathermap.org
   - Sign up for a free account
   - Go to API Keys section in your dashboard
   - Copy your key

4. Add your API key to the script:
   Open weather_app.py and replace:
   API_KEY = "your_api_key_here"
   with your actual key.

---

## ▶️ Usage

Run the script from your terminal:

   python weather_app.py

Then follow the prompt:

   Enter city name: London

   ------------------------------------
   🌤️  Weather in London
   ------------------------------------
   🌡️  Temperature : 18.4°C
   💧  Humidity    : 72%
   💨  Wind Speed  : 3.6 m/s
   🌥️  Description : light rain
   ------------------------------------

---

## 📁 Project Structure

   weather-api-app/
   │
   ├── weather_app.py       # Main Python script
   ├── README.md            # Project documentation
   └── requirements.txt     # Dependencies

---

## 📄 requirements.txt

   requests

---

## 🔑 API Reference

This app uses the OpenWeatherMap Current Weather