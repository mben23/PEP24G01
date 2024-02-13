# name = input("Cum te cheama? - ")
# print("Buna " + name)

# birth_year = input("Data nasterii:  ")
# age = 2024 - int(birth_year)
# print(age)
# print("Multi inainte!" + name)

# First = input("First: ")
# Second = input('Second: ')
# sum =float(First) + float(Second)
# print('sum: ' + str(sum))

# CUM sa indentificam un numar mai mare
#  METODA 1
# numar1 = int(input("Adaugati priml numar: "))
# numar2 = int(input("Adaugati cel de-al doilea numar: "))
#
# if numar1 > numar2:
#     numarul_mare = numar1
# else:
#     numarul_mare = numar2
#
# print('Numarul mare este: ', numarul_mare)

# METODA 2

# numar1 = int(input("Adaugati priml numar: "))
# numar2 = int(input("Adaugati cel de-al doilea numar: "))
#
# if numar1 > numar2: numarul_mai_mare = numar1
# else: numarul_mai_mare = numar2
#
# print('Numarul mai mare este:', numarul_mai_mare)


# METODA 3
# numar1 = int(input("Adaugati priml numar: "))
# numar2 = int(input("Adaugati cel de-al doilea numar: "))
# numar3 = int(input("Adaugati numarul 3: "))
#
# numarul_mare = numar1
#
# if numar2 > numarul_mare:
#     numarul_mare = numar2
#
# if numar3 > numarul_mare:
#     numarul_mare = numar3
#
# print("Numarul mai mare este:", numarul_mare)


# largest_number = 12
# number = int(input('numar'))
# if number == 1:
#     print(largest_number)
#     exit()
# if number > largest_number:
#     largest_number = number
# # Go to line 02


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

# odd_numbers = 0
# even_numbers = 0
#
# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))
#
# # 0 terminates execution.
# while number != 0:
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#     else:
#         # Increase the even_numbers counter.
#         even_numbers += 1
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))
#
# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)

# for i in range (2, 8):
#     print('Valoare lui i este acum:', i)

# for i in range(2, 1):
#     print("The value of i is currently", i)

# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2

# nume = input('Cum te numesti?')
# print('Buna , ' + nume)
# culoare_preferata = input('Care este culoarea ta preferata? ')
# print(nume + ' ii place ' + culoare_preferata)

# greutate_in_kg = input('Care este greutatea in (kg):  ')
# greutete_in_lbs = int(greutate_in_kg) / 0.45
# print(greutete_in_lbs)

# first = 'beni'
# last = 'marisescu'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(msg)

curs = ('Python pentru Incepatori')
print('python' in curs)