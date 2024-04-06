#Criação do loop que irá pedir uma nova frase até o usuário digitar 1
while True: 
    #Dicionário dentro do loop para que os values voltem a zero ao fim de cada iteração
    dicionario = {" ":0,"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    lista = {}
    caracteres = []
    frase = input("Digite uma frase (digite 1 para sair): ")
    if (frase == "1"):
        break
    #Buscar o value correspondente de cada letra de "frase" e adicionar 1 cada vez que aparecer
    for n in frase:
        #Evitar que um caractere que não está no dicionário seja utilizado
        if n in dicionario:
            if n != " ":
                dicionario[n] += 1
                #Adição de cada letra no dicionário com o value correspondente
                lista[n] = dicionario[n]
        #Adicionar os caracteres em uma lista para mostrar quais não foram utilizados
        else:
            caracteres.append(n)
    print(f'''
As letras na frase/palavra "{frase}" tiveram esse índice de aparecimento: 
{lista}
não contamos os caracteres: {caracteres}''')

