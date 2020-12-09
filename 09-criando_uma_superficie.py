"""
Faremos um painel(superfície) começar com tamanho 0 
e crescer até o tamanho da janela
"""
import pygame

def exibe_janela_e_cria_superficie():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)
    #JANELA > PRECISAMOS GRAVAR UMA REFERÊNCIA DA JANELA DO PROGRAMA
    JANELA = pygame.display.set_mode(tupla_largura_altura)
    pygame.display.set_caption("Criando uma painel")
    pygame.display.init()
    ####################################################
    def reseta_JANELA():
        #pintamos a janela, para apagar seu conteúdo
        cor_da_JANELA = (0, 0, 0)  # preto
        JANELA.fill(cor_da_JANELA)
    #configurando superfície
    def set_painel_1(contador):

        print("desenhando painel_1")

        largura_do_PAINEL_1 = contador
        altura_do_PAINEL_1 = contador
        largura_altura_do_PAINEL_1 = (largura_do_PAINEL_1, altura_do_PAINEL_1)
        # criando o painel com as dimensões desejadas
        # depois poderemos desenhar formas ou inserir textos neste painel
        PAINEL_1 = pygame.surface.Surface(largura_altura_do_PAINEL_1)       
        # pintando o painel com a cor desejada
        cor_do_PAINEL_1 = (255, 255, 255)  # branco 
        PAINEL_1.fill(cor_do_PAINEL_1)  
        
        x_inicial_do_PAINEL_1 = 0
        y_inicial_do_PAINEL_1 = 0
        # inserindo(blit) o painel na janela
        JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  
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
        #contador == 400 > o painel tomou a área total da janela
        if contador > 400:
            #faremos o painel começar do zero, novamente
            contador = 0
        reseta_JANELA()
        set_painel_1(contador)
        # Fazendo a janela exibir os componentes com seus valores atualizados
        pygame.display.update()
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_cria_superficie()
