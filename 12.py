"""
exibindo uma tela vazia.
a tela abre.
redesenhado superfícies num frequência desejada
a tela fecha automatiamente.
"""
import pygame

def exibe_janela_e_atualiza_componentes_numa_frequencia_desejada():
    
    largura_da_JANELA = 200
    altura_da_JANELA = 200
    largura_altura_da_JANELA = (largura_da_JANELA, altura_da_JANELA)

    JANELA = pygame.display.set_mode(largura_altura_da_JANELA)  # ATENÇÃO >>> PRECISAMOS GRAVAR A REFERÊNCIA DA JANELA PRINCIPAL
    pygame.display.init()
    ####################################################
    #configurando superfície
    def painel_1(contador):
        print("desenhando painel_1")
        x_inicial_do_PAINEL_1 = 0
        largura_do_PAINEL_1 = 100 + contador
        y_inicial_do_PAINEL_1 = 0
        altura_do_PAINEL_1 = 100        
        largura_altura_do_PAINEL_1 = (largura_do_PAINEL_1, altura_do_PAINEL_1)
        PAINEL_1 = pygame.surface.Surface(largura_altura_do_PAINEL_1)
        cor_do_PAINEL_1 = (255, 255, 255)  # branco
        PAINEL_1.fill(cor_do_PAINEL_1)  # pintando o painel com a cor desejada
        JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  # inserindo o painel na janela
    def painel_2(contador):
        print("desenhando painel_2")
        x_inicial_do_PAINEL_2 = 0
        largura_do_PAINEL_2 = 100 + contador
        y_inicial_do_PAINEL_2 = 100
        altura_do_PAINEL_2 = 100       
        largura_altura_do_PAINEL_2 = (largura_do_PAINEL_2, altura_do_PAINEL_2)
        PAINEL_2 = pygame.surface.Surface(largura_altura_do_PAINEL_2)
        cor_do_PAINEL_2 = (0, 0, 255)  # azul
        PAINEL_2.fill(cor_do_PAINEL_2)  # pintando o painel com a cor desejada
        JANELA.blit(PAINEL_2, (x_inicial_do_PAINEL_2, y_inicial_do_PAINEL_2))  # inserindo o painel na janela
    ####################################################
    continuar_no_loop_while = True
    contador = 0
    ####################################################   
    while continuar_no_loop_while:
        ######################################
        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                continuar_no_loop_while = False
                #continue  # sair deste loop for
        contador = contador + 1
        painel_1(contador)
        painel_2(contador)
        # Fazendo a janela exibir os componentes com seus valores atualizados
        pygame.display.update()
        pygame.time.Clock().tick(60) # nº de atualizações por segundo
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_atualiza_componentes_numa_frequencia_desejada()
