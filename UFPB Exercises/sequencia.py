def imprimir_sequencia(n):
    for i in range(1, int(n) + 1):
        print((str(i) + " ") * i)

def main():
    n = input("Número de sequências: ")
    imprimir_sequencia(n)

if (__name__ == "__main__"):
    main()