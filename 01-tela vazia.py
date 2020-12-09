"""
exibindo uma tela vazia.
a tela abre.
não fazemos nada.
a tela fecha automatiamente.
"""
import pygame

def exibe_janela_vazia_e_faz_nada():

    #configurando as dimensões da janela
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)

    # display significa tela/janela. 
    # set_mode() recebe as dimensões em forma de tupla
    pygame.display.set_mode(tupla_largura_altura)
    
    # init significa iniciar > 
    # iniciamos o programa, exibindo sua janela
    pygame.display.init()

    ... # por enquanto não fazemos nada

    # quit significa sair > 
    # sairemos automaticamente do programa
    #pygame.display.quit()

exibe_janela_vazia_e_faz_nada()