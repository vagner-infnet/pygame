"""
exibindo uma tela vazia.
a tela abre.
escutamos o click no botão SAIR da janela
para fechar a tela.
"""
import pygame

def exibe_janela_e_escuta_click_no_botao_sair():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)
    pygame.display.set_mode(tupla_largura_altura)
    pygame.display.set_caption("Pressione o botão sair para encerrar.")
    pygame.display.init()

    continuar_no_loop_while = True
    contador = 0
    ####################################################
    while continuar_no_loop_while:

        events = pygame.event.get()
      
        for event in events:
            print(f"novo evento detectado nº {contador}")
            contador = contador + 1
            if event.type == pygame.QUIT:
                continuar_no_loop_while = False
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_escuta_click_no_botao_sair()
