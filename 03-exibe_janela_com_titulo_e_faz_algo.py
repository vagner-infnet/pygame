"""
exibindo uma tela vazia.
a tela abre.
fazemos alguma coisa.
a tela fecha automatiamente.
"""
import pygame

def exibe_janela_com_titulo_e_faz_algo():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)

    pygame.display.set_mode(tupla_largura_altura)
    # O título da janela poderia ser configurado ANTES de iniciar o programa
    pygame.display.set_caption("Oi, mundo - ANTES DE ABRIR A JANELA!")
    pygame.display.init()
    # O título da janela poderia ser configurado DEPOIS de iniciar o programa
    pygame.display.set_caption("Oi, mundo - DEPOIS DE ABRIR A JANELA!")
    # depois de iniciar, faremos algo:
    ####################################################
    continuar_no_programa = True
    contador = 0
    while continuar_no_programa:
        print(f"estou no programa. contador igual a {contador}")
        contador = contador + 1
        if contador == 1000:
            continuar_no_programa = False
    ####################################################
    # O título da janela poderia ser configurado depois de fazer algo
    pygame.display.set_caption("Oi, mundo - DEPOIS DE FAZER ALGO")
    ####################################################
    continuar_no_programa = True
    contador = 0
    while continuar_no_programa:
        print(f"estou no programa. contador igual a {contador}")
        contador = contador + 1
        if contador == 1000:
            continuar_no_programa = False
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit()

exibe_janela_com_titulo_e_faz_algo()
