from time import sleep
from Dados import atacaInimigo


def digitar(texto):
    for i in texto:
        print(i, end='', flush=True)
        sleep(0.05)



def Historia():
    global personagem
    print('-*'*10)
    print('TOP RPG FODA')
    print('-*'*10)
    sleep(1)
    digitar('Seja bem vindo(a) a cidade de Genubia')
    sleep(1)
    aldeao = input('\nDeseja falar com um aldeão da cidade? [Sim/Nao]\n').upper()
    if aldeao == 'SIM':
        sleep(1)
        digitar('ALDEÃO:\nOlá nobre cavaleiro(a)\nA cidade Genubia está sofrendo por varias perdas na guerra, ' \
        'estamos em uma batalha intensa seguida por meses de cerco, por conta disso estamos sem alimento na aldeia.\n')
        personagem = input("Qual é seu nome, cavaleiro(a)?\n")
        sleep(1)
        print('POWWWWWW')
        sleep(1)
        digitar('ALDEÕES GRITANDO:\nOh não, estamos sendo atacados!!!!!\n')
        sleep(1)
        digitar(f'{personagem}, precisamos de um cavaleiro valente para evitar o exterminio total de Genubia\n')
        sleep(1)
        jogar = input('Você é valente o suficiente para salvar uma civilização *INTEIRA* sozinho? [SIM/NÃO SOU VALENTE O SUFICIENTE]' ).upper()
        sleep(1)
        if jogar == 'SIM':
            atacaInimigo()
            print('')
        else:
            digitar('ALDEÃO:\n' \
            'Você irá mesmo nos deixar morrer? Você não tem aurea nenhuma. -100 de aurea\n')
      

# Historia()


