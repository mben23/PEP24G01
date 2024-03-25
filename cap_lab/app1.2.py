class Masina:
    def __init__(self, marca: str, usi: int, culoare: str, an: int, pret: float):
        self.marca = marca
        self.usi = usi
        self.culoare = culoare
        self.an = an
        self.__pret = pret

    def getPret(self):
        return self.__pret

masina1 = Masina("Audi", 4, "gri", 2006, 3400)
masina2 = Masina("BMW", 2, "maro", 2007, 4788.60)
masina3 = Masina("Volvo", 4, "gri", 2017, 27000)
masina4 = Masina("Audi", 4, "negru", 2013, 10200)
masina5 = Masina("Audi", 2, "gri", 2005, 3400)
masina6 = Masina("BMW", 4, "negru", 2017, 22000)
masina7 = Masina("Volvo", 4, "gri", 2017, 27000)

masini = [masina7, masina6, masina5, masina4, masina3, masina1, masina2]

# a. Calculați și afișați prețul mediu al mașinilor din lista masini.
pret_mediu = sum(masina.getPret() for masina in masini) / len(masini)
print(f"Pretul mediu al masinilor este: {pret_mediu}")

# b. Afișați numărul de mașini marca BMW din lista cu ajutorul funcției filter
numar_masini_bmw = len(list(filter(lambda masina: masina.marca == 'BMW', masini)))
print(f"Numarul de masini marca BMW este: {numar_masini_bmw}")

# c. Creați un generator care sa extraga masinile marca Audi din lista de masini și calculati anul mediu de fabricație a acestora.
an_mediu_audi = sum(masina.an for masina in masini if masina.marca == 'Audi') / len([masina for masina in masini if masina.marca == 'Audi'])
print(f"Anul mediu de fabricatie al masinilor marca Audi este: {an_mediu_audi}")

# d. Cereți input de la utilizator cu o marca de masina și afisati cate masini dorite de acesta avem in stoc.
marca_cautata = input("Introduceti marca masinii dorite: ")
numar_masini = len([masina for masina in masini if masina.marca.lower() == marca_cautata.lower()])
print(f"Avem {numar_masini} masini marca {marca_cautata} in stoc.")
