n_imprimidos = int(input("Digite quantos números você deseja que sejam imprimidos na sequência de Fibonacci: "))
termox = 0
termoy = 1

print(termox)
print(termoy)

for n in range(2, n_imprimidos):
    termow = termox + termoy
    termox = termoy
    termoy = termow
    print(termow)
