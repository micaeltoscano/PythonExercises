import random

fichas_texto = {
    "Ficha Branca": [    
        " ______ ",
        "|      |",
        "|  $1  |",
        "|______|",
    ],
    "Ficha Vermelha": [
        " ______ ",
        "|      |",
        "|  $5  |",
        "|______|",
    ],
    "Ficha Verde": [
        " ______ ",
        "|      |",
        "| $10  |",
        "|______|",
    ],
    "Ficha Azul": [
        " ______ ",
        "|      |",
        "| $15  |",
        "|______|",
    ],
    "Ficha Preta": [
        " ______ ",
        "|      |",
        "| $20 |",
        "|______|",
    ],
    "Ficha Roxa": [
        " ______ ",
        "|      |",
        "| $25 |",
        "|______|",
    ],
    "Ficha Laranja": [
        " ______ ",
        "|      |",
        "| $50|",
        "|______|",
    ],
    "Ficha Rosa": [
        " ______ ",
        "|      |",
        "| $100|",
        "|______|",
    ]
}
valores_ficha= [1,5,10,15,20,25,50,100]
baralho = {
    "Ás": [
        "┌─────────┐",
        "│ A       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       A │",
        "└─────────┘",
    ],
    "2": [
        "┌─────────┐",
        "│ 2       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       2 │",
        "└─────────┘",
    ],
    "3": [
        "┌─────────┐",
        "│ 3       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       3 │",
        "└─────────┘",
    ],
    "4": [
        "┌─────────┐",
        "│ 4       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       4 │",
        "└─────────┘",
    ],
    "5": [
        "┌─────────┐",
        "│ 5       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       5 │",
        "└─────────┘",
    ],
    "6": [
        "┌─────────┐",
        "│ 6       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       6 │",
        "└─────────┘",
    ],
    "7": [
        "┌─────────┐",
        "│ 7       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       7 │",
        "└─────────┘",
    ],
    "8": [
        "┌─────────┐",
        "│ 8       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       8 │",
        "└─────────┘",
    ],
    "9": [
        "┌─────────┐",
        "│ 9       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       9 │",
        "└─────────┘",
    ],
    
    "J": [
        "┌─────────┐",
        "│ J       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       J │",
        "└─────────┘",
    ],
    "Q": [
        "┌─────────┐",
        "│ Q       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       Q │",
        "└─────────┘",
    ],
    "K": [
        "┌─────────┐",
        "│ K       │",
        "│         │",
        "│    ♠    │",
        "│         │",
        "│       K │",
        "└─────────┘",
    ],
}
cartas = {   
    "Ás": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "J": 10,
    "Q": 10,
    "K": 10,
}

def desenhar_carta(x):             # O "x" representa uma variável que é alterada durante o código, para desenhar as cartas aleatórias
    desenho_carta= baralho[x]
    for linha in desenho_carta:    # Para evitar que as cartas sejam desenhadas quebradas no output, utiliza-se esse comando for para desenhar linha por linha
        print(linha)

def desenhar_fichas(ficha):
    desenho_ficha= fichas_texto[ficha] # Mesma lógica passada, mas preciso que todas as fichas sejam printadas, então utilizo o "[ficha]" para pegar o item do dicionário. 
    for linha in desenho_ficha:          
        print(linha)

def exibir_relatorio(cash_atual):
    if cash_atual >= 100:
        print("Parabéns, você ganhou!")
        return True
    elif cash_atual <= 0:
        print("Você está sem fichas! Tente novamente")
        return True
    return False
    
