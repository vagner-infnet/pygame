"""
exibindo uma tela vazia.
a tela abre.
escutamos o click em algumas teclas
"""
import pygame

def exibe_janela_e_escuta_click_em_varios_botoes():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    largura_altura_da_JANELA = (largura_da_JANELA, altura_da_JANELA)
    pygame.display.set_mode(largura_altura_da_JANELA)
    pygame.display.set_caption("Pressione a setas esquerda, direita e letra A.")
    pygame.display.init()

    continuar_no_loop_while = True
    contador = 0
    ####################################################
    while continuar_no_loop_while:

        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                continuar_no_loop_while = False
                continue  # abandono o loop while
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pygame.display.set_caption("seta para direita pressionada")       
                if event.key == pygame.K_LEFT:
                    pygame.display.set_caption("seta para esquerda pressionada")   
                if event.key == pygame.K_a:
                    pygame.display.set_caption("letra A pressionada")        
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_escuta_click_em_varios_botoes()
