"""Citirea de la tastatură a unui șir și a unei matrice de numere."""


def converteste_numar(text):
    """Transformă un text în int sau float. Ridică ValueError dacă nu e număr."""
    text = text.strip().replace(",", ".")
    try:
        return int(text)
    except ValueError:
        return float(text)


def citeste_intreg_pozitiv(mesaj):
    """Citește un număr întreg strict pozitiv, repetând până la o valoare validă."""
    while True:
        valoare = input(mesaj).strip()
        try:
            n = int(valoare)
            if n > 0:
                return n
            print("  Valoarea trebuie să fie un număr întreg mai mare decât 0.")
        except ValueError:
            print("  Valoare invalidă. Introduceți un număr întreg.")


def citeste_sir():
    """Citește un șir de numere introduse pe o singură linie, separate prin spațiu."""
    while True:
        linie = input("Introduceți numerele șirului, separate prin spațiu: ").split()
        if not linie:
            print("  Șirul nu poate fi gol.")
            continue
        try:
            return [converteste_numar(x) for x in linie]
        except ValueError:
            print("  Toate valorile trebuie să fie numere. Încercați din nou.")


def citeste_matrice():
    """Citește o matrice cu dimensiunile alese de utilizator, linie cu linie."""
    linii = citeste_intreg_pozitiv("Numărul de linii: ")
    coloane = citeste_intreg_pozitiv("Numărul de coloane: ")
    matrice = []
    for i in range(linii):
        while True:
            valori = input(f"Linia {i + 1} ({coloane} numere separate prin spațiu): ").split()
            if len(valori) != coloane:
                print(f"  Trebuie introduse exact {coloane} numere.")
                continue
            try:
                matrice.append([converteste_numar(x) for x in valori])
                break
            except ValueError:
                print("  Toate valorile trebuie să fie numere.")
    return matrice


def afiseaza_sir(sir, titlu="Șirul introdus"):
    """Afișează șirul și numărul de elemente."""
    print(f"\n{titlu} ({len(sir)} elemente):")
    print("  [ " + ", ".join(str(x) for x in sir) + " ]")


def afiseaza_matrice(matrice, titlu="Matricea introdusă"):
    """Afișează matricea cu coloanele aliniate."""
    linii, coloane = len(matrice), len(matrice[0])
    latime = max(len(str(x)) for rand in matrice for x in rand)
    print(f"\n{titlu} ({linii} x {coloane}):")
    for rand in matrice:
        print("  | " + "  ".join(str(x).rjust(latime) for x in rand) + " |")
