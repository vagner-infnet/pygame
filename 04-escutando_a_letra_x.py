"""
exibindo uma tela vazia.
a tela abre.
escutamos o pressionamento da tecla X
para fechar a tela.
"""
import pygame

def exibe_janela_e_escuta_a_letra_x():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    largura_altura_da_JANELA = (largura_da_JANELA, altura_da_JANELA)
    pygame.display.set_mode(largura_altura_da_JANELA)
    pygame.display.set_caption("Pressione a tecla X para encerrar.")
    pygame.display.init()

    print(f"pygame.KEYDOWN: {pygame.KEYDOWN}")  # KEYDOWN == TECLA PRESSIONADA > 768
    print(f"pygame.KEYUP: {pygame.KEYUP}")  # KEYUP == TECLA LIBERADA > 769
    print(f"pygame.QUIT: {pygame.QUIT}")  # QUIT == X DA JANELA, PARA SAIR > 256
    ####################################################
    continuar_no_loop_while = True
    contador = 0
    ####################################################
    while continuar_no_loop_while:
    
        events = pygame.event.get()  # captura todos os eventos ocorridos neste exato instante: tiro uma foto dos eventos
        
        for event in events:  # percorrendo todos os eventos que estão dentro da 'foto' tirada
            print(f"novo evento detectado nº {contador}")
            contador = contador + 1
            if event.type == pygame.KEYDOWN: #  se o evento foi TECLA PRESSIONADA
                if event.key == pygame.K_x:  # checo se a tecla foi X
                    continuar_no_loop_while = False
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_escuta_a_letra_x()
