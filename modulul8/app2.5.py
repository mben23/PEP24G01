import os

# Extrage numele sistemului de operare al utilizatorului
sistem_operare_utilizator = os.name

# Deschide fișierul "user.txt" și extrage utilizatorii compatibili
with open("user.txt", "r") as f:
    for linie in f:
        nume, sistem_operare, telefon = linie.strip().split(";")
        if sistem_operare == sistem_operare_utilizator:
            print("---------------------------")
            print("User compatibil!")
            print("Nume:", nume)
            print("tel:", telefon)
