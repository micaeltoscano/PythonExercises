import pygame as pg
#Criação do loop, do cooldown e inicialização do pygame:
loop = True
cooldown= 000
ultimo_clique = 0
pg.init()
#do a1 ao a9 são as matrizes
a1= [ ]
a2= [ ]
a3= [ ]
a4= [ ]
a5= [ ]
a6= [ ]
a7= [ ]
a8= [ ]
a9= [ ]
#do b1 ao b9 são as listas para contabilizar os cliques do jogador (evitar que a ia conte uma jogada repetida do jogador como uma jogada)
b1= [ ]
b2= [ ]
b3= [ ]
b4= [ ]
b5= [ ]
b6= [ ]
b7= [ ]
b8= [ ]
b9= [ ]
#Criação da interface: 
window= pg.display.set_mode([920, 500])
imagem_jdv= pg.image.load("png-transparent-cat-tic-tac-toe-game-animal-team-cat-game-angle-animals.png")
imagem_x= pg.image.load("kisspng-tic-tac-toe-oxo-holiday-tic-tac-toe-game-blue-cross-5ae92d39a25973.266227491525230905665.jpg")
x_red= pg.transform.scale(imagem_x, (100, 100))
imagem_cont = imagem_jdv.get_rect()
imagem_0= pg.image.load("png-transparent-circle-white-circle-white-monochrome-black-thumbnail.png")
o_red= pg.transform.scale(imagem_0, (100, 100))
#
def contador_de_cliques(mouseX, mouseY):
    #A cada clique do jogador em uma determinada área, o programa irá adicionar 3 números a uma lista (da lista b1 a b9)
    def add_3(z):
        z.append(1)
        z.append(1)
        z.append(1)
    if mouseX >= 364 and mouseX <= 549 and mouseY >=200 and mouseY <= 338:
        add_3(z=b5)
    if mouseX >= 577 and mouseX <= 762 and mouseY >= 200 and mouseY <= 335:
        add_3(z=b6)
    if mouseX >= 152 and mouseX <= 337 and mouseY >= 200 and mouseY <= 335:
        add_3(z=b4)
    if mouseX >= 363 and mouseX <= 548 and mouseY >= 40 and mouseY <= 174:
        add_3(z=b2)
    if mouseX >= 152 and mouseX <= 337 and mouseY >= 40 and mouseY <= 174:
        add_3(z=b1)
    if mouseX >= 577 and mouseX <= 762 and mouseY >= 40 and mouseY <= 174:
        add_3(z=b3)
    if mouseX >= 152 and mouseX <= 337 and mouseY >= 364 and mouseY <= 499:
        add_3(z=b7)
    if mouseX >= 363 and mouseX <= 548 and mouseY >= 364 and mouseY <= 499:
        add_3(z=b8)
    if mouseX >= 577 and mouseX <= 762 and mouseY >= 364 and mouseY <= 499:
        add_3(z=b9)
def condicao_evitar_jogada_repetida():
    #Essa condição serve para evitar que o jogador coloque um X onde há uma O, entao se a posição do clique do meu mouse está entre x e y AND o quadrante tiver len = 2, a condição retorna FALSE
    #OU se a posição do meu mouse estiver entre x e y AND o len do contador de cliques da área (b) for maior que 3, também retorna FALSE e o programa só segue quando retornar TRUE
    mouseX, mouseY = pg.mouse.get_pos()
    if mouseX >= 364 and mouseX <= 549 and mouseY >=200 and mouseY <= 338 and len(a5) == 2 or mouseX >= 364 and mouseX <= 549 and mouseY >=200 and mouseY <= 338 and len(b5) > 3:
        return False 
    if mouseX >= 577 and mouseX <= 762 and mouseY >= 200 and mouseY <= 335 and len(a6) == 2 or mouseX >= 577 and mouseX <= 762 and mouseY >= 200 and mouseY <= 335 and len(b6) > 3:
        return False
    if mouseX >= 152 and mouseX <= 337 and mouseY >= 200 and mouseY <= 335 and len(a4) == 2 or mouseX >= 152 and mouseX <= 337 and mouseY >= 200 and mouseY <= 335 and len(b4) > 3:
        return False
    if mouseX >= 363 and mouseX <= 548 and mouseY >= 40 and mouseY <= 174 and len(a2) == 2 or mouseX >= 363 and mouseX <= 548 and mouseY >= 40 and mouseY <= 174 and len(b2) > 3:
        return False
    if mouseX >= 152 and mouseX <= 337 and mouseY >= 40 and mouseY <= 174 and len(a1) == 2 or mouseX >= 152 and mouseX <= 337 and mouseY >= 40 and mouseY <= 174 and len(b1) > 3:
        return False
    if mouseX >= 577 and mouseX <= 762 and mouseY >= 40 and mouseY <= 174 and len(a3) == 2 or mouseX >= 577 and mouseX <= 762 and mouseY >= 40 and mouseY <= 174 and len(b3) > 3:
        return False
    if mouseX >= 152 and mouseX <= 337 and mouseY >= 364 and mouseY <= 499 and len(a7) == 2 or mouseX >= 152 and mouseX <= 337 and mouseY >= 364 and mouseY <= 499 and len(b7) > 3:
        return False
    if mouseX >= 363 and mouseX <= 548 and mouseY >= 364 and mouseY <= 499 and len(a8) == 2 or mouseX >= 363 and mouseX <= 548 and mouseY >= 364 and mouseY <= 499 and len(b8) > 3:
        return False
    if mouseX >= 577 and mouseX <= 762 and mouseY >= 364 and mouseY <= 499 and len(a9) == 2 or mouseX >= 577 and mouseX <= 762 and mouseY >= 364 and mouseY <= 499 and len(b9) > 3:
        return False     
