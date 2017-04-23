from time import sleep
from random import choice, randint
from os import system, name
#import jsonpickle
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
            'Bulbassauro': [400, 3, 500], 'Pikachu': [600, 5, 400]}

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
        print('Você descobriu o Inspermon secreto! \nSeus atributos são: {}'.format(starters[starter]))
        #sleep(4)

    elif starter == 'Squirtle' or \
           starter == 'Jomander' or \
           starter == 'Bulbassauro':
        system('cls' if name == 'nt' else 'clear')
        print('''Você escolheu o {}
        ataque: {}
        defesa: {}
        Vida: {} \n \n \n '''.format(starter,  starters[starter][0],
                           starters[starter][1], starters[starter][2]))
        #sleep(3)
    else:
        print('Infelizmente, {} não é uma escolha válida... Tente novamente.'.format(starter))
        #sleep(3)
    system('cls' if name == 'nt' else 'clear')
escolha_stats = dex[starter]
starter_stats = escolha_stats


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
    atk = 0
    defe = 1
    hp = 2
    f = randint(1,100)
    seu = dex[game_poke]
    adv = dex[oponente]
    cont = 1

    while True:
        print('Rodada {}'.format(cont))
        print('\n\n\tVida {}: {}'.format(game_poke, seu[hp]))
        print('\n\n\tVida {}: {}\n\n'.format(oponente, adv[hp]))
        cont+=1
        if adv[hp] <= 0:
            return '{} venceu a batalha! \n\nO seu {} foi levado ao Inspèrcenter e recuperou suas forças!'.format(game_poke, game_poke)
        elif adv[hp] > 0:
        	choi=input("Atacar ou fugir? \n\n")
        	choi=choi.title()
        	if choi == "Atacar":
        		if f > 90:
        			adv[hp] = adv[hp] - 1.5*(seu[atk] / adv[defe])
        			seu[hp] = seu[hp] - (adv[atk] / seu[defe])
        			print("Acerto crítico! 1.5x dano")
        		elif f < 5:
        			adv[hp] = adv[hp] - 0*(seu[atk] / adv[defe])
        			seu[hp] = seu[hp] - (adv[atk] / seu[defe])
        			print("{} errou o ataque...".format(game_poke))
        		else:
        			adv[hp] = adv[hp] - (seu[atk] / adv[defe])
        			seu[hp] = seu[hp] - (adv[atk] / seu[defe])
        		if seu[hp] <= 0:
        			return '{} perdeu a batalha! \n\nGAME OVER'.format(game_poke)
        			break
        		else:
        			pass
	       	elif choi == "Fugir":
	       		run=randint(0,9)
	       		if run==0:
	       			print("Você não conseguiu fugir! o adversário começa atacando")
	       		if run!=0:
	       			print("Você fugiu!")
	       			break
	       	else:
	       		print("Essa não é uma escolha disponível... Tente novamente")
	       		#sleep(3)


def batalhaperda(game_poke, oponente):			
    """
    Função batalha para quando a fuga não foi bem sucedida.
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
    atk = 0
    defe = 1
    hp = 2
    f = randint(1,100)
    seu = dex[game_poke]
    adv = dex[oponente]
    cont = 1
    while True:

        seu[hp] = seu[hp] - (adv[atk] / seu[defe])

        print('Rodada {}'.format(cont))
        print('\n\n\tVida {}: {}'.format(game_poke, seu[hp]))
        print('\n\n\tVida {}: {}\n\n'.format(oponente, adv[hp]))
        cont += 1

        if adv[hp] <= 0:
        	return '{} venceu a batalha! \n\nO seu {} foi levado ao Inspèrcenter e recuperou suas forças!'.format(game_poke, game_poke)
        elif adv[hp] > 0:
        	choi=input("Atacar ou fugir? \n\n")
        	choi=choi.title()
        	
        	if choi =="Atacar":
        		if f > 90:
        			adv[hp] = adv[hp] - 1.5*(seu[atk] / adv[defe])
        			seu[hp] = seu[hp] - (adv[atk] / seu[defe])
        			print("Acerto crítico! 1.5x dano")
        		elif f < 5:
        			adv[hp] = adv[hp] - 0*(seu[atk] / adv[defe])
        			seu[hp] = seu[hp] - (adv[atk] / seu[defe])
        			print("{} errou o ataque...".format(game_poke))
        		else:
        			adv[hp] = adv[hp] - (seu[atk] / adv[defe])
        			seu[hp] = seu[hp] - (adv[atk] / seu[defe])
        		if seu[hp] <= 0:
        			return '{} perdeu a batalha! \n\nGAME OVER'.format(game_poke)
        			break
        		else:
        			pass
        	elif choi == "Fugir":
	       		run=randint(0,9)
	       		if run==0:
	       			print("Você não conseguiu fugir! O Inspèrmon inimigo atacou!")
	       		if run!=0:
	       			print("Você fugiu!")
	       			break
	       	else:
	       		print("Essa não é uma escolha disponível... Tente novamente")
	       		#sleep(3)


while escolha_stats[2] > 0:
	system('cls' if name == 'nt' else 'clear')
	i = input('Você quer ir batalhar, dormir ou acessar sua Inspèrdex?\n \n\n')
	i=i.title()
	if "per" in i:
		i.replace("per","pèr")
	escolha_stats = dex[starter]
	starter_stats = escolha_stats
	char = choice(list(mons))
	oponente = dex[char]

	if i == 'Dormir':
		print('Nos vemos na próxima!')
		break

	elif i == 'Batalhar':
		print('Procurando por um oponente...')
		#sleep(randint(1, 5))
		system('cls' if name == 'nt' else 'clear')
		print('A wild {} {} aparece!'.format(char, oponente))


		while escolha_stats[2] > 0 and oponente[2] > 0:
			n = input('Atacar ou fugir? \n \n')
			n=n.title()
			if n == 'Fugir':
				ran=randint(0,100)
				if ran>80:
					print("Você não conseguiu fugir! O Inspèrmon inimigo atacou!")
					#sleep(3)
					print(batalhaperda(starter, char))
					#sleep(300)
					break
				if ran<=80:
					print('Você fugiu')
					#sleep(3)
					break
			if n == 'Atacar':
				print(batalha(starter, char))
				#sleep(3)
				break
	elif i == "Inspèrdex":
		1==1
	else:
		print('Essa não é uma escolha disponível... Tente novamente')
		#sleep(3)