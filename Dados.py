from random import randint
from Personagens import Personagem


def CriaJogador():
    global jogador
    from Historias import Historia
    nomeJogador = Historia()
    jogador = Personagem(nomeJogador, 50, 10, 10, 1)
    return jogador
    

def criaInimigo():
    inimigo = Personagem('Inimigo', randint(jogador.vida-5,jogador.vida+5), randint(jogador.ataque-5,jogador.ataque+5), randint(jogador.defesa-5,jogador.defesa+5), jogador.lvl)
    return inimigo

inimigo = criaInimigo()

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
print(inimigo)

