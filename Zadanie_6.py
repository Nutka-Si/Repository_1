uczniowie = []
nauczyciele = []
wychowawcy = []

def utworz_uzytkownika():
    while True:
        print("Możesz utworzyć nowego użytkownika")
        print("Wybierz jedną z opcji:")
        print("u - uczeń")
        print("n - nauczyciel")
        print("w - wychowawca")
        print("k - koniec")

        uzytkownik = input()

        if uzytkownik == "u":
            print("Podaj imię i nazwisko ucznia:")
            imie_i_nazwisko = input()

            print("Podaj klasę:")
            klasa = input()

            uczen = {
                "imie_i_nazwisko": imie_i_nazwisko,
                "klasa": klasa
            }

            uczniowie.append(uczen)

        elif uzytkownik == "w":
            print("Podaj imię i nazwisko wychowawcy:")
            imie_i_nazwisko = input()

            print("Podaj klasę:")
            klasa = input()

            wychowawca = {
                "imie_i_nazwisko": imie_i_nazwisko,
                "klasa": klasa
            }

            wychowawcy.append(wychowawca)

        elif uzytkownik == "n":
            print("Podaj imię i nazwisko nauczyciela:")
            imie_i_nazwisko = input()

            print("Podaj nazwę przedmiotu:")
            przedmiot = input()

            klasy = []

            print("Podawaj klasy nauczyciela.")
            print("Pusta linia kończy dodawanie klas.")

            while True:
                klasa = input()

                if klasa == "":
                    break

                klasy.append(klasa)

            nauczyciel = {
                "imie_i_nazwisko": imie_i_nazwisko,
                "przedmiot": przedmiot,
                "klasy": klasy
            }

            nauczyciele.append(nauczyciel)

        elif uzytkownik == "k":
            break

        else:
            print("Nie ma takiego użytkownika.")

def zarzadzaj_uzytkownikami():
    while True:
        print("Zarządzanie użytkownikami")
        print("Wybierz jedną z opcji:")
        print("k - klasa")
        print("u - uczeń")
        print("n - nauczyciel")
        print("w - wychowawca")
        print("x - koniec")

        wybor = input()

        if wybor == "k":
            print("Podaj klasę:")
            klasa = input()

            print("Uczniowie klasy", klasa)

            for uczen in uczniowie:
                if uczen["klasa"] == klasa:
                    print(uczen["imie_i_nazwisko"])

            print("Wychowawca klasy", klasa)

            for wychowawca in wychowawcy:
                if wychowawca["klasa"] == klasa:
                    print(wychowawca["imie_i_nazwisko"])

        elif wybor == "u":
            print("Podaj imię i nazwisko ucznia:")
            imie_i_nazwisko = input()

            for uczen in uczniowie:
                if uczen["imie_i_nazwisko"] == imie_i_nazwisko:
                    klasa = uczen["klasa"]

                    for nauczyciel in nauczyciele:
                        if klasa in nauczyciel["klasy"]:
                            print(
                                nauczyciel["przedmiot"],
                                "-",
                                nauczyciel["imie_i_nazwisko"]
                            )

        elif wybor == "n":
            print("Podaj imię i nazwisko nauczyciela:")
            imie_i_nazwisko = input()

            for nauczyciel in nauczyciele:
                if nauczyciel["imie_i_nazwisko"] == imie_i_nazwisko:
                    print("Prowadzone klasy:")

                    for klasa in nauczyciel["klasy"]:
                        print(klasa)

        elif wybor == "w":
            print("Podaj imię i nazwisko wychowawcy:")
            imie_i_nazwisko = input()

            for wychowawca in wychowawcy:
                if wychowawca["imie_i_nazwisko"] == imie_i_nazwisko:
                    klasa = wychowawca["klasa"]

                    print("Uczniowie klasy", klasa)

                    for uczen in uczniowie:
                        if uczen["klasa"] == klasa:
                            print(uczen["imie_i_nazwisko"])

        elif wybor == "x":
            break

        else:
            print("Nie ma takiej opcji.")

while True:
    print("*******************************************************")
    print("Witam w programie obsługi szkolnej")
    print("*******************************************************")
    print("Wybierz jedną z komend:")
    print("1 - UTWÓRZ")
    print("2 - ZARZĄDZAJ")
    print("3 - ZAKOŃCZ")

    nr_komendy = int(input())

    if nr_komendy == 1:
        utworz_uzytkownika()

    elif nr_komendy == 2:
        zarzadzaj_uzytkownikami()

    elif nr_komendy == 3:
        print("Zakończyłeś program - Do widzenia")
        break
