valor = float(input("Digite o valor do produto: "))
forma_de_pagamento = input("Qual forma de pagamento (Dinheiro, cheque, débito ou crédito)?: ")

if forma_de_pagamento == "crédito":
    parcelas = int(input("Digite o número de parcelas: "))
    if parcelas > 3:
        print("O número de parcelas não pode exceder 3!")
    else:
        print(f"O valor no crédito, dividido em {parcelas} parcelas, será de: {valor / parcelas}")
else:
    print(f"O total, no {forma_de_pagamento}, a ser pago será de: {valor}")


