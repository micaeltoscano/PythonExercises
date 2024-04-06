#Criação das listas vinculadas.
lista= [[None]*2 for n in range(10)]
#Atribuição do tamanho e do sexo do indivíduo na lista:
for n in range(10):
    lista[n][0] = float(input("Digite a altura: "))
    lista[n][1] = input("digite o sexo: ")
#Verificação de maior ou menor. 
maior = 0
menor = 5.0
for j in range(len(lista)):
    if (lista[j][0] > maior):
        maior = lista[j][0]
    if (menor > lista[j][0]):
        menor = lista[j][0]
#Atribuir ao index em qual lista o item de maior valor está localizado
index = 0
for k in range(len(lista)):
    if lista[k][0] == maior:
        index = k
#Atribuir ao index_menor em qual lista o item de menor valor está localizado
index_menor = 0
for l in range(len(lista)):
    if lista[l][0] == menor:
        index_menor = l
#Com a localização, é possível determinar qual o sexo do invidíduo de maior/menor altura
print(f'''
A maior altura foi {maior}, sendo ela de um indivíduo de sexo {lista[index][1]}
A menor altura foi {menor}, sendo ela de um indivíduo de sexo {lista[index_menor][1]}''')
#Para fazer a média, é preciso localizar todos os valores correspondentes ao sexo dos indivíduos e colocá-los em listas
media_altura_f = []
media_altura_m = []
for v in range(len(lista)):
    if lista[v][1] == "f":
        media_altura_f.append(lista[v][0]) 
    elif lista[v][1] == "m":
        media_altura_m.append(lista[v][0])
#Com as listas feitas, é preciso criar um somatório
somatorio_mulheres = 0
for w in media_altura_f:
    somatorio_mulheres += w
somatorio_homens = 0
for t in media_altura_m:
    somatorio_homens += t
#E para finalizar, divide-se o somatório pela quantidade de indivíduos de cada sexo
print(f'''
A média de altura das mulheres foi: {somatorio_mulheres / len (media_altura_f):.2f}
A média de altura dos homens foi: {somatorio_homens / len(media_altura_m):.2f}''')
#Para determinar o total, basta ver o tamanho das listas que contêm a quantidade de indivíduos de cada sexo
print(f"O total de mulheres foi: {len(media_altura_f)} e o total de homens foi: {len(media_altura_m)}")
