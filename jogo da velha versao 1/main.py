import pygame as pg
import random

loop = True
cooldown= 1000
ultimo_clique = 0

pg.init()
a1= [ ]
a2= [ ]
a3= [ ]
a4= [ ]
a5= [ ]
a6= [ ]
a7= [ ]
a8= [ ]
a9= [ ]

def adicionar_ia(x):
    x.append(2)
    x.append(2)

window= pg.display.set_mode([920, 500])
imagem_jdv= pg.image.load("png-transparent-cat-tic-tac-toe-game-animal-team-cat-game-angle-animals.png")
imagem_x= pg.image.load("kisspng-tic-tac-toe-oxo-holiday-tic-tac-toe-game-blue-cross-5ae92d39a25973.266227491525230905665.jpg")
x_red= pg.transform.scale(imagem_x, (100, 100))
imagem_cont = imagem_jdv.get_rect()

imagem_0= pg.image.load("png-transparent-circle-white-circle-white-monochrome-black-thumbnail.png")
o_red= pg.transform.scale(imagem_0, (100, 100))

def desenhar():
    window.blit(imagem_jdv, (0, 0))
def movimento_jogador():
    mouseX, mouseY = pg.mouse.get_pos()
    if imagem_cont.collidepoint(mouseX, mouseY):
        if mouseX >= 364 and mouseX <= 549 and mouseY >=200 and mouseY <= 338:  #577 direita, #152 esquerda, #363 meio
            imagem_jdv.blit(x_red,(410, 216))
            a5.append(1)         
        if mouseX >= 577 and mouseX <= 762 and mouseY >= 200 and mouseY <= 335:
            imagem_jdv.blit(x_red,(600, 215))
            a6.append(1)  
        if mouseX >= 152 and mouseX <= 337 and mouseY >= 200 and mouseY <= 335:
            imagem_jdv.blit(x_red,(220, 215))
            a4.append(1)  
        if mouseX >= 363 and mouseX <= 548 and mouseY >= 40 and mouseY <= 174:
            imagem_jdv.blit(x_red,(410, 50))
            a2.append(1)
        if mouseX >= 152 and mouseX <= 337 and mouseY >= 40 and mouseY <= 174:
            imagem_jdv.blit(x_red,(220, 50))
            a1.append(1)  
        if mouseX >= 577 and mouseX <= 762 and mouseY >= 40 and mouseY <= 174:
            imagem_jdv.blit(x_red,(600, 50))
            a3.append(1)  
        if mouseX >= 152 and mouseX <= 337 and mouseY >= 364 and mouseY <= 499:
            imagem_jdv.blit(x_red,(220, 380))
            a7.append(1)  
        if mouseX >= 363 and mouseX <= 548 and mouseY >= 364 and mouseY <= 499:
            imagem_jdv.blit(x_red,(410, 380))
            a8.append(1)  
        if mouseX >= 577 and mouseX <= 762 and mouseY >= 364 and mouseY <= 499:
            imagem_jdv.blit(x_red,(600, 380))
            a9.append(1)  
        print(mouseX, mouseY)
