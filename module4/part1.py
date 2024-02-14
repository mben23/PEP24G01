# def factorial (x):
#     result = 1
#     for i in range(1, x+1):
#         result *= i
#     return result
#
# result = factorial(4)
# print(result)

# result = 1
# def factorial (x):
#     global result
#     for i in range(1, x+1):
#         result *= i
# gauss(100)
# factorial(4)
# print(result)


def sumafractii(x):
    suma = 0
    for i in range(1, x+1):
        suma += 1/i
    return suma

x = int(input())
print(sumafractii(x))
