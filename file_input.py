"""Citirea unui șir de numere dintr-un fișier text."""

from console_input import converteste_numar


def citeste_sir_din_fisier(nume_fisier):
    """
    Citește toate numerele din fișier (separate prin spații sau linii noi).
    Returnează (sir, valori_ignorate). Ridică FileNotFoundError dacă fișierul lipsește.
    """
    sir, ignorate = [], []
    with open(nume_fisier, "r", encoding="utf-8") as f:
        for token in f.read().split():
            try:
                sir.append(converteste_numar(token))
            except ValueError:
                ignorate.append(token)
    return sir, ignorate


def citeste_sir_fisier_interactiv():
    """Cere numele fișierului de la tastatură și tratează erorile de citire."""
    nume = input("Introduceți numele fișierului text (ex: numere.txt): ").strip()
    if not nume:
        print("  Nu ați introdus niciun nume de fișier.")
        return None
    try:
        sir, ignorate = citeste_sir_din_fisier(nume)
    except FileNotFoundError:
        print(f"  Eroare: fișierul '{nume}' nu există.")
        return None
    except IsADirectoryError:
        print(f"  Eroare: '{nume}' este un director, nu un fișier.")
        return None
    except PermissionError:
        print(f"  Eroare: nu aveți permisiunea să citiți fișierul '{nume}'.")
        return None
    if ignorate:
        print(f"  Atenție: au fost ignorate valorile nenumerice: {', '.join(ignorate)}")
    if not sir:
        print("  Fișierul nu conține niciun număr.")
        return None
    return sir
