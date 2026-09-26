import requests
from datetime import datetime, timedelta

searched_date = input("Podaj datę w formacie YYYY-mm-dd: ")

if searched_date == "":
    jutro = datetime.today() + timedelta(days=1)
    searched_date = jutro.strftime("%Y-%m-%d")
print("Sprawdzam pogodę dla:", searched_date)

opady = None

with open("pogoda.txt", "r") as plik:
    for linia in plik:
        if linia.strip() != "":
            data, zapisane_opady = linia.strip().split(",")

            if data == searched_date:
                opady = float(zapisane_opady)



if opady is None:
    url = f"https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"

    response = requests.get(url)

    dane = response.json()

    if "daily" in dane:
        opady = dane["daily"]["rain_sum"][0]
    else:
        opady = -1

    with open("pogoda.txt", "a") as plik:
        plik.write(searched_date + "," + str(opady) + "\n")



if opady > 0.0:
    print("Będzie padać")
elif opady == 0.0:
    print("Nie będzie padać")
else:
    print("Nie wiem")

