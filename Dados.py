from random import randint
from Personagens import Personagem
from Historias import Historia

# def criaInimigo(jogador_atual):
#     inimigo = Personagem('Inimigo Orc', randint(jogador_atual.vida -   5, jogador_atual.vida + 5), randint(jogador_atual.ataque - 5, jogador_atual.ataque + 5), randint(jogador_atual.defesa - 5, jogador_atual.defesa + 5), jogador_atual.lvl)
#     return inimigo

def criaInimigo(jogador_atual):
    inimigo = Personagem('Inimigo Orc', 1, 1, 1, 0)
    return inimigo

def InimigoAtaca(inimigo_atual, jogador_atual):
        dado = randint(0,5)
        ataque = inimigo_atual.ataque + dado
        if ataque > jogador_atual.defesa:
            print(f'\nValor do dado: {dado} | Valor do ataque: {jogador_atual.ataque} | Resultado total do ataque: {ataque}\nDefesa do jogador: {jogador_atual.defesa}\nVida do jogador antes do ataque: {jogador_atual.vida}')
            jogador_atual.vida -= ataque
            print(f'Defesa do jogador: {jogador_atual.defesa}\nVida pós ataque: {jogador_atual.vida}')
        else:
            print(f'Jogador não atacado, defesa maior que ataque\nDefesa: {jogador_atual.defesa},\n ataque inicial: {inimigo_atual.ataque}, Dado: {dado}, Ataque total: {ataque}')


def ataqueJogador(jogador_atual):
    rolarAtaqueJogador = input('\nDeseja rolar o dado de ataque? [Sim/Não]\n').upper()
    if rolarAtaqueJogador == 'SIM':
        dado = randint(0,5)
        ataque = jogador_atual.ataque + dado
        return ataque
    else:
        print('\nFoje bot noob')


def atacaInimigo(jogador_atual, inimigo_atual):
    ataqueRodada1 = ataqueJogador(jogador_atual)
    dado = ataqueRodada1 - jogador_atual.ataque
    print(f'Valor do dado: {dado} | Valor do ataque: {jogador_atual.ataque} | Resultado total do ataque: {ataqueRodada1}\nDefesa do inimigo: {inimigo_atual.defesa}\nVida do inimigo antes do ataque: {inimigo_atual.vida}')
    if ataqueRodada1 > inimigo_atual.defesa:
        dano = ataqueRodada1 - inimigo_atual.defesa
        inimigo_atual.vida -= dano
        print(f'Defesa do inimigo: {inimigo_atual.defesa}\nVida pós ataque: {inimigo_atual.vida}')
    else:
        print(f'Inimigo não atacado, defesa maior que ataque\nDefesa: {inimigo_atual.defesa}')

    def validaVidaInimigo(inimigo_atual):
        if inimigo_atual.vida <= 0:
            count = 0
            print(f'O inimigo {inimigo_atual.nome} morreu!')
            count += 1
            return count

    def sobeNivel(jogador_atual, inimigo_atual):
        count = validaVidaInimigo(inimigo_atual)
        if count == 1:
            jogador_atual.lvl += 4
            print(f'Parabéns, você avançou para o nível {jogador_atual.lvl}')
            return jogador_atual.lvl

    def seita(jogador_atual):
        if jogador_atual.lvl == 5:
            print('SEITA')
        
    sobeNivel(jogador_atual, inimigo_atual)
    seita(jogador_atual)




nome, aceitou_jogar = Historia()

if aceitou_jogar:
    jogador = Personagem(nome, 50, 10, 10, 1)
    inimigo = Personagem('nome', 20,1,10,0)
    
    while jogador.lvl < 10:
        if inimigo.vida <= 0:
            inimigo = criaInimigo(jogador)
    
        print(f"\nUm {inimigo.nome} bloqueia o seu caminho!")

        while inimigo.vida > 0 and jogador.vida > 0:
            atacaInimigo(jogador, inimigo)

            if inimigo.vida <= 0:
                print(f"{inimigo.nome} foi derrotado!")
                break

            InimigoAtaca(inimigo, jogador)

            if jogador.vida <= 0:
                print("Você morreu!")
                break



else:
    print("\nFim de jogo. A cidade caiu em ruínas.")

    print(R"""
           _..--""---.                                
          /           ".                              
          `            l                              
          |'._  ,._ l/"\                              
          |  _J&lt;__/.v._/                              
           \( ,~._,,,,-)                              
            `-\' \`,,j|                               
               \_,____J                               
          .--.__)--(__.--.                            
         /  `-----..--'. j                            
         '.- '`--` `--' \\                            
        //  '`---'`  `-' \\                           
       //   '`----'`.-.-' \\                          
     _//     `--- -'   \' | \________                 
    |  |         ) (      `.__.---- -'\               
     \7          \`-(               74\\\             
     ||       _  /`-(               l|//7__           
     |l    ('  `-)-/_.--.          f''` -.-"|         
     |\     l\_  `-'    .'         |     |  |         
     llJ   _ _)J--._.-('           |     |  l         
     |||( ( '_)_  .l   ". _    ..__I     |  L         
     ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._    
          \ |           ) /.              ``'`-.._``-.
          l l          / / |                      |''|
           " \        / /   "-..__                |  |
           | |       / /          1       ,- t-...J_.'
           | |      / /           |       |  |        
           J  \  /"  (            l       |  |        
           | ().'`-()/            |       |  |        
          _.-"_.____/             l       l.-l        
      _.-"_.+"|                  /        \.  \       
/"\.-"_.-"  | |                 /          \   \      
\_   "      | |                1            | `'|     
  |ll       | |                |            i   |     
  \\\       |-\               \j ..          L,,'. `/ 
 __\\\     ( .-\           .--'    ``--../..'      '-.
   `'''`----`\\\\ .....--'''                          
              \\\\                           -nabis  '
    """)