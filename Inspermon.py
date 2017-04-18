import time
import random
import sys
dex = {"0":["Atk","Def","Hp"],"1":["Atk","Def","Hp"],"2":["Atk","Def","Hp"],"3":["Atk","Def","Hp"],"4":["Atk","Def","Hp"],"5":["Atk","Def","Hp"],"6":["Atk","Def","Hp"],"7":["Atk","Def","Hp"],"8":["Atk","Def","Hp"],"9":["Atk","Def","Hp"],"10":["Atk","Def","Hp"]}
mons = ["0","1","2","3","4","5","6","7","8","9"]
Starters = ["0","1","2","3"]
Starter=""
while Starter != "0" and Starter !="1" and Starter !="2" and Starter !="3":
	Starter = input("Escolha um dos três Inspèrmons iniciais: 1,2,3\n")
	if Starter == "0":
		print("Você descobriu o Inspermon secreto! O {} agora é seu!")
	elif Starter == "1" or Starter == "2" or Starter == "3":
		print("Você escolheu o {}".format(Starter))
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
		print("Você venceu a batalha!")
	if Starter[Hp]<=0:
		print("Você perdeu a batalha!")
while True:

	i = input("Você quer ir batalhar ou dormir?  b/d\n")

	if i == "d":
		print("Nos vemos na próxima!")
		break


	if i == "b":
		Oponente = mons[rand()]
		print("Procurando por um oponente...")
		time.sleep(rand())
		print("A wild {} aparece!".format(Oponente))

		while Escolha[2] > 0 and dex[Oponente][2] > 0: #Trocar os "1", "2"... pelos nomes s/ ""
			n = input("Atacar ou fugir? a/f")
			if n == "f":
				print("calma fião")
				continue
			if n == "a":
				batalha(Starter,Oponente)


	else:
		print("Essa não é uma escolha disponível... tente novamente")