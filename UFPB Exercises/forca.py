import random as rd

def forca():
    fim = False
    turno = 0
    lista_palavras = ["abacaxi", "amigo", "arco", "banana", "barco", "cachorro", "cadeira", "caneta", "carro", "cebola",
    "chinelo", "chocolate", "computador", "copo", "dinossauro", "elefante", "escada", "escova", "espelho", "faca",
    "fogo", "garfo", "gato", "guitarra", "hamburguer", "helicoptero", "igreja", "iluminacao", "impressora", "jacare",
    "janela", "joelho", "lapis", "livro", "lua", "macaco", "melancia", "mesa", "mochila", "navio",
    "ovelha", "palavra", "parede", "passarinho", "peixe", "pipoca", "porta", "queijo", "rato", "sapato",
    "telefone", "tigre", "uva", "vaca", "ventilador", "viagem", "xadrez", "zebra"]

    palavra_aleatoria = rd.choice(lista_palavras)

    display = []
    for n in range(len(palavra_aleatoria)):
        display.append(" _ ")

    while not fim:
        
        letra = input("Digite uma letra: ")

        for m in range(len(palavra_aleatoria)):
            tentativa = palavra_aleatoria[m]

            if letra == tentativa:
                display[m] = letra

        if letra not in palavra_aleatoria:
            turno += 1
            print(f"Você errou pela {turno}º vez")

        else:
            print(f"A palavra é: {display}")

        if " _ " not in display:
            print("Você acertou!")
            fim = True

        if turno == 6:
            fim = True
            print(f" Você perdeu! A palavra era {palavra_aleatoria}! ")

def main():
    forca()

if (__name__ == "__main__"):
    main()



   