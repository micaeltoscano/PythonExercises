def comprimento_string(lista):
    if (len(lista[0]) == len(lista[1])):
        return True
    else:
        return False

def comparar_conteudo(lista):
    if (lista[0] == lista[1]):
        return True
    else:
        return False

def main():
    #Criação de uma lista para armazenar strings
    lista_frase = []
    #Loop para ler e adicionar as strings na lista
    for n in range(2):
        lista_frase.append(input(f"Digite a {n+1}º frase: "))
    #Comparando as strings:
    if (comprimento_string(lista_frase) and comparar_conteudo(lista_frase)):
        print("Ambas strings possuem mesmo tamanho e o mesmo conteúdo! ")
    elif (comprimento_string(lista_frase) and not comparar_conteudo(lista_frase)):
        print("Ambas strings possuem mesmo tamanho, mas conteúdos diferentes! ")
    else:
        print("Ambas strings possuem tamanhos diferentes e conteúdos diferentes! ")
    
if (__name__ == "__main__"):
    main()
