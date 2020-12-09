"""
exibindo uma tela vazia.
a tela abre.
fazemos alguma coisa.
a tela fecha automatiamente.
"""
import pygame

def exibe_janela_vazia_e_faz_algo():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)

    pygame.display.set_mode(tupla_largura_altura)
    pygame.display.init()
    # depois de iniciar, faremos algo:
    ####################################################
    continuar_no_programa = True
    contador = 0
    while continuar_no_programa:
        print(f"estou no programa. contador igual a {contador}")
        contador = contador + 1
        if contador == 1000:
            continuar_no_programa = False
            #próximo while não será executado
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit()

exibe_janela_vazia_e_faz_algo()
