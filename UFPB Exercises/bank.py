#Crie um programa para gerenciar uma conta bancária, apresentando o seguinte menu para o usuário:

x = 0
saldo = 0

while (x != 4):

    print("""
    <1> Depositar
    <2> Sacar
    <3> Consultar saldo
    <4> Sair
        """)
    
    x= int(input("Digite a opção desejada: "))
    if (x == 1):
        deposito = float(input("Digite o valor que você deseja depositar: "))
        saldo += deposito
    elif (x == 2):
        saque = float(input("Digite o valor que você deseja sacar: "))
        if saque > saldo:
            print("transação recusada! Saldo insuficiente.")
        else:
            saldo -= saque
    else:
        print(f"Seu saldo é {saldo}")
