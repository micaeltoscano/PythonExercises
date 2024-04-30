matriz = [[1,2,3], [4,5,6], [7,8,9]]
#Criação do loop para aparecer a primeira matriz:
print("Primeira matriz: ")
for n in range(3):
    print(matriz[n])
#Pegar os valores correspondentes de cada linha/coluna e trocá-los durante o loop
for m in range(3):
    coluna_2 = matriz[m][1]
    linha_2 = matriz[1][m]
    matriz[1][m] = coluna_2
    matriz[m][1] = linha_2
#Criação do segundo loop com os valores trocados
print("Segunda matriz:")
for s in range(3):
    print(matriz[s])