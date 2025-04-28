#Estonia Weather App (PyQt5)

This is a simple weather application built using PyQt5 and the OpenWeatherMap API. The app allows users to fetch and display weather information for cities in Estonia.
Features

    Fetches real-time weather data using the OpenWeatherMap API.

    Displays temperature, weather description, pressure, humidity, wind speed, and more.

    User-friendly PyQt5 GUI with input for city names.

Prerequisites

    Python 3.x

    PyQt5

    requests library

    A valid OpenWeatherMap API key

Installation

    Clone or download this repository.

    Install the required Python libraries:

    bash

    pip install PyQt5 requests

    Replace the API_KEY variable in the code with your valid OpenWeatherMap API key.

Usage

    Run the application:

    bash

    python your_script_name.py

    Enter the name of a city in Estonia (e.g., "Tartu") in the input field.

    Click the "Fetch Weather" button to retrieve the weather data.

    The weather information will be displayed in the text area.

Code Overview
Main Components

    WeatherThread: A QThread subclass that handles the network request to fetch weather data in the background.

    WeatherApp: The main PyQt5 application window that provides the GUI for user interaction.

Key Functions

    get_weather(city): Fetches weather data for the specified city using the OpenWeatherMap API.

    fetch_weather(): Initiates the weather-fetching process when the "Fetch Weather" button is clicked.

    update_weather_info(weather_info): Updates the text area with the fetched weather information.

Example Output

When you fetch weather data for "Tartu", the output in the application’s text area might look like this:

yaml

Fetching weather data for Tartu...

Tartu Weather:
Temperature: 10.5°C (Feels like 8.7°C)
Min Temp: 10.2°C, Max Temp: 11.1°C
Weather: Overcast clouds
Pressure: 1017 hPa
Humidity: 42%
Wind Speed: 6.2 m/s, Direction: 240°

Done.

Troubleshooting

If you encounter any issues, check the following:

    API Key: Ensure that the OpenWeatherMap API key is valid and has sufficient permissions.

    Internet Connection: Make sure your machine is connected to the internet to fetch weather data.

    Invalid City: Ensure that the city name entered is correct, and make sure to enter it without extra spaces.
