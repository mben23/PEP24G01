# word = input("Enter a word: ")
# count = 0
#
# for letter in word:
#     if word[0] == letter:
#         count += 1
#
# print(f"'{word[0]}' appears {count} times.")



lista = input("Introduceti lista de taskuri: ")
lista_taskuri = lista.split(",")
print(lista_taskuri)

no_duplicates = []

for task in lista_taskuri:
    if task not in no_duplicates:
        no_duplicates.append(task)

print(no_duplicates)