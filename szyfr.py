# Szyfr permutacyjny - szyfrowanie i deszyfrowanie
# Nr indeksu: 166481, 166481 mod 3 = 2 -> wariant c) szyfr permutacyjny

# Klucz (permutacja) wpisany na stałe, długość 6.
# Liczby to pozycje liter w bloku (liczone od 0).
# Np. pierwsza litera szyfrogramu to litera z pozycji 2 w bloku.
klucz = [2, 5, 0, 4, 1, 3]

dlugosc_bloku = len(klucz)


def sprawdz_tekst(tekst):
    # Zwraca opis błędu albo None, jeśli tekst jest poprawny
    if tekst == "":
        return "Tekst nie może być pusty."
    for litera in tekst:
        if not (litera.isalpha() or litera == " "):
            return "Niedozwolony znak: '" + litera + "'. Dozwolone są tylko litery i spacje."
    return None


def sprawdz_szyfrogram(szyfrogram):
    # Zwraca opis błędu albo None, jeśli szyfrogram jest poprawny
    if szyfrogram == "":
        return "Szyfrogram nie może być pusty."
    if len(szyfrogram) % dlugosc_bloku != 0:
        return "Długość szyfrogramu musi być wielokrotnością " + str(dlugosc_bloku) + "."
    for litera in szyfrogram:
        if not (litera.isalpha() or litera == " " or litera == "_"):
            return "Niedozwolony znak w szyfrogramie: '" + litera + "'."
    return None


def szyfruj(tekst):
    # Dopisujemy "_" na końcu, aż długość będzie wielokrotnością 6
    while len(tekst) % dlugosc_bloku != 0:
        tekst = tekst + "_"

    wynik = ""
    # Bierzemy po 6 liter i przestawiamy je według klucza
    for start in range(0, len(tekst), dlugosc_bloku):
        blok = tekst[start:start + dlugosc_bloku]
        for pozycja in klucz:
            wynik = wynik + blok[pozycja]
    return wynik


def deszyfruj(szyfrogram):
    wynik = ""
    for start in range(0, len(szyfrogram), dlugosc_bloku):
        blok = szyfrogram[start:start + dlugosc_bloku]
        # Odwracamy przestawienie: litera z miejsca i wraca na miejsce klucz[i]
        oryginal = [""] * dlugosc_bloku
        for i in range(dlugosc_bloku):
            oryginal[klucz[i]] = blok[i]
        wynik = wynik + "".join(oryginal)
    # Usuwamy dopisane "_" z końca
    return wynik.rstrip("_")


def menu():
    while True:
        print()
        print("===== SZYFR PERMUTACYJNY =====")
        print("Klucz:", klucz)
        print("1. Szyfruj")
        print("2. Deszyfruj")
        print("0. Wyjście")
        wybor = input("Wybierz opcję: ").strip()

        if wybor == "1":
            tekst = input("Podaj tekst do zaszyfrowania: ").strip()
            blad = sprawdz_tekst(tekst)
            if blad:
                print("BŁĄD:", blad)
            else:
                # Nawiasy, żeby było widać spacje na początku i końcu
                print("Szyfrogram: [" + szyfruj(tekst) + "]")

        elif wybor == "2":
            szyfrogram = input("Podaj szyfrogram: ")
            blad = sprawdz_szyfrogram(szyfrogram)
            if blad:
                print("BŁĄD:", blad)
            else:
                print("Tekst jawny: [" + deszyfruj(szyfrogram) + "]")

        elif wybor == "0":
            print("Koniec programu.")
            break

        else:
            print("BŁĄD: Nie ma takiej opcji. Wybierz 1, 2 lub 0.")


# Uruchomienie programu
try:
    menu()
except (KeyboardInterrupt, EOFError):
    print("\nProgram przerwany.")