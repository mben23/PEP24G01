import re

class EnumeratorCuvant():
    def __init__(self, cuvant: str):
        self.cuvant = cuvant
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.cuvant):
            valoare = (self.i, self.cuvant[self.i])
            self.i += 1
            return valoare
        else:
            raise StopIteration

def verifica_cuvant(cuvant):
    # Verifica daca cuvantul contine doar litere
    return bool(re.match("^[a-zA-Z]+$", cuvant))

cuvant = input("Introduceți un cuvânt: ")

if verifica_cuvant(cuvant):
    with open("cuvinte.txt", "w") as f:
        for i, litera in EnumeratorCuvant(cuvant):
            f.write(f"{i}: {litera}\n")
    print("Rezultatul a fost scris în fișierul cuvinte.txt.")
else:
    print("Cuvântul introdus nu este valid. Asigurați-vă că conține doar litere.")