def blackjack():
    
    cash_atual= 10

    jogar= True

    while jogar:
        banco= []            #Começa com os bancos vazios para que quando a proxima rodada comece, ele seja atualizado com novas cartas
        banco_robo= []

        primeira_carta_jogador= random.choice(list(baralho.keys()))   #Como o random.choice não identifica corretamente o comando Keys(), transformo eles em lista com o list()
        segunda_carta_jogador= random.choice(list(baralho.keys()))
        banco.append(cartas[primeira_carta_jogador]) #Acrescenta as cartas na lista 
        banco.append(cartas[segunda_carta_jogador])


        primeira_carta_robo= random.choice(list(baralho.keys()))
        segunda_carta_robo= random.choice(list(baralho.keys()))
        banco_robo.append(cartas[primeira_carta_robo])
        banco_robo.append(cartas[segunda_carta_robo])

        def puxar_mais_uma():
            nova_carta_jogador= random.choice(list(baralho.keys()))
            desenhar_carta(x=nova_carta_jogador)
            banco.append(cartas[nova_carta_jogador])

        def puxar_mais_uma_robo():
            nova_carta_robo= random.choice(list(baralho.keys()))
            banco_robo.append(cartas[nova_carta_robo])
        
        for ficha in fichas_texto:    # E aqui uso o for para loopar entre todas as cartas dentro do dicionario de fichas
            desenhar_fichas(ficha)

        valor_da_ficha= int(input("Digite o valor da ficha que deseja apostar: ")) #Pergunta ao usuário o valor da ficha
        if valor_da_ficha not in valores_ficha:
            print("Digite um valor que esteja listado!")
            
        elif valor_da_ficha > cash_atual:
            print("Você digitou um valor maior do que o seu saldo! Tente outro") #Evita que o usuário use um valor não listado
        else:
                
            print(" Suas cartas foram: ")

            desenhar_carta(x=primeira_carta_jogador)
            desenhar_carta(x= segunda_carta_jogador)

            print(" A primeira carta do computador foi: ")

            desenhar_carta(x=primeira_carta_robo)  

            #Verificar se o jogador ou o computador obtiveram um blackjack de cara
            if primeira_carta_jogador == "Ás" and segunda_carta_jogador == "K" or primeira_carta_jogador == "Ás" and segunda_carta_jogador == "J" or primeira_carta_jogador == "Ás" and segunda_carta_jogador == "Q": 
                print("O jogador ganhou por blackjack!")
                cash_atual += valor_da_ficha
                print(f"""Relatório:
cartas do jogador: {banco} 
cartas do computador: {banco_robo}
cash atual: {cash_atual}""")
                break

            elif primeira_carta_robo == "Ás" and segunda_carta_robo == "K" or primeira_carta_robo == "Ás" and segunda_carta_robo == "J" or primeira_carta_robo == "Ás" and segunda_carta_robo == "Q": 
                print("O computador ganhou por blackjack!")
                cash_atual -= valor_da_ficha
                print(f"""Relatório:
cartas do jogador: {banco} 
cartas do computador: {banco_robo}
cash atual: {cash_atual}""")
                break

            else: #caso contrário, 

                while sum(banco) < 21:   #pergunto ao usuário se ele quer continuar puxando cartas, caso o somatório seja menor que 21
                        
                    puxar_mais_carta= input("Deseja puxar mais uma carta? S/N ").lower()

                    if puxar_mais_carta == "s":
                        print("Sua nova carta é: ")
                        puxar_mais_uma()

                    else:
                        break

                while sum(banco_robo) < 17: #Caso a soma das cartas do robô sejam menor que 17, ele puxará outra carta.
                    puxar_mais_uma_robo()

                #verificações do resultado do jogo:            
                if sum(banco) > 21 and sum(banco_robo) <= 21:
                    print("A soma de suas cartas foi maior que 21, portanto você perdeu")
                    cash_atual -= valor_da_ficha
                    print(f"""Relatório:
cartas do jogador: {banco}
cartas do computador: {banco_robo}
cash atual: {cash_atual}""")
                        
                elif sum(banco_robo) > 21 and sum(banco) <= 21:
                    print("A soma das cartas do robô ultrapassou 21, portanto você venceu")
                    cash_atual += valor_da_ficha
                    print(f"""Relatório:
cartas do jogador: {banco}
cartas do computador: {banco_robo}
cash atual: {cash_atual}""")
                        
                elif sum(banco) > 21 and sum(banco_robo) > 21:
                    print("Ambos tiveram soma acima de 21, portanto empate")
                    print(f"""Relatório:
cartas do jogador: {banco} 
cartas do computador: {banco_robo}
cash atual: {cash_atual}
                                                    """)
                           
                else:
                    if sum(banco) > sum(banco_robo):
                        print("A soma de suas cartas foi maior do que a do robô, portanto você venceu")
                        cash_atual += valor_da_ficha
                        print(f"""Relatório:
cartas do jogador: {banco} 
cartas do computador: {banco_robo}
cash atual: {cash_atual}
                                                    """)
                            
                    elif sum(banco) < sum(banco_robo):
                         print("A soma de suas cartas foi menor do que a do robô, portanto você perdeu")
                         cash_atual -= valor_da_ficha
                         print(f"""Relatório:
cartas do jogador: {banco} 
cartas do computador: {banco_robo}
cash atual: {cash_atual}
                                                    """)
                            
                    else:
                        print("A soma de suas cartas foi igual a do robô, portanto vocês empataram")
                        print(f"""Relatório:
cartas do jogador: {banco} 
cartas do computador: {banco_robo}
cash atual: {cash_atual}
                                                    """)
 
        if exibir_relatorio(cash_atual):
            jogar = False
        else:
            verificacao = input("Deseja continuar apostando? S/N ").lower()
            if verificacao == "n":
                jogar = False
              
           
print(""" 

BEM VINDO AO BLACKJACK.COM!
VOCÊ INICIA COM UM VALOR DIGITAL DE 10 FICHAS
CASO CONSIGA ATINGIR 100 FICHAS, VOCÊ GANHA O JOGO
          
""")
blackjack()


