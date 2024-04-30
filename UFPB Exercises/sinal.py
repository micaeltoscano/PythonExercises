def sinal(num):
    if num <= 0:
        return "N"
    else:
        return "P"
    
def main():
    num = int(input("Digite um número: "))
    print(sinal(num))

if __name__ == "__main__":
    main()