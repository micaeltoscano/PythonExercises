def contar_digito(num):
    quant = 0
    for n in num:
        quant += 1
    
    return quant

def main():
    num = input("Digite um número: ")
    print(f"{num} tem {contar_digito(num)} digito(s)")

if (__name__ == "__main__"):
    main()