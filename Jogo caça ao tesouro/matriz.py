import random as rd
import pygame as pg
def adicionar_item(item, matriz):
    pos_vazia = True
    while pos_vazia:
        linha_aleatoria = rd.randint(0, len(matriz)-1)
        coluna_aleatoria = rd.randint(0, len(matriz)-1)

        if matriz[linha_aleatoria][coluna_aleatoria] is None:
            matriz[linha_aleatoria][coluna_aleatoria] = item
            pos_vazia = False

def desenhar_no_tabuleiro(tela, matriz_a, a, b, um, dois, tres, coord_x, coord_y):

    if matriz_a[a][b] == 1:
        
        tela.blit(um, (coord_x * 100 + 100, coord_y * 100 + 100))
    
    if matriz_a[a][b] == 2:
        
        tela.blit(dois, (coord_x * 100 + 100, coord_y * 100 + 100))

    if matriz_a[a][b] == 3:
        
        tela.blit(tres, (coord_x * 100 + 100, coord_y * 100 + 100))
