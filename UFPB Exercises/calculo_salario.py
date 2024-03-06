ganhos_hora = float(input("Digite o quanto você ganha por hora: "))
quant_horas= float(input("Digite quantas horas você trabalha por mês: "))
salario = ganhos_hora * quant_horas

print(f"""Salário bruto: {salario:.2f}
Valor pago ao Imposto de renda: {salario * (11/100):.2f} 
Valor pago ao INSS: {salario * (8/100):.2f}
Valor pago ao sindicato: {salario * (5/100):.2f}
Salário líquido: {salario*0.76:.2f}""")
