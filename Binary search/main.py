import random as rd
import math as mt

def binary_search(vetor, elemento):
    #Ordenar os vetores do menor ao maior:
    lista = sorted(vetor)
    #print(lista)
    #Definir qual a posição do primeiro item do vetor e do último (menos 1 para evitar out of range)
    primeiro_item = 0
    ultimo_item = len(lista) - 1 
    #Criação do loop:
    while (primeiro_item <= ultimo_item):
        meio = mt.floor(((primeiro_item + ultimo_item) / 2))
        if (lista[meio] == elemento):
            return True
        #Se o elemento do meio for maior que o elemento buscado, o meio deve se deslocar para esquerda, então o último item assume a posição do meio e a divisão seguirá para o meio até o fim do loop:
        elif (lista[meio] > elemento):
            ultimo_item = (meio - 1)
        #Caso contrário, a divisão seguirá para direita com o primeiro item assumindo a posição do meio e a divisão segue para direita até o fim do loop:
        else:
            primeiro_item = (meio + 1)
    #Caso o "primeiro item" se iguale ao "ultimo item", o loop é quebrado e retorna-se:
    return False
#Criação do vetor com números aleatórios:
vetor = []
for i in range (0,100):
    vetor.append(rd.randint(0,1000))
#print(vetor) 
    
elemento = int(input("Digite um elemento a ser procurado na lista: ")) 

if (binary_search(vetor, elemento)):  
    print("Achei!") 
else:
    print("Não encontrado!") 
    
