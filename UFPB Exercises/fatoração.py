num = int(input("Digite o número a ser fatorado: "))
fatorial = 1

while (num > 1):
    fatorial = num * fatorial
    num -= 1
    if fatorial > 1000:
        break
 
print(fatorial)
