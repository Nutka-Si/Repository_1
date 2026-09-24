print("*******************************************************")
print("To jest program do łączenia elementów i pakowania do wspólnej paczki")
print("Paczka nie może przekroczyć 20 kg")
print("Pojedynczy element nie może przekroczyć 10 kg")
print("Dla każdego elementu trzeba podać wagę w kg")
print("*******************************************************\n")
print("Podaj ile elementów chcesz wysłać:")
ilosc_elementow = int(input())
i=1
suma_wag = 0
ilosc_paczek = 0
suma_niewykorzystanych_wag = 0
suma_wszystkich_wag = 0
najwiecej_pustych_kg = -1
numer_najbardziej_pustej_paczki = 0

while i <= ilosc_elementow:

    print(f"Podaj wagę dla elementu nr {i}")
    waga_elementu = int(input())

    if waga_elementu < 1 or waga_elementu > 10:
        if suma_wag > 0:
            ilosc_paczek += 1
            niewykorzystana_waga = 20 - suma_wag
            suma_niewykorzystanych_wag += niewykorzystana_waga

            if niewykorzystana_waga > najwiecej_pustych_kg:
                najwiecej_pustych_kg = niewykorzystana_waga
                numer_najbardziej_pustej_paczki = ilosc_paczek

        break

    suma_wag += waga_elementu
    suma_wszystkich_wag += waga_elementu

    if suma_wag < 20:
        if i == ilosc_elementow:
            ilosc_paczek += 1
            niewykorzystana_waga = 20 - suma_wag
            suma_niewykorzystanych_wag += niewykorzystana_waga

            if niewykorzystana_waga > najwiecej_pustych_kg:
                najwiecej_pustych_kg = niewykorzystana_waga
                numer_najbardziej_pustej_paczki = ilosc_paczek

    elif suma_wag == 20:
        ilosc_paczek += 1
        niewykorzystana_waga = 0

        if niewykorzystana_waga > najwiecej_pustych_kg:
            najwiecej_pustych_kg = niewykorzystana_waga
            numer_najbardziej_pustej_paczki = ilosc_paczek

        suma_wag = 0

    else:
        ilosc_paczek += 1
        waga_paczki = suma_wag - waga_elementu
        niewykorzystana_waga = 20 - waga_paczki
        suma_niewykorzystanych_wag += niewykorzystana_waga
        if niewykorzystana_waga > najwiecej_pustych_kg:
            najwiecej_pustych_kg = niewykorzystana_waga
            numer_najbardziej_pustej_paczki = ilosc_paczek
        suma_wag = waga_elementu

        if i == ilosc_elementow:
            ilosc_paczek += 1
            niewykorzystana_waga = 20 - suma_wag
            suma_niewykorzystanych_wag += niewykorzystana_waga

            if niewykorzystana_waga > najwiecej_pustych_kg:
                najwiecej_pustych_kg = niewykorzystana_waga
                numer_najbardziej_pustej_paczki = ilosc_paczek

    i += 1

print(f"Najwięcej pustych kilogramów ma paczka nr {numer_najbardziej_pustej_paczki}: {najwiecej_pustych_kg} kg")
print(f"Ilość wysłanych paczek to: {ilosc_paczek}")
print(f"Ilość wysłanych kilogramów to: {suma_wszystkich_wag} kg")
print(f"Suma niewykorzystanych kilogramów to {suma_niewykorzystanych_wag} kg")