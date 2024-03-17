import csv

def codificar(shift):
    #Leitura do arquivo a ser codificado:
    texto = "test.txt"
    with open(texto, "r") as file:
        conteudo = file.read()

    frase_encriptada = ""
    for i in conteudo:
        soma = ord(i) + shift
        #Limitando ao número 126 da tabela ASCII:
        if soma > 126:
            soma = 31 + (soma % 126) 
            frase_encriptada = frase_encriptada + chr(soma)
        else:
            frase_encriptada = frase_encriptada + chr(soma)
    print(frase_encriptada)

def descodificar(shift):
    #Leitura do arquivo a ser descodificado:
    descodificado = "descodificar.txt"
    with open(descodificado, "r") as file_descodificado:
        conteudo_descodificado = file_descodificado.read()

    frase_descodificada = ""
    for n in conteudo_descodificado:
        sub = ord(n) - shift
        #Limitando para o número não ser menor que 32
        if sub < 32:
            sub = 126 - (31 % sub)
            frase_descodificada = frase_descodificada + chr(sub)
        else:
            frase_descodificada = frase_descodificada + chr(sub)
    print(frase_descodificada)

shift = int(input("Qual é o shift desejado? "))
opcao = int(input("Digite 1 para codificar e 2 para descodificar: "))
if opcao == 1:
    codificar(shift=shift)
else:
    descodificar(shift=shift)

