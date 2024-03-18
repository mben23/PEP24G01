class Angajat:
    angajati = []

    def __init__(self, nume, salariu, departament):
        self.nume = nume
        self.salariu = salariu
        self.departament = departament
        Angajat.angajati.append(self)

    @classmethod
    def adauga_angajati(cls, *angajati):
        cls.angajati.extend(angajati)

    @classmethod
    def afisare_angajati(cls):
        for angajat in cls.angajati:
            print(f"Nume: {angajat.nume}, Salariu: {angajat.salariu}, Departament: {angajat.departament}")

    @classmethod
    def extrage_angajati_departament(cls, departament):
        for angajat in cls.angajati:
            if angajat.departament == departament:
                yield angajat

    @classmethod
    def majorare_salariu_departament(cls, departament, procent_maj):
        for angajat in cls.extrage_angajati_departament(departament):
            angajat.salariu *= (1 + procent_maj / 100)

# Adaugăm câțiva angajați
Angajat.adauga_angajati(
    Angajat("John", 3000, "IT"),
    Angajat("Alice", 3500, "HR"),
    Angajat("Bob", 4000, "IT"),
    Angajat("Carol", 3200, "Finance"),
    Angajat("David", 3800, "IT")
)

# Afisam detaliile angajatilor
Angajat.afisare_angajati()

# Cerem input de la utilizator pentru departament și procent de majorare
departament = input("Introduceti departamentul: ")
procent_maj = float(input("Introduceti procentul de majorare a salariilor: "))

# Majoram salariile angajatilor din departamentul respectiv
Angajat.majorare_salariu_departament(departament, procent_maj)

# Afisam salariile marite
print("Salariile marite sunt:")
Angajat.afisare_angajati()
