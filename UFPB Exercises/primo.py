n = int(input("Digite um número para verificar se é primo: "))
primo = True

if n <= 1:
    primo = False

else:
    for i in range(2,n):
        div = n % i
        if (div == 0):
            primo = False
            break

if primo:
    print("É primo!")
else:
    print("Não é primo!")

        