def eliminar_brancos(frase):
    frase_formatada = ""
    for n in frase:
        if n != " ":
            frase_formatada += n
    
    return frase_formatada

def main():
    frase = input("Digite uma frase: ")
    print(f"A frase formatada é {eliminar_brancos(frase)}")

if (__name__ == "__main__"):
    main()