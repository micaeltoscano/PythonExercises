import math as mt

def esquerda(lista):
    meio = mt.floor(len(lista) / 2)
    maior_esquerda = 0
    while meio > -1:
        n = lista[meio]
      
        if n > maior_esquerda:
            maior_esquerda = n
        meio -= 1
    return maior_esquerda

def direita(lista):
    lista_direita = []
    meio = (mt.floor(len(lista) / 2)) + 1
    maior_direita = 0
    while (meio < len(lista) - 1):
        m = lista[meio]
        lista_direita.append(m)
        if m > maior_direita:
            maior_direita = m
        meio += 1
    return maior_direita

def lista_esquerda(lista):
    meio = int((len(lista) / 2))
    lista_esquerda = []
    while meio > -1:
        n = lista[meio]
        lista_esquerda.append(n)
        meio -= 1
    print((lista_esquerda))

def lista_direita(lista):
    meio = (mt.floor(len(lista) / 2)) + 1
    lista_direita = []
    while meio < (len(lista)):
        m = lista[meio]
        lista_direita.append(m)
        meio += 1
    print((lista_direita))


