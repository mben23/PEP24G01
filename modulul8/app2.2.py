dict1 = {}

# Deschide fișierul pentru citire
with open("cuvinte.txt", "r") as f:
    # Citește fiecare linie din fișier
    for linie in f:
        # Eliminăm eventualele spații albe și caractere de newline de la finalul liniei
        linie = linie.strip()
        # Separăm indexul și litera utilizând ":" ca separator
        index, litera = linie.split(": ")
        # Adăugăm perechea cheie-valoare în dicționar
        dict1[index] = litera

# Afisăm dicționarul
print(dict1)
