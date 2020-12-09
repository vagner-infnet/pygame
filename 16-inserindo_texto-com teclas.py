"""
exibindo uma tela vazia.
a tela abre.
redesenhado 2 textos numa superfície com direta, esquerda e espaço
a tela fecha automatiamente.
"""
import pygame

def exibe_janela_e_desenha_2formas_com_teclas():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)
    #JANELA > PRECISAMOS GRAVAR UMA REFERÊNCIA DA JANELA DO PROGRAMA
    JANELA = pygame.display.set_mode(tupla_largura_altura)
    pygame.display.set_caption("Desenhando duas formas")
    pygame.display.init()
    ####################################################
    pygame.font.init()
    font_family_1 = 'Comic Sans MS'
    font_family_2 = 'None'
    font_size_1 = 30
    font_size_2 = 15
    myfont_1 = pygame.font.SysFont(font_family_1, font_size_1)
    myfont_2 = pygame.font.SysFont(font_family_2, font_size_2)
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
        print("escrevendo texto_1")
        x_inicial_do_TEXTO_1 = 0
        y_inicial_do_TEXTO_1 = 0
        cor_do_TEXTO_1 = (0, 0, 255)  # azul
        text = myfont_1.render("TEXTO_1", True, cor_do_TEXTO_1)
        PAINEL_1.blit(text, (x_inicial_do_TEXTO_1, y_inicial_do_TEXTO_1))
    def forma_2(contador):
        print("escrevendo texto_2")
        x_inicial_do_TEXTO_2 = 0
        y_inicial_do_TEXTO_2 = altura_do_PAINEL_1/2
        cor_do_TEXTO_2 = (255, 0, 0)  # vermelho
        text = myfont_2.render("TEXTO_2", True, cor_do_TEXTO_2)
        PAINEL_1.blit(text, (x_inicial_do_TEXTO_2, y_inicial_do_TEXTO_2))
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("seta para direita pressionada")   
                    contador = contador + 1  
                    #reseta_painel_1()
                    forma_1(contador)
                if event.key == pygame.K_LEFT:
                    print("seta para esquerda pressionada")  
                    contador = contador + 1
                    #reseta_painel_1()
                    forma_2(contador)
                if event.key == pygame.K_SPACE:
                    print("tecla espaço pressionada") 
                    contador = 0
                    reseta_painel_1()
        contador = contador + 1
        #painel_1(contador)
        #reseta_painel_1()
        #forma_1(contador)
        #forma_2(contador)
        # Fazendo a janela exibir os componentes com seus valores atualizados
        JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  # inserindo o painel na janela
        pygame.display.update()
        pygame.time.Clock().tick(60) # nº de atualizações por segundo
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_desenha_2formas_com_teclas()
