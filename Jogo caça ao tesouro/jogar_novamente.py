import pygame as pg
import jogo
import interface

# Função para a tela de jogar novamente
def tela_jogar_novamente():
    largura, altura = 800, 600
    tela = pg.display.set_mode((largura, altura))
    pg.display.set_caption("Jogar Novamente")

    verde = (0, 255, 0)
    branco = (255, 255, 255)

    fundo = pg.image.load("fundo.jpg")
    fundo = pg.transform.scale(fundo, (largura, altura))

    tela.blit(fundo, (0, 0))

    # Criar botão
    botao_jogar_novamente, botao_sair = interface.criar_botoes(largura, altura)

    jogando = True
    while jogando:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            
            if evento.type == pg.MOUSEBUTTONDOWN:
                if botao_jogar_novamente.collidepoint(evento.pos):
                    jogo.jogo()  

                if botao_sair.collidepoint(evento.pos):
                    pg.quit()
                    quit()
                    
        interface.desenhar_botoes(botao_jogar_novamente, botao_sair, tela, verde, branco, "Jogar novamente", "Sair")
        pg.display.update()
        
    pg.quit()


