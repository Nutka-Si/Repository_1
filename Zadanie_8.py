import sys
import csv

plik_wejsciowy = sys.argv[1]
plik_wyjsciowy = sys.argv[2]

zmiany = sys.argv[3:]

dane = []

with open(plik_wejsciowy, newline="") as plik:
    reader = csv.reader(plik)

    for wiersz in reader:
        dane.append(wiersz)

for zmiana in zmiany:
    x, y, wartosc = zmiana.split(",")

    x = int(x)
    y = int(y)

    dane[y][x] = wartosc


for wiersz in dane:
    print(",".join(wiersz))

with open(plik_wyjsciowy, "w", newline="") as plik:
    writer = csv.writer(plik)

    for wiersz in dane:
        writer.writerow(wiersz)