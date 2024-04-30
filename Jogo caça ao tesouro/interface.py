import pygame as pg

def criar_botoes(largura, altura):
    #Criando um botões no formato retangular e aplicando suas dimensões
    botao_iniciar = pg.Rect(largura // 2 - 100, altura // 2 - 50, 200, 50)

    botao_sair = pg.Rect(largura // 2 - 100, altura // 2 + 50, 200, 50)

    return botao_iniciar, botao_sair

def desenhar_botoes(botao_iniciar, botao_sair, tela, verde, branco,texto_1, texto_2):
    pg.font.init()
    #Usando o draw para desenhar os botões na tela
    pg.draw.rect(tela, verde, botao_iniciar)
    #Aplicando a fonte
    fonte_botao = pg.font.Font(None, 36)
    texto_botao = fonte_botao.render(texto_1, True, branco)
    #Centralizando os botões na tela
    texto_botao_retangulo = texto_botao.get_rect(center=botao_iniciar.center)
    tela.blit(texto_botao, texto_botao_retangulo)
    
    pg.draw.rect(tela, verde, botao_sair)
    texto_botao_sair = fonte_botao.render(texto_2, True, branco)
    texto_botao_sair_retangulo = texto_botao_sair.get_rect(center=botao_sair.center)
    tela.blit(texto_botao_sair, texto_botao_sair_retangulo)
