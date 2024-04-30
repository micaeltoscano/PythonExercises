def numero_extenso(num):
    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    especiais = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

    if 0 <= int(num) <= 9:
        return unidades[int(num)]
    
    elif 10 <= int(num) <= 19:
        return especiais[int(num) - 10]
    
    elif 20 <= int(num) <= 99:

        if num[1] == "0":
            return dezenas[int(num[0]) - 2]
        
        else:
            return dezenas[int(num[0]) - 2], unidades[int(num[1])]    

def main():
    num = input("Digite um número: ")
    
    if int(num) < 19:
        print(numero_extenso(num))

    elif num[1] == "0":
        print(f"{numero_extenso(num)}")

    else:
        print(f"{numero_extenso(num)[0]} e {numero_extenso(num)[1]}")

if (__name__ == "__main__"):
    main()