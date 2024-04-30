import pygame as pg
import jogo
import interface


def main():
    #Inicializando o pygame, determinando os tamanhos e aplicando o plano de fundo:
    pg.init() 
    
    largura, altura = 800, 600
    tela = pg.display.set_mode((largura, altura))
    fundo = pg.image.load("fundo.jpg")
    
    tela.blit(fundo, (0,0))
    pg.display.set_caption("Caça ao tesouro")

    branco = (255, 255, 255)
    verde = (0, 255, 0)

    #Usando o arquivo interface para criação dos botões da tela inicial
    botao_iniciar, botao_sair = interface.criar_botoes(largura, altura)

    while True:
        #Usando uma função do pygame para detectar eventos do código
        for evento in pg.event.get():
            if evento.type == pg.QUIT: #Para encerrar a execução do pygame
                pg.quit()
                quit()
                
            elif evento.type == pg.MOUSEBUTTONDOWN: #Detectar quando o botão do mouse é pressionado
                if botao_iniciar.collidepoint(evento.pos): #Caso a posição do mouse esteja "No ponto de colisão" do botão iniciar, o jogo é iniciado
                    jogo.jogo()
                            
                elif botao_sair.collidepoint(evento.pos): #Caso a posição do mouse esteja "No ponto de colisão" do botão sair, o jogo é encerrado
                    pg.quit()
                    quit()

        #Desenhando os botões usando a interface
        interface.desenhar_botoes(botao_iniciar, botao_sair, tela, verde, branco, "Iniciar", "Sair")
        #Utilizando a função do pygame para atualizar a tela
        pg.display.update()
        
if(__name__ == "__main__"):
    main()