def movimento_ia():
    def movimento(y):
        # Se o Jogador Artificial ou seu oponente tiver duas marcações em sequência, marque o quadrado restante
        #fazer trinca:
        if len(a1) == y and len(a2) == y and len(a3) == 0 or len(a9) == y and len(a6) == y and len(a3) == 0:
            imagem_jdv.blit(o_red,(600, 50)) #para a3
            adicionar_ia(x=a3)
        elif len(a4) == y and len(a5) == y and len(a6) == 0:
            imagem_jdv.blit(o_red,(600, 215)) #para a6
            adicionar_ia(x=a6)    
        elif len(a7) == y and len(a8) == y and len(a9) == 0 or len(a1) == y and len(a5) == y and len(a9) == 0 or len(a3) == y and len(a6) == y and len(a9) == 0:
            imagem_jdv.blit(o_red,(600, 380)) #para a9
            adicionar_ia(x=a9)
        elif len(a3) == y and len(a5) == y and len(a7) == 0 or len(a1) == y and len(a4) == y and len(a7) == 0 or len(a9) == y and len(a8) == y and len(a7) == 0:
            imagem_jdv.blit(o_red,(220, 380)) #para a7
            adicionar_ia(x=a7)
        elif len(a3) == y and len(a2) == y and len(a1) == 0 or len(a7) == y and len(a4) == y and len(a1) == 0:
            imagem_jdv.blit(o_red,(220, 50)) #para a1
            adicionar_ia(x=a1)
        elif len(a6) == y and len(a5) == y and len(a4) == 0 or len(a7) == y and len(a2) == y and len(a4) == 0:
            imagem_jdv.blit(o_red,(220, 215)) #para a4
            adicionar_ia(x=a4)
        elif len(a8) == y and len(a5) == y and len(a2) == 0 or len(a7) == y and len(a4) == y and len(a1) == 0:
            imagem_jdv.blit(o_red,(410, 50)) #para a2
            adicionar_ia(x=a2)
        elif len(a2) == y and len(a5) == y and len(a8) == 0:
            imagem_jdv.blit(o_red,(410, 380)) #para a8
            adicionar_ia(x=a8)
        #impedir trinca jogador:
        elif len(a1) == 1 and len(a2) == 1 and len(a3) == 0 or len(a9) == 1 and len(a6) == 1 and len(a3) == 0 or len(a7) == 1 and len(a5) == 1 and len(a3) == 0:
            imagem_jdv.blit(o_red,(600, 50)) #para a3
            adicionar_ia(x=a3)
        elif len(a4) == 1 and len(a5) == 1 and len(a6) == 0:
            imagem_jdv.blit(o_red,(600, 215)) #para a6
            adicionar_ia(x=a6)    
        elif len(a7) == 1 and len(a8) == 1 and len(a9) == 0 or len(a1) == 1 and len(a5) == 1 and len(a9) == 0 or len(a3) == 1 and len(a6) == 1 and len(a9) == 0:
            imagem_jdv.blit(o_red,(600, 380)) #para a9
            adicionar_ia(x=a9)
        elif len(a3) == 1 and len(a5) == 1 and len(a7) == 0 or len(a1) == 1 and len(a4) == 1 and len(a7) == 0 or len(a9) == 1 and len(a8) == 1 and len(a7) == 0:
            imagem_jdv.blit(o_red,(220, 380)) #para a7
            adicionar_ia(x=a7)
        elif len(a3) == 1 and len(a2) == 1 and len(a1) == 0 or len(a7) == 1 and len(a4) == 1 and len(a1) == 0:
            imagem_jdv.blit(o_red,(220, 50)) #para a1
            adicionar_ia(x=a1)
        elif len(a6) == 1 and len(a5) == 1 and len(a4) == 0 or len(a7) == 1 and len(a1) == 1 and len(a4) == 0:
            imagem_jdv.blit(o_red,(220, 215)) #para a4
            adicionar_ia(x=a4)
        elif len(a8) == 1 and len(a5) == 1 and len(a2) == 0 or len(a7) == 1 and len(a4) == 1 and len(a1) == 0:
            imagem_jdv.blit(o_red,(410, 50)) #para a2
            adicionar_ia(x=a2)
        elif len(a2) == 1 and len(a5) == 1 and len(a8) == 0:
            imagem_jdv.blit(o_red,(410, 380)) #para a8
            adicionar_ia(x=a8)
        # Caso contrário, se houver uma jogada que crie duas linhas com duas marcações em sequência, use-a:
        else:
            if len(a1) == y and len(a2) == 0 or len(a3) == y and len(a2) == 0 or len(a5) == y and len(a2) == 0:
                imagem_jdv.blit(o_red,(410, 50)) #para a2
                adicionar_ia(x=a2)
            elif len(a4) == y and len(a5) == 0 or len(a6) == y and len(a5) == 0:
                imagem_jdv.blit(o_red,(410, 216))
                adicionar_ia(x=a5)
            elif len(a7) == y and len(a8) == 0 or len(a9) == y and len(a8) == 0 or len(a5) == y and len(a8) == 0:
                imagem_jdv.blit(o_red,(410, 380)) #para a8
                adicionar_ia(x=a8)
            elif len(a3) == y and len(a6) == 0 or len(a9) == y and len(a6) == 0 or len(a5) == y and len(a6) == 0:
                imagem_jdv.blit(o_red,(600, 215)) #para a6
                adicionar_ia(x=a6)
            elif len(a1) == y and len(a4) == 0 or len(a7) == y and len(a4) == 0 or len(a5) == y and len(a4) == 0:
                imagem_jdv.blit(o_red,(220, 215)) #para a4
                adicionar_ia(x=a4)
            elif len(a2) == y and len(a1) == 0 or len(a4) == y and len(a1) == 0 or len(a5) == y and len(a1) == 0:
                imagem_jdv.blit(o_red,(220, 50)) #para a1
                adicionar_ia(x=a1)
            elif len(a5) == y and len(a3) == 0:
                imagem_jdv.blit(o_red,(600, 50)) #para a3
                adicionar_ia(x=a3)
            elif len(a5) == y and len(a9) == 0:
                imagem_jdv.blit(o_red,(600, 380)) #para a9
                adicionar_ia(x=a9)
            #Caso contrário, se o quadrado central estiver livre, marque-o;
            else:
                if len(a5) == 0:
                    imagem_jdv.blit(o_red,(410, 216))
                    adicionar_ia(x=a5)
                #Caso contrário, se seu oponente tiver marcado um dos cantos, marque o canto oposto;
                else:
                    if len(a1) == 1: 
                        imagem_jdv.blit(o_red,(600, 50)) #para a3
                        adicionar_ia(x=a3)
                    elif len(a7) == 1:
                        imagem_jdv.blit(o_red,(600, 380)) #para a9
                        adicionar_ia(x=a9)
                    elif len(a3) == 1:
                        imagem_jdv.blit(o_red,(220, 50)) #para a1
                        adicionar_ia(x=a1)
                    elif len(a9) == 1:
                        imagem_jdv.blit(o_red,(220, 380)) #para a7
                        adicionar_ia(x=a7)
                    #Caso contrário, se houver um canto vazio, marque-o;
                    else:
                        if len(a1) == 0: 
                            imagem_jdv.blit(o_red,(220, 50)) #para a1
                            adicionar_ia(x=a1)
                        elif len(a7) == 0:
                            imagem_jdv.blit(o_red,(220, 380)) #para a7
                            adicionar_ia(x=a7)
                        elif len(a3) == 0:
                            imagem_jdv.blit(o_red,(600, 50)) #para a3
                            adicionar_ia(x=a3)
                        elif len(a9) == 0:
                            imagem_jdv.blit(o_red,(600, 380)) #para a9
                            adicionar_ia(x=a9)
                        #Como última alternativa, marque qualquer quadrado vazio.
                        else:
                            if len(a1) == 0: 
                                imagem_jdv.blit(o_red,(220, 50)) #para a1
                                adicionar_ia(x=a1)
                            elif len(a7) == 0:
                                imagem_jdv.blit(o_red,(220, 380)) #para a7
                                adicionar_ia(x=a7)
                            elif len(a3) == 0:
                                imagem_jdv.blit(o_red,(600, 50)) #para a3
                                adicionar_ia(x=a3)
                            elif len(a9) == 0:
                                imagem_jdv.blit(o_red,(600, 380)) #para a9
                                adicionar_ia(x=a9)
                            elif len(a2) == 0:
                                imagem_jdv.blit(o_red,(410, 50)) #para a2
                                adicionar_ia(x=a2)
                            elif len(a4) == 0:
                                imagem_jdv.blit(o_red,(220, 215)) #para a4
                                adicionar_ia(x=a4)
                            elif len(a5) == 0:
                                imagem_jdv.blit(o_red,(410, 216))
                                adicionar_ia(x=a5)
                            elif len(a6) == 0:
                                imagem_jdv.blit(o_red,(600, 215)) #para a6
                                adicionar_ia(x=a6) 
                            else:
                                imagem_jdv.blit(o_red,(410, 380)) #para a8
                                adicionar_ia(x=a8)
    movimento(y=2)
while loop:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            loop = False
        if events.type == pg.MOUSEBUTTONDOWN:
            if events.button == 1:
                tempo_atual = pg.time.get_ticks()
                if tempo_atual - ultimo_clique > cooldown:
                        movimento_jogador()
                        ultimo_clique = tempo_atual
                        movimento_ia()           
    desenhar()
    pg.display.update()
