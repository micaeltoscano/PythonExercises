import random as rd
import math as mt
#Criação do vetor com números aleatórios:
vetor = []
for i in range (0,100):
    vetor.append(rd.randint(0,1000))
#print(vetor) #- caso queira ver os números presentes no vetor
elemento = int(input("Digite um elemento a ser procurado na lista: "))

def binary_search(vetor, elemento):
    #Ordenar os vetores do menor ao maior:
    lista = sorted(vetor)
    #Definir qual a posição do primeiro item do vetor e do último (menos 1 para evitar out of range)
    primeiro_item = 0
    ultimo_item = len(lista) - 1 
    #Criação do loop:
    while (primeiro_item <= ultimo_item):
        meio = mt.floor(((primeiro_item + ultimo_item) / 2))
        if (lista[meio] == elemento):
            return True
        #Se o item do meio for maior que o número buscado, reduz-se 1 do "último item" para que a busca siga pela esquerda, ou seja, diminui-se a razão:
        elif (lista[meio] > elemento):
            ultimo_item -= 1
        #Caso contrário, soma-se 1 para que a busca siga pela direita:
        else:
            primeiro_item += 1
    #Caso o "primeiro item" se iguale ao "ultimo item", o loop é quebrado e retorna-se:
    return False
               
if (binary_search(vetor, elemento)):  
    print("Achei!") 
else:
    print("Não encontrado!") 
    