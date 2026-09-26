import sys
import csv
import json
import pickle

class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def change(self, x, y, value):
        self.data[y][x] = value

    def display(self):
        for row in self.data:
            print(row)


class CSVReader(Reader):
    def read(self):
        with open(self.filename, newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                self.data.append(row)

    def write(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            for row in self.data:
                writer.writerow(row)


class JSONReader(Reader):
    def read(self):
        with open(self.filename) as file:
            self.data = json.load(file)

    def write(self, filename):
        with open(filename, "w") as file:
            json.dump(self.data, file)

class TXTReader(Reader):
    def read(self):
        with open(self.filename) as file:
            for line in file:
                row = line.strip().split(",")
                self.data.append(row)

    def write(self, filename):
        with open(filename, "w") as file:
            for row in self.data:
                file.write(",".join(str(value) for value in row) + "\n")

class PickleReader(Reader):
    def read(self):
        with open(self.filename, "rb") as file:
            self.data = pickle.load(file)

    def write(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.data, file)

plik_wejsciowy = sys.argv[1]
plik_wyjsciowy = sys.argv[2]
zmiany = sys.argv[3:]

if plik_wejsciowy.endswith(".csv"):
    reader = CSVReader(plik_wejsciowy)
elif plik_wejsciowy.endswith(".json"):
    reader = JSONReader(plik_wejsciowy)
elif plik_wejsciowy.endswith(".txt"):
    reader = TXTReader(plik_wejsciowy)
elif plik_wejsciowy.endswith(".pickle"):
    reader = PickleReader(plik_wejsciowy)
else:
    raise ValueError("Nieobsługiwany format pliku wejściowego")
reader.read()

for zmiana in zmiany:
    x, y, wartosc = zmiana.split(",")
    x = int(x)
    y = int(y)

    reader.change(x, y, wartosc)

reader.display()

try:
    if plik_wyjsciowy.endswith(".csv"):
        writer = CSVReader(plik_wyjsciowy)
    elif plik_wyjsciowy.endswith(".json"):
        writer = JSONReader(plik_wyjsciowy)
    elif plik_wyjsciowy.endswith(".txt"):
        writer = TXTReader(plik_wyjsciowy)
    elif plik_wyjsciowy.endswith(".pickle"):
        writer = PickleReader(plik_wyjsciowy)
    else:
        raise ValueError("Nieobsługiwany format pliku wyjściowego")

    writer.data = reader.data
    writer.write(plik_wyjsciowy)

except ValueError as error:
    print(error)