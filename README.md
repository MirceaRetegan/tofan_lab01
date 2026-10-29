# Laborator 2 – Citirea datelor în Python

Aplicație Python pentru citirea și afișarea datelor introduse de utilizator.

## Cerințe
- Python 3.8 sau mai nou (fără biblioteci externe)

## Rulare
```bash
python main.py
```

## Funcționalități
1. **Citirea unui șir de la tastatură** – numerele se introduc pe o linie, separate prin spațiu.
2. **Citirea unei matrice** – utilizatorul alege numărul de linii și de coloane, apoi introduce fiecare linie.
   Șirul și matricea sunt afișate formatat (matricea cu coloane aliniate).
3. **Citirea unui șir din fișier** – se introduce numele unui fișier text; numerele pot fi separate prin spații sau pe linii diferite.
   Dacă fișierul nu există, se afișează un mesaj de eroare. Exemplu inclus: `numere.txt`.

## Structura proiectului
| Fișier | Rol |
|---|---|
| `main.py` | meniul principal |
| `console_input.py` | citire/afișare șir și matrice de la tastatură |
| `file_input.py` | citirea șirului din fișier |
| `numere.txt` | fișier de test |

## Branch-uri
- `feature/console-input` – Cerința 1
- `feature/array-file-input` – Cerința 2

Ambele au fost integrate în `main`.
