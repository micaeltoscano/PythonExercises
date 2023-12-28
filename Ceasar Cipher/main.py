alfabeto= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encriptar(frase_2, shift_2):
    palavra_encriptada = " "
    for l in frase:
        if l in alfabeto:
            indexo= int(alfabeto.index(l))
            valor_att= indexo + shift_2
            letra_att= alfabeto[valor_att]
            palavra_encriptada += letra_att
        else: 
             palavra_encriptada += ' '

    print(palavra_encriptada)

def desencriptar(frase_2, shift_2):
    palavra_desencriptada = " "
    for l in frase:
        if l in alfabeto:
            indexo= int(alfabeto.index(l))
            valor_att= indexo - shift_2
            letra_att= alfabeto[valor_att]
            palavra_desencriptada += letra_att
        else: 
             palavra_desencriptada += ' '

    print(palavra_desencriptada)

frase= input("Frase: ")
shift= int(input("Qual é o shift desejado?: "))

escolha= int(input("""O que deseja?
Para Encriptar: digite 1
Para Desencriptar: digite 2 
Escolha: """ ))

if escolha == 1:
    encriptar(frase_2=frase, shift_2=shift)

elif escolha == 2: 
    desencriptar(frase_2=frase, shift_2=shift)






        
