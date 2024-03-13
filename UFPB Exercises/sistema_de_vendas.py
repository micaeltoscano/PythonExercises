somatorio = 0
codigo = True
while codigo:
    print("""
Código   Valor
  1 ---> 5,50 
  2 ---> 2,30 
  3 ---> 4,75 
  4 ---> 6,80
  5 ---> 9,30 
 """)
    codigo = int(input("Digite o código do produto (digite 0 para sair): "))
    while (codigo < 0 or codigo > 5):
        codigo = int(input(" Código inválido! Digite um código válido: "))
    if (codigo == 0):
        codigo = False
    elif (codigo == 1):
        somatorio += 5.50
    elif (codigo == 2):
        somatorio += 2.30
    elif (codigo == 3):
        somatorio += 4.75
    elif (codigo == 4):
        somatorio += 6.80
    else:
        somatorio += 9.30
    print("O item foi adicionado à sacola com sucesso! (Digite 0 se deseja parar)")

print(f"O total foi: {somatorio}")
    