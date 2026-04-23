from time import sleep
from Hud import hudCastelo, hudInimigoAtacando,hudNaoAjudou
import os

def digitar(texto):
    for i in texto:
        print(i, end='', flush=True)
        sleep(0.0) 

def LimpaTela():
    os.system('cls')

def Historia():
    digitar('Você chegou em uma vila desconhecida....\n\n')
    sleep(1.5)
    hudCastelo()
    sleep(3.5)
    LimpaTela()

    digitar('Seja bem vindo(a) a vila de Genubia\n')
    sleep(1)
    digitar('Você vai em direção a uma multidão na sua frente...\n\r\n\r')
    sleep(1)

    digitar('Você pergunta para um aldeão o motivo do panico da multidão.\n')
    sleep(1)
    digitar('ALDEÃO:\nOlá nobre cavaleiro(a)\nA cidade Genubia está sofrendo por varias perdas na guerra, estamos em uma batalha intensa seguida por meses de cerco, por conta disso estamos sem alimento na aldeia.\n')
    sleep(1)

    nome_jogador = input("\nQual é seu nome, cavaleiro(a)?\n").strip()
    
    sleep(1)
    
    print("""
                                POOOOOOOOWWWW!!!!!   


     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    sleep(2.5)
    LimpaTela()
    print('INIMIGO:')
    digitar('Vamos invadir e matar todos!\n')
    hudInimigoAtacando()
    sleep(1.5)
    print('ALDEÕES GRITANDO:')
    digitar('Oh não, vamos morrer!!!!!\n')
    sleep(1)

    
    digitar(f'\n{nome_jogador}, precisamos de um cavaleiro valente para evitar o exterminio total de Genubia\n')
    sleep(1)
    
    jogar = input('Você é valente o suficiente para salvar uma civilização *INTEIRA* sozinho? [SIM/NAO]\n').strip().upper()
    sleep(2.5)
    LimpaTela()
    
    if jogar != 'SIM':
        digitar('ALDEÃO:\nVocê irá mesmo nos deixar morrer? -100 de aura\n')
            
    return nome_jogador, jogar == 'SIM'