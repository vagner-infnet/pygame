"""
exibindo uma tela vazia.
a tela abre.
escutamos o click no botão SAIR da janela
a tela fecha automatiamente.
"""
import pygame

def exibe_janela_e_escuta_click_no_botao_sair_e_outros_botoes():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)

    # display significa tela. Precisamos configurar o modo de exibição da tela > suas dimensões > sua altura e largura
    pygame.display.set_mode(tupla_largura_altura)
    # init significa iniciar > iniciar o programa, exibindo sua janela
    pygame.display.init()

    print(f"pygame.KEYDOWN: {pygame.KEYDOWN}")  # KEYDOWN == TECLA PRESSIONADA > 768
    print(f"pygame.KEYUP: {pygame.KEYUP}")  # KEYUP == TECLA LIBERADA > 769
    print(f"pygame.QUIT: {pygame.QUIT}")  # QUIT == X DA JANELA, PARA SAIR > 256

    continuar_no_loop_while = True
    contador = 0
    ####################################################
    while continuar_no_loop_while:

        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                continuar_no_loop_while = False
                #continue  # sair deste loop for
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("seta para direita pressionada")       
                if event.key == pygame.K_LEFT:
                    print("seta para esquerda pressionada")   
                if event.key == pygame.K_a:
                    print("letra A pressionada")        
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_escuta_click_no_botao_sair_e_outros_botoes()