def condicao_evitar_bordas():
    #A IA só irá jogar se a posição do clique do mouse do jogador estiver nessa determinada área. 
    #OBS: Melhorar código, ILEGÍVEL.
    mouseX, mouseY = pg.mouse.get_pos()
    if imagem_cont.collidepoint(mouseX, mouseY):
        if mouseX >= 364 and mouseX <= 549 and mouseY >=200 and mouseY <= 338 or mouseX >= 577 and mouseX <= 762 and mouseY >= 200 and mouseY <= 335 or mouseX >= 152 and mouseX <= 337 and mouseY >= 200 and mouseY <= 335 or mouseX >= 363 and mouseX <= 548 and mouseY >= 40 and mouseY <= 174 or mouseX >= 152 and mouseX <= 337 and mouseY >= 40 and mouseY <= 174 or mouseX >= 577 and mouseX <= 762 and mouseY >= 40 and mouseY <= 174 or mouseX >= 152 and mouseX <= 337 and mouseY >= 364 and mouseY <= 499 or mouseX >= 363 and mouseX <= 548 and mouseY >= 364 and mouseY <= 499 or mouseX >= 577 and mouseX <= 762 and mouseY >= 364 and mouseY <= 499:
            return True
def desenhar(): #desenhar o jogo da velha
    window.blit(imagem_jdv, (0, 0))
def movimento_jogador():
    mouseX, mouseY = pg.mouse.get_pos()
    if imagem_cont.collidepoint(mouseX, mouseY): #Verifica que o clique do meu mouse está dentro da imagem
        #SE o quadrante que o clique do meu mouse está tiver len = 0, COLOQUE o X na posição x e y e adicione 1 à matriz. 
        if len(a5) == 0:
            if mouseX >= 364 and mouseX <= 549 and mouseY >=200 and mouseY <= 338:  #577 direita, #152 esquerda, #363 meio
                imagem_jdv.blit(x_red,(410, 216))
                a5.append(1)
        if len(a6) == 0:         
            if mouseX >= 577 and mouseX <= 762 and mouseY >= 200 and mouseY <= 335:
                imagem_jdv.blit(x_red,(600, 215))
                a6.append(1)  
        if len(a4) == 0:
            if mouseX >= 152 and mouseX <= 337 and mouseY >= 200 and mouseY <= 335:
                imagem_jdv.blit(x_red,(220, 215))
                a4.append(1) 
        if len(a2) == 0: 
            if mouseX >= 363 and mouseX <= 548 and mouseY >= 40 and mouseY <= 174:
                imagem_jdv.blit(x_red,(410, 50))
                a2.append(1)
        if len(a1) == 0:
            if mouseX >= 152 and mouseX <= 337 and mouseY >= 40 and mouseY <= 174:
                imagem_jdv.blit(x_red,(220, 50))
                a1.append(1)
        if len(a3) == 0:  
            if mouseX >= 577 and mouseX <= 762 and mouseY >= 40 and mouseY <= 174:
                imagem_jdv.blit(x_red,(600, 50))
                a3.append(1)
        if len(a7) == 0:  
            if mouseX >= 152 and mouseX <= 337 and mouseY >= 364 and mouseY <= 499:
                imagem_jdv.blit(x_red,(220, 380))
                a7.append(1) 
        if len(a8) == 0: 
            if mouseX >= 363 and mouseX <= 548 and mouseY >= 364 and mouseY <= 499:
                imagem_jdv.blit(x_red,(410, 380))
                a8.append(1) 
        if len(a9) == 0: 
            if mouseX >= 577 and mouseX <= 762 and mouseY >= 364 and mouseY <= 499:
                imagem_jdv.blit(x_red,(600, 380))
                a9.append(1)  
        contador_de_cliques(mouseX=mouseX, mouseY=mouseY)
    while condicao_evitar_jogada_repetida() == False:
        return False
    return True    
def movimento_ia():
    def adicionar_ia(x):
        x.append(2)
        x.append(2)
    def movimento(y):
        # Se o Jogador Artificial ou seu oponente tiver duas marcações em sequência, marque o quadrado restante
        #fazer trinca:
        if condicao_evitar_bordas():
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
            elif len(a4) == 1 and len(a5) == 1 and len(a6) == 0 or len(a9) == 1 and len(a3) == 1 and len(a6) == 0:
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
                        if len(a1) == 1 and len(a3) == 0: 
                            imagem_jdv.blit(o_red,(600, 50)) #para a3
                            adicionar_ia(x=a3)
                        elif len(a7) == 1 and len(a9) == 0:
                            imagem_jdv.blit(o_red,(600, 380)) #para a9
                            adicionar_ia(x=a9)
                        elif len(a3) == 1 and len(a1) == 0:
                            imagem_jdv.blit(o_red,(220, 50)) #para a1
                            adicionar_ia(x=a1)
                        elif len(a9) == 1 and len(a7) == 0:
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
                                elif len(a8) == 0:
                                    imagem_jdv.blit(o_red,(410, 380)) #para a8
                                    adicionar_ia(x=a8)
    movimento(y=2)
#Cérebro do sistema:    
while loop:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            loop = False
        if events.type == pg.MOUSEBUTTONDOWN:
            if events.button == 1:
                tempo_atual = pg.time.get_ticks()
                if tempo_atual - ultimo_clique > cooldown:
                        if movimento_jogador():
                            ultimo_clique = tempo_atual
                            movimento_ia()  
                            print(a1,a2,a3,a4,a5,a6,a7,a8,a9)         
    desenhar()
    pg.display.update()

#Melhoria da IA
#Melhoria no sistema de matriz
#Melhoria de interface
