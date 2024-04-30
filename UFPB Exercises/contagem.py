def contagem(frase):
    dic = {}

    for letra in frase:

        if letra in dic:
            dic[letra] += 1

        else:
            dic[letra] = 1

    return dic

def main():
   frase = input("Digite uma frase: ")
   print(contagem(frase))

if __name__ == "__main__":
    main()
