from time import sleep
from random import choice, randint
from os import system, name
system('cls' if name == 'nt' else 'clear')
# Modelo: 'Nome': [Ataque, Defesa, Vida]
dex = {'Narf': [200, 3, 600], 'Jomander': [500, 3, 400],
       'Squirtle': [300, 5, 400], 'Bulbassauro': [400, 5, 300],
       'Pikachu': [600, 5, 400], 'Hage-Monstro': [500, 5, 700],
       'Hitmon-Jorge': [550, 2.5, 400], 'Toranxu': [350, 1.5, 600],
       'Alex': [350, 1.5, 600], 'Gokuma': [350, 1.5, 600],
       'Batatrampo': [350, 1.5, 600]}

mons = dex.keys()
starters = {'Squirtle': [300, 5, 400], 'Jomander': [500, 3, 400],
            'Bulbassauro': [400, 3, 300], 'Pikachu': [600, 5, 400]}

starter = ''
while starter not in starters.keys():
    starter = input('''Escolha um dos três Inspèrmons iniciais:
    Squirtle {}
    Jomander {}
    Bulbassauro {} \n'''.format(starters['Squirtle'],
                                starters['Jomander'],
                                starters['Bulbassauro']))
    starter=starter.title()
    if starter == 'Pikachu':
        system('cls' if name == 'nt' else 'clear')
        print('Você descobriu o Inspermon secreto!')
        print('O Pikachu {} agora é seu! \n \n \n aperte "enter" para continuar'.format(starters['Pikachu']))

    elif starter == 'Squirtle' or \
           starter == 'Jomander' or \
           starter == 'Bulbassauro':
        system('cls' if name == 'nt' else 'clear')
        print('''Você escolheu o {}
        ataque: {}
        defesa: {}
        Vida: {} \n \n \n aperte "enter" para continuar'''.format(starter,  starters[starter][0],
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

        adv[hp] = adv[hp] - (seu[atk] / adv[defe])

        if adv[hp] <= 0:
            return '{} venceu a batalha!'.format(game_poke)
        if adv[hp] > 0:
        	choi=input("Atacar ou fugir? \n\n")
        	choi=choi.title()
        	if choi =="Atacar":
	            seu[hp] = seu[hp] - (adv[atk] / seu[defe])
	            if seu[hp] <= 0:
	                return '{} perdeu!'.format(oponente)
	            if seu[hp] > 0:
	            	pass
	       	if choi == "Fugir":
	       		run=randint(0,9)
	       		if run==0:
	       			print("Você não conseguiu fugir! o adversário começa atacando")
	       		if run!=0:
	       			print("Você fugiu!")
	       			break
def batalhaperda(game_poke, oponente):
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

        seu[hp] = seu[hp] - (adv[atk] / seu[defe])

        if seu[hp] <= 0:
            return 'você perdeu'
        if seu[hp] > 0:
        	choi=input("Atacar ou fugir? \n\n")
        	choi=choi.title()
        	if choi =="Atacar":
	            adv[hp] = adv[hp] - (seu[atk] / adv[defe])
	            if adv[hp] <= 0:
	                return '{} perdeu!'.format(oponente)
	            if adv[hp] > 0:
	            	pass
	       	if choi == "Fugir":
	       		run=randint(0,9)
	       		if run==0:
	       			print("Você não conseguiu fugir!")
	       		if run!=0:
	       			print("Você fugiu!")
	       			break
        cont += 1
while True:
    system('cls' if name == 'nt' else 'clear')
    i = input('Você quer ir batalhar ou dormir? \n \n')
    i=i.title()

    if i == 'Dormir':
        print('Nos vemos na próxima!')
        break

    if i == 'Batalhar':
        char = choice(list(mons))
        oponente = dex[char]
        print('Procurando por um oponente...')
        sleep(randint(1, 5))
        system('cls' if name == 'nt' else 'clear')
        print('A wild {} {} aparece!'.format(char, oponente))

        while escolha_stats[2] > 0 and oponente[2] > 0:
            n = input('Atacar ou fugir? \n \n')
            n=n.title()
            if n == 'Fugir':
                ran=randint(0,100)
                if ran>70:
                	print('Você não conseguiu fugir dessa batalha')
                	sleep(3)
                	print(batalhaperda(starter, char))
                	sleep(300)
                	break
                if ran<=70:
                	print('Você fugiu')
                	sleep(3)
                	break
            if n == 'Atacar':
                print(batalha(starter, char))
                sleep(3)
                break
    else:
        print('Essa não é uma escolha disponível... tente novamente')