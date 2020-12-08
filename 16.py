import pygame

def exibe_janela_e_substitui_forma_azul_por_texto_no_painel():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    largura_altura_da_JANELA = (largura_da_JANELA, altura_da_JANELA)

    JANELA = pygame.display.set_mode(largura_altura_da_JANELA)  # ATENÇÃO >>> PRECISAMOS GRAVAR A REFERÊNCIA DA JANELA PRINCIPAL
    pygame.display.init()
    pygame.font.init()
    font_family = 'Comic Sans MS' # None
    font_size = 30
    myfont_1 = pygame.font.SysFont(font_family, font_size)
    ####################################################
    x_inicial_do_PAINEL_1 = 0
    largura_do_PAINEL_1 = 100
    y_inicial_do_PAINEL_1 = 0
    altura_do_PAINEL_1 = 100       
    largura_altura_do_PAINEL_1 = (largura_do_PAINEL_1, altura_do_PAINEL_1)
    PAINEL_1 = pygame.surface.Surface(largura_altura_do_PAINEL_1)
    ####################################################
    #configurando superfície
    def texto_1():
        print("escrevendo texto_1")
        x_inicial_do_TEXTO_1 = 0
        #largura_do_TEXTO_1 = 0 + contador
        y_inicial_do_TEXTO_1 = 0
        #altura_do_TEXTO_1 = 0 + contador  
        #if altura_do_TEXTO_1 > 50:  
            #altura_do_TEXTO_1 = 50    
        #largura_altura_do_TEXTO_1 = (largura_do_TEXTO_1, altura_do_TEXTO_1)
        #TEXTO_1 = pygame.surface.Surface(largura_altura_do_TEXTO_1)
        cor_do_TEXTO_1 = (0, 0, 255)  # azul
        text = myfont_1.render("TEXTO_1", True, cor_do_TEXTO_1)
        #pygame.draw.rect(PAINEL_1, cor_do_TEXTO_1, (x_inicial_do_TEXTO_1, y_inicial_do_TEXTO_1, largura_do_TEXTO_1, altura_do_TEXTO_1))
        #AGORA QUE DESENHEI UM RECT NO PAINEL, DEVO PEDIR À JANELA PARA RECEBER O PAINEL REDESENHADO
        PAINEL_1.blit(text, (x_inicial_do_TEXTO_1, y_inicial_do_TEXTO_1))
        #JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  # inserindo o painel na janela
    def forma_2(contador):
        print("desenhando forma_2")
        x_inicial_da_FORMA_2 = 0
        largura_da_FORMA_2 = 0 + contador
        y_inicial_da_FORMA_2 = 50
        altura_da_FORMA_2 = 0 + contador       
        #largura_altura_da_FORMA_2 = (largura_da_FORMA_2, altura_da_FORMA_2)
        #FORMA_2 = pygame.surface.Surface(largura_altura_da_FORMA_2)
        cor_da_FORMA_2 = (255, 0, 0)  # vermelho
        pygame.draw.rect(PAINEL_1, cor_da_FORMA_2, (x_inicial_da_FORMA_2, y_inicial_da_FORMA_2, largura_da_FORMA_2, altura_da_FORMA_2))
        #AGORA QUE DESENHEI UM RECT NO PAINEL, DEVO PEDIR À JANELA PARA RECEBER O PAINEL REDESENHADO
        #JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  # inserindo o painel na janela
    def painel_1():
        print("desenhando painel_1")
        cor_do_PAINEL_1 = (255, 255, 255)  # branco
        PAINEL_1.fill(cor_do_PAINEL_1)  # pintando o painel com a cor desejada
        #JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  # inserindo o painel na janela
    ####################################################
    continuar_no_loop_while = True
    contador = 0
    ####################################################   
    painel_1()
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
                    texto_1()
                if event.key == pygame.K_LEFT:
                    print("seta para esquerda pressionada")  
                    contador = contador + 1
                    forma_2(contador)
                if event.key == pygame.K_SPACE:
                    print("letra A pressionada") 
                    contador = 0
                    painel_1()
        #contador = contador + 1
        #painel_1(contador)
        #texto_1(contador)
        #forma_2(contador)
        JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  # inserindo o painel na janela
        # Fazendo a janela exibir os componentes com seus valores atualizados
        pygame.display.update()
        pygame.time.Clock().tick(60) # nº de atualizações por segundo
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_substitui_forma_azul_por_texto_no_painel()
