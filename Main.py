import sys
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit

API_KEY = '9cf865e60609b51b31f7385ea85594ff'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q=Tartu,EE&appid=9cf865e60609b51b31f7385ea85594ff&units=metric'


class WeatherThread(QThread):
    # Signal to emit the fetched weather information
    # This signal will be emitted when the weather data is fetched
    # and will be connected to the update_weather_info method in the main app
    weather_fetched = pyqtSignal(str)

    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        # This method runs in a separate thread to avoid blocking the GUI
        # Fetch the weather information for the specified city
        # and emit the result through the weather_fetched signal
        weather_info = self.get_weather(self.city)
        self.weather_fetched.emit(weather_info)

    def get_weather(self, city):
        try:
            params = {
                'q': f"{city},EE", # Append country code for Estonia
                'appid': API_KEY,  # Your OpenWeatherMap API key
                'units': 'metric'  # Use metric units for temperature
            }
            response = requests.get(BASE_URL, params=params, timeout=10)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

            if response.status_code == 200:
                data = response.json()
                city_name = data['name']
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                temp_min = data['main']['temp_min']
                temp_max = data['main']['temp_max']
                pressure = data['main']['pressure']
                humidity = data['main']['humidity']
                weather_description = data['weather'][0]['description']
                wind_speed = data['wind']['speed']
                wind_deg = data['wind']['deg']

                # Format the weather information
                # to be displayed in the text area
                weather_info = (f"{city_name} Weather:\n"
                                f"Temperature: {temp:.1f}°C (Feels like {feels_like:.1f}°C)\n"
                                f"Min Temp: {temp_min:.1f}°C, Max Temp: {temp_max:.1f}°C\n"
                                f"Weather: {weather_description.capitalize()}\n"
                                f"Pressure: {pressure} hPa\n"
                                f"Humidity: {humidity}%\n"
                                f"Wind Speed: {wind_speed} m/s, Direction: {wind_deg}°")
                return weather_info
            else:
                return f"{city}: Error {response.status_code}" # Handle non-200 responses

        except requests.exceptions.HTTPError as http_err:
            return f"{city}: HTTP error occurred: {http_err}"  # Handle HTTP errors
        except requests.exceptions.RequestException as req_err:
            return f"{city}: Request error occurred: {req_err}"  # Handle other request errors


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estonia Weather App (PyQt5)")
        self.setGeometry(100, 100, 600, 500)  # Set window size
        self.layout = QVBoxLayout()

        # Input field for city name
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter a city name")
        self.layout.addWidget(self.city_input)

        # Button to fetch weather data
        self.button = QPushButton("Fetch Weather")
        self.button.clicked.connect(self.fetch_weather)
        self.layout.addWidget(self.button)

        # Text area to display weather information
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.layout.addWidget(self.text_area)

        # Set the layout for the main window
        self.setLayout(self.layout)

    def fetch_weather(self):
        city = self.city_input.text().strip()
        if not city:
            self.text_area.setText("Please enter a city name.")
            return

        self.text_area.setText(f"Fetching weather data for {city}...\n\n")

        # Create a new thread to fetch weather data
        self.weather_thread = WeatherThread(city)
        # Connect the weather_fetched signal to the update_weather_info method
        self.weather_thread.weather_fetched.connect(self.update_weather_info)
        # Start the thread to fetch weather data
        self.weather_thread.start()

    def update_weather_info(self, weather_info):
        self.text_area.append(weather_info)
        self.text_area.append("\nDone.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
