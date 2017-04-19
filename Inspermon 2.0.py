import time
import random
import sys
dex = {"Narf":[20,30,60],"Jomander":[50,30,40],"Squirtle":[30,50,40],"Bulbassauro":[40,50,30],"Pikachu":[60,50,40],"Hage-Monstro":[50,50,70],"Hitmon-Jorge":[55,25,40],"Toranxu":[35,15,60],"Alex":[35,15,60],"Gokuma":[35,15,60],"Batatrampo":[35,15,60]}
mons = ["Narf","Jomander","Squirtle","Bulbassauro","Toranxu","Pikachu","Hage-Monstro","Hitmon-Jorge","Alex","Gokuma","Batatrampo"]
Starters = {"Squirtle":[30,50,40],"Jomander":[50,30,40],"Bulbassauro":[40,50,30],"Pikachu":[60,50,40]}
Starter=""
while Starter != "Squirtle" and Starter !="Jomander" and Starter !="Bulbassauro" and Starter !="Pikachu":
	Starter = input("Escolha um dos três Inspèrmons iniciais:\n Squirtle {} \n Jomander {} \n Bulbassauro {} \n".format(Starters["Squirtle"],Starters["Jomander"],Starters["Bulbassauro"]))
	if Starter == "Pikachu":
		print("Você descobriu o Inspermon secreto! O Pikachu {} agora é seu!".format(Starters["Pikachu"]))
	elif Starter == "Squirtle" or Starter == "Jomander" or Starter == "Bulbassauro":
		print("Você escolheu o {} \n ataque: {} \n defesa: {} \n Vida: {}".format(Starter, Starters[Starter][0],Starters[Starter][1],Starters[Starter][2]))
	else:
		print("Infelizmente, {} não é uma escolha válida... tente novamente.".format(Starter))
Escolha_stats = dex[Starter]

def rand():
	randomnum = random.randint(0,10)
	return randomnum
def batalha(Escolha_stats,Oponente,dex):
	Hp=2
	Atk=0
	Def=1
	while True:
		dex[Oponente][Hp]=dex[Oponente][Hp]-(Escolha_stats[Atk]-dex[Oponente][Def])
		if dex[Oponente][Hp]<=0:
			return "Você venceu a batalha!"
		if dex[Oponente][Hp]>0:
			Escolha_stats[Hp]=Escolha_stats[Hp]-(dex[Oponente][Atk]-Escolha_stats[Def])
			if Escolha_stats[Hp]<=0:
				return "Você perdeu!"
			if Escolha_stats[Hp]>0:
				continue
while True:

	i = input("Você quer ir batalhar ou dormir? \n \n b/d\ \n \n")

	if i == "d":
		print("Nos vemos na próxima!")
		break


	if i == "b":
		Oponente = mons[rand()]
		print("Procurando por um oponente...")
		time.sleep(rand())
		print("A wild {} aparece!".format(Oponente))

		while Escolha_stats[2] > 0 and dex[Oponente][2] > 0: #Trocar os "1", "2"... pelos nomes s/ ""
			n = input("Atacar ou fugir? \n a/f \n \n")
			if n == "f":
				print("calma fião")
				continue
			if n == "a":
				batalha(Starter,Oponente,dex)										
	else:
		print("Essa não é uma escolha disponível... tente novamente")