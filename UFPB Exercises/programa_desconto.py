valor = float(input("Digite o valor do produto: "))
forma_de_pagamento = input("Qual forma de pagamento (Dinheiro ou cheque)?: ")

if valor >= 100 and forma_de_pagamento == "dinheiro":
    print(f"O valor a ser pago será de: {valor * 0.90}")
elif forma_de_pagamento != "dinheiro" and forma_de_pagamento != "cheque":
    print("Forma de pagamento inválida")
else:
    print(f"O valor a ser pago será de {valor}")

