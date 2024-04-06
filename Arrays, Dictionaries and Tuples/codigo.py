codigo = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
codificado = []
mensagem = 0
frase_descodificada = ""
#Armazenamento da mensagem codificada
while (mensagem != -1):
    mensagem = int(input("Digite um número a ser descodificado (digite -1 para sair): "))
    #Evitar que o -1 e um número menor que 0 e maior que 26 entrem na lista
    if (mensagem != -1):
        if (mensagem >= 0 and mensagem <= 26):
            codificado.append(mensagem)
#Buscando a letra correspondente ao número buscado
for n in codificado:
    letra_descodificada = codigo[n]
    frase_descodificada += letra_descodificada
print(frase_descodificada)






    