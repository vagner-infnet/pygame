"""
exibindo uma tela vazia.
a tela abre.
não fazemos nada.
a tela fecha automatiamente.
"""
import pygame

def exibe_janela_vazia_e_faz_nada():

    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)

    # display significa tela. Precisamos configurar o modo de exibição da tela > suas dimensões > sua altura e largura
    pygame.display.set_mode(tupla_largura_altura)
    # init significa iniciar > iniciar o programa, exibindo sua janela
    pygame.display.init()
    ... # não fazemos nada
    # quit significa sair > sair do programa que está com a janela aberta
    #pygame.display.quit()

exibe_janela_vazia_e_faz_nada()