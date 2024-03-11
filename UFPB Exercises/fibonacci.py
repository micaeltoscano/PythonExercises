n_imprimidos = int(input("Digite quantos números você deseja que sejam imprimidos na sequência de Fibonacci: "))
contador = 2
soma = 0
termox = 0
termoy = 1

while (contador <= n_imprimidos):
    termow = termox + termoy 
    termox = termoy
    termoy = termow
    contador += 1
    
print(termow)

    