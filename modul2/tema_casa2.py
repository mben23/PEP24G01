nr = input("Cate carti doriti sa adaugati la lista?:  ")
lista_carti = []

for i in range(int(nr)):
    print(f"======== Cartea {i + 1} ========")
    carte = {}
    carte["nume"] = input("Numele cartii : ")
    carte["autor"] = input("Numele autorului : ")
    carte["an"] = input("Anul publicarii : ")
    lista_carti.append(carte)

print("Cartile dumneavoastra sunt:")
for i, carte in enumerate(lista_carti, 1):
    print(f"{i}. {carte}")
