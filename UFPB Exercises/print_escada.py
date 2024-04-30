def escada(frase):
    frase_nova = ""
    for n in frase:
        frase_nova += n

        print(frase_nova)
    
def main():
    frase = input("Digite uma frase: ")
    escada(frase)

if (__name__ == "__main__"):
    main()
