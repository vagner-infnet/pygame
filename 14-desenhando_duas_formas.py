"""
exibindo uma tela vazia.
a tela abre.
redesenhado 2 formas numa superfície
a tela fecha automatiamente.
"""
import pygame

def exibe_janela_e_desenha_2formas():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)
    #JANELA > PRECISAMOS GRAVAR UMA REFERÊNCIA DA JANELA DO PROGRAMA
    JANELA = pygame.display.set_mode(tupla_largura_altura)
    pygame.display.set_caption("Desenhando duas formas")
    pygame.display.init()
    ####################################################
    largura_do_PAINEL_1 = largura_da_JANELA/2
    altura_do_PAINEL_1 = altura_da_JANELA/2       
    largura_altura_do_PAINEL_1 = (largura_do_PAINEL_1, altura_do_PAINEL_1)
    PAINEL_1 = pygame.surface.Surface(largura_altura_do_PAINEL_1)

    y_inicial_do_PAINEL_1 = 0
    x_inicial_do_PAINEL_1 = 0
    def reseta_painel_1():
        print("desenhando painel_1")
        cor_do_PAINEL_1 = (255, 255, 255)  # branco
        PAINEL_1.fill(cor_do_PAINEL_1)  # pintando o painel com a cor desejada
    reseta_painel_1()
    ####################################################
    #configurando superfície
    def forma_1(contador):
        print("desenhando forma_1")
        x_inicial_da_FORMA_1 = 0
        y_inicial_da_FORMA_1 = 0
        largura_da_FORMA_1 = contador        
        altura_da_FORMA_1 = contador  
        if altura_da_FORMA_1 > altura_do_PAINEL_1/2:  
            altura_da_FORMA_1 = altura_do_PAINEL_1/2    
        cor_da_FORMA_1 = (0, 0, 255)  # azul
        pygame.draw.rect(PAINEL_1, cor_da_FORMA_1, (x_inicial_da_FORMA_1, y_inicial_da_FORMA_1, largura_da_FORMA_1, altura_da_FORMA_1))
    def forma_2(contador):
        print("desenhando forma_2")
        x_inicial_da_FORMA_2 = 0
        y_inicial_da_FORMA_2 = altura_do_PAINEL_1/2
        largura_da_FORMA_2 = contador
        altura_da_FORMA_2 = contador       
        cor_da_FORMA_2 = (255, 0, 0)  # vermelho
        pygame.draw.rect(PAINEL_1, cor_da_FORMA_2, (x_inicial_da_FORMA_2, y_inicial_da_FORMA_2, largura_da_FORMA_2, altura_da_FORMA_2))
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
        #painel_1(contador)
        reseta_painel_1()
        forma_1(contador)
        forma_2(contador)
        # Fazendo a janela exibir os componentes com seus valores atualizados
        JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  # inserindo o painel na janela
        pygame.display.update()
        pygame.time.Clock().tick(60) # nº de atualizações por segundo
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_desenha_2formas()
