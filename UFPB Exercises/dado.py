import random as rd
#Criação da quantidade de vezes que o dado será jogado e armazenamento do resultado em lista
vezes = int(input("Digite a quantidade de vezes: "))
numeros = [rd.randint(1,6) for n in range(vezes)]
#print(numeros)
#Criaçaõ de 6 listas para armazenar o resultado
lista = [[] for n in range(6)]
#Loop para buscar os 6 números na lista de números e armazená-los em uma lista correspondente
for n in numeros:
    if(n == 1):
        lista[0].append(n)
    elif(n == 2):
        lista[1].append(n)
    elif(n == 3):
        lista[2].append(n)
    elif(n == 4):
        lista[3].append(n)
    elif(n == 5):
        lista[4].append(n)
    elif(n == 6):
        lista[5].append(n)
#print(lista)
#Com os números armazenados, basta pegar o length de cada lista e fazer operações para descobrir a porcentagem de aparecimento de cada número
for a in range(6):
    print(f"A porcentagem do número {a + 1} aparecer foi: {(len(lista[a]) / vezes) * 100:.2f}%")