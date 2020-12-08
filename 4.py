"""
exibindo uma tela vazia.
a tela abre.
checamos palavras-chave importantes 
para saber o que o usuário está fazendo com o teclado e o mouse
a tela fecha automatiamente.
"""
import pygame

def exibe_janela_e_checa_alguns_codigo_de_tecla_e_click():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)

    # display significa tela. Precisamos configurar o modo de exibição da tela > suas dimensões > sua altura e largura
    pygame.display.set_mode(tupla_largura_altura)
    # init significa iniciar > iniciar o programa, exibindo sua janela
    pygame.display.init()
    print(f"pygame.KEYDOWN: {pygame.KEYDOWN}")  # KEYDOWN == TECLA PRESSIONADA > 768
    print(f"pygame.KEYUP: {pygame.KEYUP}")  # KEYUP == TECLA LIBERADA > 769
    print(f"pygame.QUIT: {pygame.QUIT}")  # QUIT == click no X DA JANELA, PARA SAIR > 256
    #pygame.display.quit()

exibe_janela_e_checa_alguns_codigo_de_tecla_e_click()
