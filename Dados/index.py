from random import randint
from Personagens.index import Personagem
from Historia.index import Historia


nomeJogador = Historia()
jogador = Personagem(nomeJogador, 50, 10, 10, 1)
inimigo = Personagem('Inimigo Fudido', randint(45,55), randint(5,15), randint(5,15), 1)



def ataqueJogador():
    rolarAtaqueJogador = input('Deseja rolar o dado de ataque? [Sim/Não]').upper()
    if rolarAtaqueJogador == 'SIM':
        dado = randint(0,5)
        ataque = jogador.ataque + dado
        return ataque
    else:
        print('Foje bot noob')

def atacaInimigo():
    ataqueRodada1 = ataqueJogador()
    dado = ataqueRodada1 - jogador.ataque
    print(f'Valor do dado: {dado} | Valor do ataque: {jogador.ataque} | Resultado total do ataque: {ataqueRodada1}\nDefesa do inimigo: {inimigo.defesa}\nVida do inimigo antes do ataque: {inimigo.vida}')
    if ataqueRodada1 > inimigo.defesa:
        dano = ataqueRodada1 - inimigo.defesa
        inimigo.vida -= dano
        print(f'Defesa do inimigo: {inimigo.defesa}\nVida pós ataque: {inimigo.vida}')
    else:
        print(f'Inimigo não atacado, defesa maior que ataque\nDefesa: {inimigo.defesa}')

# ataqueJogador()
atacaInimigo()


print('TOP ALTERAÇÕES')