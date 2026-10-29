"""Laborator 2 – meniul principal al aplicației."""

from console_input import afiseaza_matrice, afiseaza_sir, citeste_matrice, citeste_sir


def meniu():
    print("\n===== Laborator 2 =====")
    print("1. Citește un șir de numere de la tastatură")
    print("2. Citește o matrice de numere de la tastatură")
    print("0. Ieșire")
    return input("Alegeți o opțiune: ").strip()


def main():
    while True:
        optiune = meniu()
        if optiune == "1":
            afiseaza_sir(citeste_sir())
        elif optiune == "2":
            afiseaza_matrice(citeste_matrice())
        elif optiune == "0":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă.")


if __name__ == "__main__":
    main()
