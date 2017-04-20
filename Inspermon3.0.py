from time import sleep
from random import choice, randint
from os import system, name

# Modelo: 'Nome': [Ataque, Defesa, Vida]
dex = {'Narf': [20, 30, 60], 'Jomander': [50, 30, 40],
       'Squirtle': [30, 50, 40], 'Bulbassauro': [40, 50, 30],
       'Pikachu': [60, 50, 40], 'Hage-Monstro': [50, 50, 70],
       'Hitmon-Jorge': [55, 25, 40], 'Toranxu': [35, 15, 60],
       'Alex': [35, 15, 60], 'Gokuma': [35, 15, 60],
       'Batatrampo': [35, 15, 60]}

mons = dex.keys()
starters = {'Squirtle': [30, 50, 40], 'Jomander': [50, 30, 40],
            'Bulbassauro': [40, 50, 30], 'Pikachu': [60, 50, 40]}

starter = ''
while starter not in starters.keys():
    starter = input('''Escolha um dos três Inspèrmons iniciais:
    Squirtle {}
    Jomander {}
    Bulbassauro {} \n'''.format(starters['Squirtle'],
                                starters['Jomander'],
                                starters['Bulbassauro']))
    if starter == 'Pikachu':
        system('cls' if name == 'nt' else 'clear')
        print('Você descobriu o Inspermon secreto!')
        print('O Pikachu {} agora é seu!'.format(starters['Pikachu']))

    elif starter == 'Squirtle' or \
           starter == 'Jomander' or \
           starter == 'Bulbassauro':
        system('cls' if name == 'nt' else 'clear')
        print('''Você escolheu o {}
        ataque: {}
        defesa: {}
        Vida: {}'''.format(starter,  starters[starter][0],
                           starters[starter][1], starters[starter][2]))
    else:
        print('''Infelizmente, {} não é uma escolha válida...
        tente novamente.'''.format(starter))
    input()

escolha_stats = dex[starter]


def batalha(game_poke, oponente):
    """
    Função batalha.
    Essa função executa uma batalha entre seu pokémon e um pokémon randômico
    Args:
        - game_poke: Seu pokémon
        - oponente: Pokémon do oponente
    Vars:
        - Hp: Vida
        - atk: Ataque
        - defe: Defesa
        - seu: Seu pokemon
        - adv: Pokémon adversário
    """
    system('cls' if name == 'nt' else 'clear')
    print('######### BATALHA #########')
    print('######### {} Vs. {} #########'.format(game_poke, oponente))
    hp = 2
    atk = 0
    defe = 1
    seu = dex[game_poke]
    adv = dex[oponente]
    cont = 1
    while True:
        print('Rodada {}'.format(cont))
        print('\n\n\tVida {}: {}'.format(game_poke, seu[hp]))
        print('\n\n\tVida {}: {}\n\n'.format(oponente, adv[hp]))

        adv[hp] = adv[hp] - (seu[atk] - adv[defe])

        if adv[hp] <= 0:
            return '{} venceu a batalha!'.format(game_poke)
        if adv[hp] > 0:
            seu[hp] = seu[hp] - (adv[atk] - seu[defe])
            if seu[hp] <= 0:
                return '{} perdeu!'.format(oponente)
            if seu[hp] > 0:
                pass
        cont += 1


while True:
    system('cls' if name == 'nt' else 'clear')
    i = input('Você quer ir batalhar ou dormir? \n \n b ou d \n \n')

    if i == 'd':
        print('Nos vemos na próxima!')
        break

    if i == 'b':
        char = choice(list(mons))
        oponente = dex[char]
        print('Procurando por um oponente...')
        sleep(randint(1, 10))
        system('cls' if name == 'nt' else 'clear')
        print('A wild {} {} aparece!'.format(char, oponente))

        while escolha_stats[2] > 0 and oponente[2] > 0:
            n = input('Atacar ou fugir? \n a/f \n \n')
            if n == 'f':
                print('calma fião')
                continue
            if n == 'a':
                print(batalha(starter, char))
                input()
    else:
        print('Essa não é uma escolha disponível... tente novamente')