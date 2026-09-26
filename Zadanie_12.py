from obsluga_plikow import zapisz_dane, odczytaj_dane

class Manager:
    def __init__(self):
        self.stan_konta, self.magazyn, self.historia = odczytaj_dane()
        self.actions = {}

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb

        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Nie ma takiej komendy")
        else:
            self.actions[name](self)


manager = Manager()

@manager.assign(1)
def saldo(manager):
    print("Podaj kwotę do dodania lub odjęcia:")
    kwota = float(input())

    manager.stan_konta += kwota
    manager.historia.append(f"SALDO: {kwota} zł")

    print(f"Stan konta wynosi: {manager.stan_konta} zł")
    print("\n")

@manager.assign(2)
def sprzedaz(manager):
    print("SPRZEDAŻ")
    print("Podaj nazwę produktu:")
    nazwa = input()
    print("Podaj cenę produktu:")
    cena = float(input())
    print("Podaj liczbę sztuk:")
    ilosc = int(input())

    if cena <= 0 or ilosc <= 0:
        print("Cena i liczba sztuk muszą być większe od zera")
        return

    znaleziono = False

    for produkt in manager.magazyn:
        if produkt["nazwa_produktu"] == nazwa and produkt["cena w zł"] == cena:
            znaleziono = True

            if produkt["ilość"] >= ilosc:
                print("Znaleziono produkt")
                print("Można wykonać sprzedaż")

                produkt["ilość"] -= ilosc
                wartosc_sprzedazy = cena * ilosc
                manager.stan_konta += wartosc_sprzedazy

                manager.historia.append(
                    f"SPRZEDAŻ: {nazwa}, {ilosc} szt., {wartosc_sprzedazy} zł"
                )
            else:
                print("Brak wystarczającej liczby sztuk w magazynie")

    if znaleziono == False:
        print("Nie znaleziono takiego produktu")

@manager.assign(3)
def zakup(manager):
    print("ZAKUP")
    print("Podaj nazwę produktu:")
    nazwa = input()
    print("Podaj cenę produktu:")
    cena = float(input())
    print("Podaj liczbę sztuk:")
    ilosc = int(input())

    if cena <= 0 or ilosc <= 0:
        print("Cena i liczba sztuk muszą być większe od zera")
        return

    wartosc_zakupu = cena * ilosc

    if manager.stan_konta >= wartosc_zakupu:
        manager.stan_konta -= wartosc_zakupu
        znaleziono = False

        for produkt in manager.magazyn:
            if produkt["nazwa_produktu"] == nazwa and produkt["cena w zł"] == cena:
                produkt["ilość"] += ilosc
                znaleziono = True

        if znaleziono == False:
            nowy_produkt = {
                "nazwa_produktu": nazwa,
                "cena w zł": cena,
                "ilość": ilosc
            }
            manager.magazyn.append(nowy_produkt)

        print("Zakup został wykonany")
        manager.historia.append(
            f"ZAKUP: {nazwa}, {ilosc} szt., {wartosc_zakupu} zł"
        )
        print(f"Stan konta wynosi: {manager.stan_konta} zł")

    else:
        print("Brak wystarczających środków na koncie")

@manager.assign(4)
def konto(manager):
    print("KONTO")
    print(f"Stan konta wynosi: {manager.stan_konta} zł")
    print("\n")


@manager.assign(5)
def lista(manager):
    print("LISTA PRODUKTÓW")

    for produkt in manager.magazyn:
        print(f"Nazwa: {produkt['nazwa_produktu']}, "
              f"cena: {produkt['cena w zł']} zł, "
              f"ilość: {produkt['ilość']} szt.")

    print("\n")

@manager.assign(6)
def magazyn(manager):
    print("MAGAZYN")
    print("Podaj nazwę produktu:")
    nazwa = input()
    znaleziono = False

    for produkt in manager.magazyn:
        if produkt["nazwa_produktu"] == nazwa:
            print(f"Produkt: {produkt['nazwa_produktu']}, "
                  f"ilość: {produkt['ilość']} szt.")
            znaleziono = True

    if znaleziono == False:
        print("Nie znaleziono takiego produktu")

    print("\n")

@manager.assign(7)
def przeglad(manager):
    print("PRZEGLĄD")
    print("Podaj indeks OD (Enter = od początku):")
    od = input()
    print("Podaj indeks DO (Enter = do końca):")
    do = input()

    if od == "":
        od = 0
    else:
        od = int(od)

    if do == "":
        do = len(manager.historia)
    else:
        do = int(do)

    if od < 0 or do < 0 or od > len(manager.historia) or do > len(manager.historia) or od > do:
        print(f"Podano zakres poza historią. Liczba zapisanych operacji: {len(manager.historia)}")
    else:
        for operacja in manager.historia[od:do]:
            print(operacja)

    print("\n")

while True:
    print("*******************************************************")
    print("To jest prosty program magazynowy")
    print("*******************************************************")
    print("Wybierz jedną z komend poniżej aby uruchomić lub zakończyć program - podaj jej numer")
    print("1 - SALDO")
    print("2 - SPRZEDAŻ")
    print("3 - ZAKUP")
    print("4 - KONTO")
    print("5 - LISTA")
    print("6 - MAGAZYN")
    print("7 - PRZEGLĄD")
    print("8 - KONIEC")

    nr_komendy = int(input())

    if nr_komendy == 8:
        zapisz_dane(
            manager.stan_konta,
            manager.magazyn,
            manager.historia
        )
        print("Dane zostały zapisane")
        print("Zakończyłeś program - Do widzenia")
        break

    manager.execute(nr_komendy)