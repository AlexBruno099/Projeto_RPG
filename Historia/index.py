from time import sleep


def Historia():
    global personagem
    print('-*'*10)
    print('TOP RPG FODA')
    print('-*'*10)
    sleep(1)
    print('Seja bem vindo(a) a cidade de Genubia')
    sleep(1)
    aldeao = input('Deseja falar com um aldeão da cidade? [Sim/Nao]\n').upper()
    if aldeao == 'SIM':
        sleep(1)
        print('ALDEÃO:\nOlá nobre cavaleiro(a)\nA cidade Genubia está sofrendo por varias perdas na guerra, ' \
        'estamos em uma batalha intensa seguida por meses de cerco, por conta disso estamos sem alimento na aldeia.')
        personagem = input("Qual é seu nome, cavaleiro(a)?")
        sleep(1)
        print('POWWWWWW')
        sleep(1)
        print('ALDEÕES GRITANDO:\nOh não, estamos sendo atacados!!!!!')
        sleep(1)
        print(f'{personagem}, precisamos de um cavaleiro valente para evitar o exterminio total de Genubia')
        sleep(1)
        jogar = input('Você é valente o suficiente para salvar uma civilização *INTEIRA* sozinho? [SIM/NÃO SOU VALENTE O SUFICIENTE]' ).upper()
        sleep(1)
        if jogar == 'SIM':
            jogar()
            print('')
        else:
            print('ALDEÃO:\n' \
            'Você irá mesmo nos deixar morrer? Você não tem aurea nenhuma. -100 de aurea')
      