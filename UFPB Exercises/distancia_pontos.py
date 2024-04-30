lista_tuplas = [(),()]
#Criação das listas
lista_cood = [[None]*2 for n in range(2)]
#Atribuição das coordenadas x e y nas listas
for n in range(2):
    lista_cood[n][0] = int(input(f"Digite a coordenada x do {n + 1}º ponto: "))
    lista_cood[n][1] = int(input(f"Digite a coordenada y do {n + 1}º ponto: "))
#Adição dos valores de x na e y nas tuplas correspondentes
coordenadas_ponto_1 = lista_tuplas[0] + (lista_cood[0][0],lista_cood[0][1])
coordenadas_ponto_2 = lista_tuplas[1] + (lista_cood[1][0],lista_cood[1][1])
#Cálculos para aplicação na fórmula de distância euclidiana √((x1 – x2)² + (y1 – y2)²)
x = (coordenadas_ponto_1[0] - coordenadas_ponto_2[0]) ** 2
y = (coordenadas_ponto_1[1] - coordenadas_ponto_2[1]) ** 2
soma = x + y
#Uso da fórmula de newton para cálculo da raiz quadrada
b= 2
p = 0
while True:
    p = (b + soma / b) / 2
    if abs(b - p) < 0.0001:
        break
    b = p
print(f'''
A distância mínima entre os pontos {coordenadas_ponto_1} e {coordenadas_ponto_2} é aproximadamente {b:.2f}
A distância média entre os pontos {coordenadas_ponto_1} e {coordenadas_ponto_2} é aproximadamente {b / 2:.2f}
A distância máxima entre os pontos {coordenadas_ponto_1} e {coordenadas_ponto_2} é aproximadamente {b:.2f}''')
