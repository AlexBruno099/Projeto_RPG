from time import sleep

def digitar(texto):
    for i in texto:
        print(i, end='', flush=True)
        sleep(0.02) 

def Historia():
    print('-*' * 10)
    print('TOP RPG FODA')
    print('-*' * 10)
    sleep(1)
    
    digitar('Seja bem vindo(a) a cidade de Genubia\n')
    sleep(1)
    digitar('Você vai em direção a uma multidão na sua frente...\n\r\n\r')
    
    sleep(1)
    digitar('ALDEÃO:\nOlá nobre cavaleiro(a)\nA cidade Genubia está sofrendo por varias perdas na guerra, estamos em uma batalha intensa seguida por meses de cerco, por conta disso estamos sem alimento na aldeia.\n')
    
    nome_jogador = input("\nQual é seu nome, cavaleiro(a)?\n").strip()
    sleep(1)
    
    print('\nPOWWWWWW')
    sleep(1)
    digitar('ALDEÕES GRITANDO:\nOh não, estamos sendo atacados!!!!!\n')
    sleep(1)
    
    digitar(f'\n{nome_jogador}, precisamos de um cavaleiro valente para evitar o exterminio total de Genubia\n')
    sleep(1)
    
    jogar = input('Você é valente o suficiente para salvar uma civilização *INTEIRA* sozinho? [SIM/NÃO SOU VALENTE O SUFICIENTE]\n').strip().upper()
    sleep(1)
    
    if jogar != 'SIM':
        digitar('ALDEÃO:\nVocê irá mesmo nos deixar morrer? Você não tem aurea nenhuma. -100 de aurea\n')
            
    return nome_jogador, jogar == 'SIM'