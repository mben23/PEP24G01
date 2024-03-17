import datetime
import csv

class Elev:
    def __init__(self, nume, data_nasterii):
        self.nume = nume
        self.data_nasterii = datetime.datetime.strptime(data_nasterii, "%Y-%m-%d").date()

# Citim fișierul și creăm obiecte Elev
elevi = []
with open("elevi.txt", "r") as f:
    for linie in f:
        nume, data_nasterii = linie.strip().split("/")
        elev = Elev(nume, data_nasterii)
        elevi.append(elev)

# Sortăm elevii după ziua de naștere
elevi.sort(key=lambda x: x.data_nasterii)

# Determinăm următoarea persoană care își sărbătorește ziua de naștere și câți ani va împlini
ziua_de_azi = datetime.date.today()
urmatoarea_persoana = None
for elev in elevi:
    if elev.data_nasterii >= ziua_de_azi:
        urmatoarea_persoana = elev
        break

# Afișăm următoarea persoană și câți ani va împlini
if urmatoarea_persoana:
    ani = ziua_de_azi.year - urmatoarea_persoana.data_nasterii.year
    print(f"Următoarea persoană care își sărbătorește ziua de naștere este {urmatoarea_persoana.nume} și va împlini {ani} ani.")
else:
    print("Nu există nicio persoană care sărbătorește ziua de naștere în viitor.")

# Creăm un fișier CSV cu persoanele născute în aceeași zi
dict_persoane_ziua_nasterii = {}
for elev in elevi:
    ziua_nasterii = elev.data_nasterii.strftime("%Y-%m-%d")
    if ziua_nasterii not in dict_persoane_ziua_nasterii:
        dict_persoane_ziua_nasterii[ziua_nasterii] = []
    dict_persoane_ziua_nasterii[ziua_nasterii].append(elev.nume)

# Scriem datele în fișierul CSV
with open("persoane_ziua_nasterii.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for ziua_nasterii, persoane in dict_persoane_ziua_nasterii.items():
        writer.writerow([ziua_nasterii] + persoane)
