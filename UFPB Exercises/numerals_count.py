#Escreva um programa para determinar o número de algarismos de um número inteiro positivo dado.

num= int(input("Digite um número: "))
alg = 1

while (num >= 10):
    num /= 10
    alg += 1

print(alg)
