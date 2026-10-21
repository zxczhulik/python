import requests


class Geocoder:
    BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"
    
    def find(self, city):

        params = {
            "name": city,
            "count": 1,
            "language": "ru",
            "format": "json"
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        if "results" not in data:
            return None

        place = data["results"][0]
        return {
            "name": place["name"],
            "country": place.get("country", ""),
            "latitude": place["latitude"],
            "longitude": place["longitude"],
        }


class WeatherClient:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_current(self, latitude, longitude):
        """Возвращает словарь с temperature, humidity, wind."""
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone": "auto"
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        current = data["current"]

        return {
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind": current["wind_speed_10m"],
        }


class WeatherApp:

    def __init__(self):
        self.geocoder = Geocoder()
        self.weather = WeatherClient()

    def run(self):
        city = input("Введите город: ")

        place = self.geocoder.find(city)
        if place is None:
            print("Город не найден.")
            return

        current = self.weather.get_current(place["latitude"], place["longitude"])

        print(f"Погода в {place['name']}, {place['country']}:")
        print(f"Температура: {current['temperature']}°C")
        print(f"Влажность: {current['humidity']}%")
        print(f"Ветер: {current['wind']} км/ч")


if __name__ == "__main__":
    app = WeatherApp()
    app.run()