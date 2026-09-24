print("Podaj imię osoby, do której chcesz wysłać wiadomość urodzinową:")
imie_odbiorcy = input()

print("Podaj rok urodzenia solenizanta:")
rok_urodzenia = int(input())

print("Napisz krótką wiadomość dla solenizanta:")
wiadomosc = input()

print("Podaj swoje imię:")
imie_nadawcy = input()

wiek_solenizanta = 2026 - rok_urodzenia

print()
tresc_powitania = f"{imie_odbiorcy}, wszystkiego najlepszego z okazji {wiek_solenizanta} urodzin!"

print(tresc_powitania)
print(wiadomosc)
print(imie_nadawcy)