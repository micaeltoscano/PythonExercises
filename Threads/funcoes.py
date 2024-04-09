def segunda_metade(lista):
    lista_segunda_metade = []
    meio = (len(lista)/4 + 1)
    while (meio < len(lista) / 2):
        lista_segunda_metade.append(lista[meio])
        meio += 1
        #print("segunda metade funcionando")
    return max(lista_segunda_metade)   
 
def terceira_metade(lista):
    lista_terceira_metade = []
    meio = (len(lista)/2 + 1)
    while (meio < (len(lista) / 2 + len(lista) / 4)):
        lista_terceira_metade.append(lista[meio])
        meio += 1
        #print("terceira metade funcionando")
    return max(lista_terceira_metade)    


def quarta_metade(lista):
    lista_quarta_metade = []
    meio = (len(lista) / 2 + len(lista) / 4) + 1
    while (meio < len(lista)):
        lista_quarta_metade.append(lista[meio])
        meio += 1
        #print("terceira metade funcionando")
    return max(lista_quarra_metade)    




