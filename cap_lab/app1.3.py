
salarii_input = input("Introduceti salariile separate cu virgula: ")
salarii = [int(s) for s in salarii_input.split(",")]

# Citirea procentului de majorare de la utilizator
procent_maj = float(input("Introduceti procentul de marire: "))

# Calcularea salariilor marite folosind map si o functie lambda
salarii_marite = list(map(lambda x: x * (1 + procent_maj / 100), salarii))

# Afisarea salariilor marite
print("Salariile marite sunt:")
for salariu in salarii_marite:
    print(salariu)
