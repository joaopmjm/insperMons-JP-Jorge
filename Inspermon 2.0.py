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
	randomnum = random.randint(0,9)
	return randomnum
def batalha(Starter,Oponente):
	while Starter[Hp]>0 or Oponente[Hp]>0:
		Oponente[Hp]=Starter[Atk]-Oponente[Def]
		Starter[Hp]=Oponente[Atk]-Starter[Def]
		time.sleep(3)
	if Oponente[Hp]<=0:
		return "Você venceu a batalha!"
	if Starter[Hp]<=0:
		return "Você perdeu a batalha!"
while True:

	i = input("Você quer ir batalhar ou dormir? \n b/d\n")

	if i == "d":
		print("Nos vemos na próxima!")
		break


	if i == "b":
		Oponente = mons[rand()]
		print("Procurando por um oponente...")
		time.sleep(rand())
		print("A wild {} aparece!".format(Oponente))

		while Escolha_stats[2] > 0 and dex[Oponente][2] > 0: #Trocar os "1", "2"... pelos nomes s/ ""
			n = input("Atacar ou fugir? a/f")
			if n == "f":
				print("calma fião")
				continue
			if n == "a":
				batalha(Starter,Oponente)														
	else:
		print("Essa não é uma escolha disponível... tente novamente")