from flask import Flask, request, jsonify, render_template
import requests
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Define a function to fetch weather data from WeatherAPI
#https://api.weatherapi.com/v1/future.json?key=7e1682484e304737beb50642240403&q=Chennai&dt=2024-03-20
#https://api.weatherapi.com/v1/forecast.json?key=7e1682484e304737beb50642240403&q=Chennai&alert=yes
#https://api.weatherapi.com/v1/history.json?key=7e1682484e304737beb50642240403&q=chennai&dt=2023-08-29

def fetch_weather_data(api_key, city_name):
    url = f'https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city_name}&alert=yes'
    response = requests.get(url)
    data = response.json()
    return data

# Define a function to preprocess weather data
def preprocess_weather_data(data):
    # Extract relevant features
    weather = {
        'temp_min': data['forecast']['forecastday'][0]['day']['mintemp_c'],
        'temp_max': data['forecast']['forecastday'][0]['day']['maxtemp_c'],
        'rain': data['current']['precip_mm'],
        'humidity': data['current']['humidity'],
        'pressure': data['current']['pressure_mb'],
        'wind_speed': data['current']['wind_kph'],
        'clouds': data['current']['cloud'] / 10
    }

    temp_min = weather['temp_min']
    temp_max = weather['temp_max']
    rain = weather['rain']
    humidity = weather['humidity']
    pressure = weather['pressure']
    wind_speed = weather['wind_speed']
    clouds = weather['clouds']

    input_data = pd.DataFrame({
        'temp_min': [temp_min],
        'temp_max': [temp_max],
        'rain': [rain],
        'wind_speed': [wind_speed],
        'humidity': [humidity],
        'pressure': [pressure],
        'clouds': [clouds]
    })
    return input_data

# Load ML model
model = joblib.load('model.joblib')  # Use the path to your model file

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle form submission and predict cloudburst
@app.route('/predict', methods=['POST'])
def predict():
    # Get city name from the form field
    city_name = request.form['city_name']
    if not city_name:
        return render_template('index.html', prediction_text='City name is required')

    # Fetch weather data
    weather_data = fetch_weather_data('7e1682484e304737beb50642240403', city_name)

    # Preprocess weather data
    processed_data = preprocess_weather_data(weather_data)

    # Make prediction
    prediction = model.predict(processed_data)
    prediction_text = 'Cloudburst' if prediction else 'No Cloudburst'

    # Pass weather data and prediction result to the template
    return render_template('index.html', weather_data=weather_data, city_name=city_name, prediction_text=prediction_text)


if __name__ == '__main__':
    app.run(debug=True)
