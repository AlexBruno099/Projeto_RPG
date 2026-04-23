from time import sleep
from random import randint
from Personagens import Personagem
from Historias import Historia
import os
from Hud import hudBatalha, hudDefesa, hudErraAtaque, hudMorreu, hudNaoAjudou, hudCinemaAbsoluto

# Função pra limpar os dados da tela
def LimpaTela():
    os.system('cls')

#Função para mostrar a barra de vida no hud de batalha
def barra_vida(nome, vida, vida_max):
    tamanho_barra = 20
    vida_ratio = vida / vida_max
    preenchido = int(tamanho_barra * vida_ratio)
    
    barra = '█' * preenchido + '-' * (tamanho_barra - preenchido)
    
    print(f'{nome}: [{barra}] {vida}/{vida_max}')


#Função de status para batalha
def hudStatus(jogador, inimigo):
    print("\n" + "="*50)
    print("⚔️  BATALHA ⚔️")
    print("="*50)
    
    barra_vida(jogador.nome, jogador.vida, jogador.vida_Max)
    barra_vida(inimigo.nome, inimigo.vida, inimigo.vida_Max)
    
    print("="*50 + "\n")

# Função pra criar os inimigos, com base nos dados do jogador
def criaInimigo(jogador_atual):
    inimigo = Personagem('Inimigo Orc', randint(jogador_atual.vida -5, jogador_atual.vida + 5), randint(jogador_atual.ataque -5, jogador_atual.ataque + 5), randint(jogador_atual.defesa - 5, jogador_atual.defesa + 5), jogador_atual.lvl)
    return inimigo


# Função onde o inimigo ataca o jogador
def InimigoAtaca(inimigo_atual, jogador_atual):
        sleep(1)
        sleep(1)
        LimpaTela()
        print(f'O inimigo {inimigo_atual.nome} vai te atacar!')
        dado = randint(0,5)
        ataque = inimigo_atual.ataque + dado
        dadoDefesa = randint(0,5)
        defesa = jogador.defesa + dadoDefesa
        if ataque > defesa:
            dano = ataque - defesa
            jogador_atual.vida -= dano
            hudStatus(jogador_atual, inimigo_atual)
            hudBatalha()
        else:
            hudStatus(jogador_atual, inimigo_atual)
            hudDefesa()
            print(f'Jogador não atacado, defesa maior que ataque')

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
        dano = ataqueRodada1 - inimigo_atual.defesa
        inimigo_atual.vida -= dano
        hudStatus(jogador_atual, inimigo_atual)
        hudBatalha()
        sleep(0.5)
        input('Pressione ENTER para continuar...')
    else:
        hudStatus(jogador_atual, inimigo_atual)
        hudErraAtaque()
        print(f'Inimigo não atacado, defesa maior que ataque.')
        input('Pressione ENTER para continuar...')


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
            LimpaTela()
            print(f'✨Parabéns {jogador_atual.nome}✨\nVocê avançou para o nível {jogador_atual.lvl}\nVocê ganhou também atributos novos\n- Vida: {jogador_atual.vida}\n- Ataque: {jogador_atual.ataque}\n- Defesa: {jogador_atual.defesa}')
            sleep(3.5)
            return jogador_atual.lvl

        
    sobeNivel(jogador_atual, inimigo_atual)


nome, aceitou_jogar = Historia()

if aceitou_jogar:
    jogador = Personagem(nome, 50, 10, 10, 1)
    inimigo = criaInimigo(jogador)
    count = 1
    while jogador.lvl < 20:
        if inimigo.vida <= 0:
            inimigo = criaInimigo(jogador)
            count += 1
            print(f'O inimigo {count} está vindo!')
    
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
    LimpaTela()
    print('ALDEÕES:')
    print('Obrigado(a), você salvou nossa vida.\nAgora lhe entregamos nossa vila para você comandar e nos guiar para proxima batalha.')           
    hudCinemaAbsoluto()
else:
    hudNaoAjudou()
