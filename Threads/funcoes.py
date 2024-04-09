#Lógica: Localizar o meio, pegar os valores entre uma metade e outra para colocá-los em listas e depois usar a função max para pegar o maior valor de cada metade
#Obs: para verificar a eficácia das threads, descomente a linha 10, 19 e 28 

def segunda_metade(lista):
    lista_segunda_metade = []
    meio = int(len(lista)/4 + 1)
    while (meio < len(lista) / 2):
        lista_segunda_metade.append(lista[meio])
        meio += 1
        #print("segunda metade funcionando")
    return lista_segunda_metade 
 
def terceira_metade(lista):
    lista_terceira_metade = []
    meio = int(len(lista)/2)
    while (meio < (len(lista) / 2 + len(lista) / 4)):
        lista_terceira_metade.append(lista[meio])
        meio += 1
        #print("terceira metade funcionando")
    return lista_terceira_metade 

def quarta_metade(lista):
    lista_quarta_metade = []
    meio = int((len(lista) / 2 + len(lista) / 4))
    while (meio < len(lista)):
        lista_quarta_metade.append(lista[meio])
        meio += 1
        #print("quarta metade funcionando")
    return lista_quarta_metade  

def primeiro(lista):
    lista_primeiro = []
    meio = int(len(lista)/4)
    while (meio > -1):
        lista_primeiro.append(lista[meio])
        meio -= 1
    return lista_primeiro

def exibicao_lista(primeiro, segunda_metade, terceira_metade, quarta_metade, lista):
    print("Lista primeira metade: ")
    print(primeiro(lista))

    print("Lista segunda metade: ")
    print(segunda_metade(lista))

    print("Lista terceira metade: ")
    print(terceira_metade(lista))

    print("Lista quarta metade: ")
    print(quarta_metade(lista))

def inicializacao(a,b,c):
    a.start()
    b.start()
    c.start()
    a.join()
    b.join()
    c.join()




