from flask import Flask, render_template, request
from obsluga_plikow import odczytaj_dane, zapisz_dane

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def strona_glowna():
    stan_konta, magazyn, historia = odczytaj_dane()

    if request.method == 'POST':
        akcja = request.form['akcja']

        if akcja == 'zakup':
            nazwa = request.form['nazwa'].lower()
            cena = float(request.form['cena'])
            ilosc = int(request.form['ilosc'])

            wartosc_zakupu = cena * ilosc

            if stan_konta >= wartosc_zakupu:
                stan_konta -= wartosc_zakupu

                znaleziono = False

                for produkt in magazyn:
                    if produkt["nazwa_produktu"] == nazwa and produkt["cena w zł"] == cena:
                        produkt["ilość"] += ilosc
                        znaleziono = True

                if znaleziono == False:
                    nowy_produkt = {
                        "nazwa_produktu": nazwa,
                        "cena w zł": cena,
                        "ilość": ilosc
                    }
                    magazyn.append(nowy_produkt)

                historia.append(
                    f"ZAKUP: {nazwa}, {ilosc} szt., {wartosc_zakupu} zł"
                )

                zapisz_dane(stan_konta, magazyn, historia)

        if akcja == 'sprzedaz':
            nazwa = request.form['nazwa'].lower()
            ilosc = int(request.form['ilosc'])

            for produkt in magazyn:
                if produkt["nazwa_produktu"] == nazwa:
                    if produkt["ilość"] >= ilosc:
                        produkt["ilość"] -= ilosc

                        wartosc_sprzedazy = produkt["cena w zł"] * ilosc
                        stan_konta += wartosc_sprzedazy

                        historia.append(
                            f"SPRZEDAŻ: {nazwa}, {ilosc} szt., {wartosc_sprzedazy} zł"
                        )

                        zapisz_dane(stan_konta, magazyn, historia)

        if akcja == 'saldo':
            wartosc = float(request.form['wartosc'])

            stan_konta += wartosc

            historia.append(
                f"SALDO: {wartosc} zł"
            )

            zapisz_dane(stan_konta, magazyn, historia)

    return render_template(
        "main.html",
        stan_konta=stan_konta,
        produkty=magazyn
    )

@app.route('/historia/')
def historia():
    stan_konta, magazyn, historia = odczytaj_dane()

    return render_template(
        "historia.html",
        historia=historia
    )


@app.route('/historia/<start>/<koniec>/')
def historia_zakres(start, koniec):
    stan_konta, magazyn, historia = odczytaj_dane()

    start = int(start)
    koniec = int(koniec)

    if start < 0 or koniec > len(historia) or start > koniec:
        komunikat = f"Nieprawidłowy zakres. Możliwy zakres: 0 - {len(historia)}"

        return render_template(
            "historia.html",
            historia=[],
            komunikat=komunikat
        )

    return render_template(
        "historia.html",
        historia=historia[start:koniec]
    )