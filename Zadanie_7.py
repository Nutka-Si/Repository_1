from obsluga_plikow import zapisz_dane, odczytaj_dane


stan_konta, Magazyn, historia = odczytaj_dane()

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

    if nr_komendy == 1:
        print("Podaj kwotę do dodania lub odjęcia:")
        kwota = float(input())


        stan_konta += kwota
        historia.append(f"SALDO: {kwota} zł")

        print(f"Stan konta wynosi: {stan_konta} zł")
        print("\n")

    elif nr_komendy == 2:
        print("SPRZEDAŻ")
        print("Podaj nazwę produktu:")
        nazwa = input()

        print("Podaj cenę produktu:")
        cena = float(input())

        print("Podaj liczbę sztuk:")
        ilosc = int(input())

        if cena <= 0 or ilosc <= 0:
            print("Cena i liczba sztuk muszą być większe od zera")
            continue

        znaleziono = False

        for produkt in Magazyn:
            if produkt["nazwa_produktu"] == nazwa and produkt["cena w zł"] == cena:
                znaleziono = True

                if produkt["ilość"] >= ilosc:
                    print("Znaleziono produkt")
                    print("Można wykonać sprzedaż")

                    produkt["ilość"] -= ilosc

                    wartosc_sprzedazy = cena * ilosc
                    stan_konta += wartosc_sprzedazy
                    historia.append(f"SPRZEDAŻ: {nazwa}, {ilosc} szt., {wartosc_sprzedazy} zł")

                else:
                    print("Brak wystarczającej liczby sztuk w magazynie")

        if znaleziono == False:
            print("Nie znaleziono takiego produktu")




    elif nr_komendy == 3:
        print("ZAKUP")

        print("Podaj nazwę produktu:")
        nazwa = input()

        print("Podaj cenę produktu:")
        cena = float(input())

        print("Podaj liczbę sztuk:")
        ilosc = int(input())

        if cena <= 0 or ilosc <= 0:
            print("Cena i liczba sztuk muszą być większe od zera")
            continue

        wartosc_zakupu = cena * ilosc

        if stan_konta >= wartosc_zakupu:
            stan_konta -= wartosc_zakupu

            znaleziono = False

            for produkt in Magazyn:
                if produkt["nazwa_produktu"] == nazwa and produkt["cena w zł"] == cena:
                    produkt["ilość"] += ilosc
                    znaleziono = True

            if znaleziono == False:
                nowy_produkt = {
                    "nazwa_produktu": nazwa,
                    "cena w zł": cena,
                    "ilość": ilosc
                }
                Magazyn.append(nowy_produkt)

            print("Zakup został wykonany")
            historia.append(f"ZAKUP: {nazwa}, {ilosc} szt., {wartosc_zakupu} zł")
            print(f"Stan konta wynosi: {stan_konta} zł")

        else:
            print("Brak wystarczających środków na koncie")

    elif nr_komendy == 4:
        print("KONTO")
        print(f"Stan konta wynosi: {stan_konta} zł")
        print("\n")

    elif nr_komendy == 5:
        print("LISTA PRODUKTÓW")

        for produkt in Magazyn:
            print(f"Nazwa: {produkt['nazwa_produktu']}, "
                  f"cena: {produkt['cena w zł']} zł, "
                  f"ilość: {produkt['ilość']} szt.")

        print("\n")

    elif nr_komendy == 6:
        print("MAGAZYN")
        print("Podaj nazwę produktu:")
        nazwa = input()

        znaleziono = False

        for produkt in Magazyn:
            if produkt["nazwa_produktu"] == nazwa:
                print(f"Produkt: {produkt['nazwa_produktu']}, "
                      f"ilość: {produkt['ilość']} szt.")
                znaleziono = True

        if znaleziono == False:
            print("Nie znaleziono takiego produktu")

        print("\n")

    elif nr_komendy == 7:
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
            do = len(historia)
        else:
            do = int(do)

        if od < 0 or do < 0 or od > len(historia) or do > len(historia) or od > do:
            print(f"Podano zakres poza historią. Liczba zapisanych operacji: {len(historia)}")
        else:
            for operacja in historia[od:do]:
                print(operacja)

        print("\n")

    elif nr_komendy == 8:
        zapisz_dane(stan_konta, Magazyn, historia)
        print("Dane zostały zapisane")
        print("Zakończyłeś program - Do widzenia ")
        break