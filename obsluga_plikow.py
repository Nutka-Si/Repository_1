def zapisz_dane(stan_konta, Magazyn, historia):
    with open("dane.txt", "w") as plik:
        plik.write(str(stan_konta) + "\n")

        for produkt in Magazyn:
            plik.write(
                produkt["nazwa_produktu"] + ";"
                + str(produkt["cena w zł"]) + ";"
                + str(produkt["ilość"]) + "\n"
            )

        plik.write("HISTORIA\n")

        for operacja in historia:
            plik.write(operacja + "\n")

def odczytaj_dane():
    with open("dane.txt") as plik:
        linie = plik.readlines()

    stan_konta = float(linie[0])
    Magazyn = []
    historia = []

    czy_historia = False

    for linia in linie[1:]:
        linia = linia.strip()

        if linia == "HISTORIA":
            czy_historia = True
            continue

        if czy_historia == False:
            dane = linia.split(";")

            produkt = {
                "nazwa_produktu": dane[0],
                "cena w zł": float(dane[1]),
                "ilość": int(dane[2])
            }

            Magazyn.append(produkt)

        else:
            historia.append(linia)

    return stan_konta, Magazyn, historia