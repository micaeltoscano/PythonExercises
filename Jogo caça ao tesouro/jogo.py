import pygame as pg
import random as rd
import matriz
import jogar_novamente
import time


def desenhar_tabuleiro(tela):
    #Passando os parametros para o desenho do tabuleiro do jogo
    preto = (0,0,0)
    altura = 100
    largura = 100

    for i in range(1, 5):
        for j in range(1, 5):
            #Desenha retângulos que são desenhados conforme a execução do laço for
            pg.draw.rect(tela, preto, (i*largura, j*altura, largura, altura), 1)

def distribuindo_itens(matriz_a):
    #Utiliza a "matriz" para distribuir X, Y e inteiros numa matriz
    for n in range(6):
        matriz.adicionar_item("X", matriz_a)
    for m in range(3):
        matriz.adicionar_item("Y", matriz_a)
    for l in range(7):
        aleatorio = rd.randint(1,3)
        matriz.adicionar_item(aleatorio, matriz_a)

def contagem(tela, jogador_1, jogador_2):
    fonte = pg.font.Font(None, 36)

    tela.fill((255, 255, 255), (550, 100, 550, 200))

    texto = fonte.render(f"Jogador 1 -{jogador_1}", True, (0,0,0))
    tela.blit(texto, (550, 100))

    texto_2 = fonte.render(f"Jogador 2 - {jogador_2} ", True, (0,0,0))
    tela.blit(texto_2, (550, 200))

def vencedor(tela, jogador_1, jogador_2):

    fonte = pg.font.Font(None, 36)
    tela.fill((255, 255, 255), (550, 100, 550, 200))

    if jogador_1 > jogador_2:
        nome_vencedor = "jogador 1"
        
    elif jogador_1 < jogador_2:
        nome_vencedor = "jogador 2"

    nome_vencedor = fonte.render(f"O vencedor: {nome_vencedor}!", True, (0,0,0)) 

    tela.blit(nome_vencedor, (510,150))
    pg.mixer.music.load('applause.ogg')
    pg.mixer.music.play(1)

def sistema(tela, matriz_a, matriz_b, tesouro, buraco, um, dois,tres):
    turno = 0
    jogador_1 = 0
    jogador_2 = 0
    fonte = pg.font.Font(None, 36)
    while True:
        vazio = False
        for evento in pg.event.get(): 
            if evento.type == pg.QUIT:
                pg.quit()
                quit()

            if evento.type == pg.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    x,y = pg.mouse.get_pos()
                    #Garantir que o mouse esteja dentro do tabuleiro
                    if 100 < x < 500 and 100 < y < 500:
                        coord_x = (x // 100) - 1 # -1 para evitar erro de index
                        coord_y = (y // 100) - 1

                        #Criação de uma matriz para evitar jogadas repetidas
                        if matriz_b[coord_x][coord_y] == False:
                            vazio = True 
                            matriz_b[coord_x][coord_y] = True

            #Caso aquela região esteja vazia:           
            if vazio:
                turno += 1 #Criação do turno para jogadas
                print(f"turno: {turno}")

                #Pegando as coordenadas do mouse calculadas
                a, b= coord_x, coord_y
                print(matriz_a[a][b])

                #Caso naquela posição esteja um "X", sera desenhado um tesouro naquela região
                if matriz_a[a][b] == "X":
                    # Se o turno for ímpar, jogador 1 ganha os pontos , e se for par, jogador 2 ganha.
                    if (turno % 2 != 0):
                        jogador_1 += 100
                    else:
                        jogador_2 += 100
                    #Função do pygame para aplicar imagens em determinada coordena. 
                    tela.blit(tesouro, (coord_x * 100 + 100, coord_y * 100 + 100))

                #Caso naquela região esteja um "Y", será desenhado um buraco naquela região
                if matriz_a[a][b] == "Y":
                    #Para evitar placares negativos
                    if jogador_1 > 0 and jogador_2 > 0:
                        #Se o turno for ímpar, o jogador 1 perde pontos e vice-versa
                        if (turno % 2 != 0):
                            jogador_1 -= 50
                        else:
                            jogador_2 -= 50

                    tela.blit(buraco, (coord_x * 100 + 100, coord_y * 100 + 100))

                matriz.desenhar_no_tabuleiro(tela, matriz_a, a, b, um, dois, tres, coord_x, coord_y)

                #Chama a função contagem para contabilizar a pontuação dos jogadores
                contagem(tela, jogador_1, jogador_2)
                #print(f"pontuação 1: {jogador_1}, pontuação 2: {jogador_2}")

                #Caso o turno seja igual a 16, ocorre a comparação dos pontos e determina o jogador
                if turno == 16:
                    vencedor(tela, jogador_1, jogador_2)
                    pg.display.update()
                    time.sleep(3)
                    #Leva para uma nova interface
                    jogar_novamente.tela_jogar_novamente()
                    
        pg.display.update()

def jogo():

    pg.init()
    tesouro = pg.image.load("tesouro.png")
    tesouro = pg.transform.scale(tesouro, (100,100))

    buraco = pg.image.load("buraco.jpg")
    buraco = pg.transform.scale(buraco, (100,100))

    um = pg.image.load("1.png")
    um = pg.transform.scale(um, (100,100))

    dois = pg.image.load("2.png")
    dois = pg.transform.scale(dois, (100,100))

    tres = pg.image.load("3.png")
    tres = pg.transform.scale(tres, (100,100))



   
    matriz_a = [[None]*4 for _ in range(4)]
    matriz_b = [[False]*4 for _ in range(4)]

    tela = pg.display.set_mode((800, 600))
    tela.fill((255, 255, 255))

    #fundo = pg.image.load("fundo.jpg")
    #tela.blit(fundo, (0,0))

    distribuindo_itens(matriz_a)

    desenhar_tabuleiro(tela)

    sistema(tela, matriz_a, matriz_b, tesouro, buraco, um, dois, tres)

    

