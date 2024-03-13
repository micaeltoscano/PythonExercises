valor = float(input("Digite o valor inicial da dívida: "))
juros_em_porcentagem = float(input("Digite o valor do juros mensal em %: "))
valor_mensal = float(input("Digite o valor mensal a ser pago: "))

juros= juros_em_porcentagem / 100

meses = 0
valor_total_divida = 0

while (valor > 0):
    meses +=  1
    valor = (valor * 1 + juros) - valor_mensal
    valor_total_divida += valor_mensal
print(meses, valor_total_divida)