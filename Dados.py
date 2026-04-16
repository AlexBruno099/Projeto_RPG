from time import sleep
from random import randint
from Personagens import Personagem
from Historias import Historia
import os
from Hud import hudBatalha, hudDefesa, hudErraAtaque, hudMorreu, hudNaoAjudou

# Funçaõ pra limpar os dados da tela
def LimpaTela():
    os.system('cls')

# Função pra criar os inimigos, com base nos dados do jogador
def criaInimigo(jogador_atual):
    inimigo = Personagem('Inimigo Orc', randint(jogador_atual.vida -10, jogador_atual.vida - 9), randint(jogador_atual.ataque -1, jogador_atual.ataque + 1), randint(jogador_atual.defesa - 5, jogador_atual.defesa + 5), jogador_atual.lvl)
    return inimigo


# Função onde o inimigo ataca o jogador
def InimigoAtaca(inimigo_atual, jogador_atual):
        sleep(1)
        LimpaTela()
        sleep(1)
        print(f'O inimigo {inimigo.nome} vai te atacar!')
        sleep(1)
        dado = randint(0,5)
        ataque = inimigo_atual.ataque + dado
        dadoDefesa = randint(0,5)
        defesa = jogador.defesa + dadoDefesa
        if ataque > defesa:
            hudBatalha()
            dano = ataque - defesa
            jogador_atual.vida -= dano
            print(f'\n- Valor do dado do ataque: {dado}\n- Valor do ataque do inimigo: {inimigo_atual.ataque}\n- Resultado total do ataque: {ataque}\n- Valor do dado da defesa: {dadoDefesa}\n- Defesa do jogador: {jogador_atual.defesa}\n- Defesa total: {defesa}\n- Vida do jogador antes do ataque: {jogador_atual.vida+dano}\n- Vida pós ataque: {jogador_atual.vida}')
        else:
            hudDefesa()
            print(f'Jogador não atacado, defesa maior que ataque\n- Defesa do jogador: {jogador_atual.defesa}\n- Ataque inicial: {inimigo_atual.ataque}\n- Dado: {dado}\n- Ataque total: {ataque}')

# Função pra questionar se o jogador deseja atacar
def ataqueJogador(jogador_atual):
    sleep(1)
    rolarAtaqueJogador = input('\nDeseja rolar o dado de ataque? [Sim/Não]\n').upper()
    LimpaTela()
    if rolarAtaqueJogador == 'SIM':
        dado = randint(0,5)
        ataque = jogador_atual.ataque + dado
        return ataque
    else:
        print('\nFoje bot noob')

# Função onde o jogador ataca o inimigo
def atacaInimigo(jogador_atual, inimigo_atual):
    ataqueRodada1 = ataqueJogador(jogador_atual)
    dado = ataqueRodada1 - jogador_atual.ataque
    dadoDefesa = randint(0,5)
    defesa = inimigo_atual.defesa + dadoDefesa
    if ataqueRodada1 > defesa:
        hudBatalha()
        sleep(0.5)
        dano = ataqueRodada1 - inimigo_atual.defesa
        inimigo_atual.vida -= dano
        print(f'Defesa do inimigo: {inimigo_atual.defesa}\nVida pós ataque: {inimigo_atual.vida}')
        input('Pressione ENTER para continuar...')
    else:
        hudErraAtaque()
        print(f'Inimigo não atacado, defesa maior que ataque\nDefesa: {inimigo_atual.defesa}\nAtaque do jogador: {jogador_atual.ataque + dado}')
        input('Pressione ENTER paraontinuar...')


    def validaVidaInimigo(inimigo_atual):
        if inimigo_atual.vida <= 0:
            count = 0
            print(f'O inimigo {inimigo_atual.nome} morreu!')
            count += 1
            return count

    def sobeNivel(jogador_atual, inimigo_atual):
        count = validaVidaInimigo(inimigo_atual)
        if count == 3:
            jogador_atual.lvl += 1
            jogador_atual.vida_Max += 10
            jogador_atual.vida = jogador_atual.vida_Max
            jogador_atual.defesa += 2
            jogador_atual.ataque += 2
            print(f'Parabéns, você avançou para o nível {jogador_atual.lvl}\nVocê ganhou também atributos novos\n- Vida: {jogador_atual.vida}\n- Ataque: {jogador_atual.ataque}\n- Defesa: {jogador_atual.defesa}')
            return jogador_atual.lvl

    def seita(jogador_atual):
        if jogador_atual.lvl == 5:
            print('SEITA')
        
    sobeNivel(jogador_atual, inimigo_atual)
    seita(jogador_atual)


nome, aceitou_jogar = Historia()

if aceitou_jogar:
    jogador = Personagem(nome, 50, 50, 10, 1)
    inimigo = criaInimigo(jogador)
    
    while jogador.lvl < 10:
        if inimigo.vida <= 0:
            inimigo = criaInimigo(jogador)
    
        print(f"\nUm {inimigo.nome} bloqueia o seu caminho!")

        while inimigo.vida > 0 and jogador.vida > 0:
            atacaInimigo(jogador, inimigo)

            if inimigo.vida <= 0:
                print(f"{inimigo.nome} foi derrotado!")
                jogador.vida += 15
                if jogador.vida > jogador.vida_Max:
                    jogador.vida = jogador.vida_Max
                break

            InimigoAtaca(inimigo, jogador)

            if jogador.vida <= 0:
                hudMorreu()
                break

else:
    hudNaoAjudou()
