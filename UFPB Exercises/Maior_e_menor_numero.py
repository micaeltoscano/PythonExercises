#Faça um programa que leia números repetidamente até que o valor -1 seja digitado. Quando isso ocorrer, o programa deve exibir o menor valor, o maior valor e a soma dos valores. 

num = 0
maior = 0
menor = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
soma = 0

while True: 
    num = int(input("Digite um número: "))
    if num == -1:
        break
    else:
        if (num > maior):
            maior = num
        if (menor > num):
            menor = num
        soma = soma + num
        
print(maior, menor, soma)


