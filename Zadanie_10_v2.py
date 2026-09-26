import requests
from datetime import datetime, timedelta


class WeatherForecast:

    def __init__(self, filename):
        self.filename = filename
        self.forecasts = {}

        with open(self.filename, "r") as plik:
            for linia in plik:
                if linia.strip() != "":
                    date, rain = linia.strip().split(",")
                    self.forecasts[date] = float(rain)

    def __setitem__(self, date, rain):
        self.forecasts[date] = rain

        with open(self.filename, "a") as plik:
            plik.write(date + "," + str(rain) + "\n")

    def __getitem__(self, date):

        if date in self.forecasts:
            return self.forecasts[date]

        url = f"https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01&daily=rain_sum&timezone=Europe%2FLondon&start_date={date}&end_date={date}"

        response = requests.get(url)
        dane = response.json()

        if "daily" in dane:
            rain = dane["daily"]["rain_sum"][0]
        else:
            rain = -1

        self[date] = rain

        return rain

    def __iter__(self):
        for date in self.forecasts:
            yield date

    def items(self):
        for date in self.forecasts:
            yield date, self.forecasts[date]


weather_forecast = WeatherForecast("pogoda.txt")

searched_date = input("Podaj datę w formacie YYYY-mm-dd: ")

if searched_date == "":
    jutro = datetime.today() + timedelta(days=1)
    searched_date = jutro.strftime("%Y-%m-%d")

print("Sprawdzam pogodę dla:", searched_date)

opady = weather_forecast[searched_date]

if opady > 0.0:
    print("Będzie padać")
elif opady == 0.0:
    print("Nie będzie padać")
else:
    print("Nie wiem")