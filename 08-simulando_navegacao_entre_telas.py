"""
exibindo uma tela vazia.
a tela abre.
escutamos as setas esquerda, direita e espaço e simulamos navegação entre telas
"""
import pygame

def exibe_janela_e_simula_navegacao_entre_telas():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    largura_altura_da_JANELA = (largura_da_JANELA, altura_da_JANELA)
    pygame.display.set_mode(largura_altura_da_JANELA)
    pygame.display.set_caption("Simulando navegação entre telas")
    pygame.display.init()

    continuar_no_loop_while = True
    tela_atual = "tela_principal"
    ####################################################
    while continuar_no_loop_while:

        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                continuar_no_loop_while = False
                continue  # sair deste loop for, sem executar as demais linhas dentro de while
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("seta para direita pressionada")   
                    if tela_atual == "tela_1":
                        tela_atual = "tela_2"
                    elif tela_atual == "tela_2":
                        tela_atual = "tela_3"
                    elif tela_atual == "tela_3":
                        tela_atual = "tela_1"
                    elif tela_atual == "tela_principal":
                        tela_atual = "tela_1"
                    pygame.display.set_caption(f"TELA ATUAL: {tela_atual}")
                if event.key == pygame.K_LEFT:
                    print("seta para esquerda pressionada")   
                    if tela_atual == "tela_3":
                        tela_atual = "tela_2"
                    elif tela_atual == "tela_2":
                        tela_atual = "tela_1"
                    elif tela_atual == "tela_1":
                        tela_atual = "tela_3" 
                    elif tela_atual == "tela_principal":
                        tela_atual = "tela_3"     
                    pygame.display.set_caption(f"TELA ATUAL: {tela_atual}")                
                if event.key == pygame.K_SPACE:
                    print("tecla espaço pressionada")   
                    tela_atual = "tela_principal"      
                    pygame.display.set_caption(f"TELA ATUAL: {tela_atual}")                 
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_simula_navegacao_entre_telas()
