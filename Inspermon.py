import time
import random
Starters = {"0":["Atk","Def","Hp"],"1":["Atk","Def","Hp"],"2":["Atk","Def","Hp"],"3":["Atk","Def","Hp"],}
Starter = input("Escolha um dos três Inspèrmons iniciais: 1,2,3\n")

dex = ["0"={"Atk":10,"Def":2,"Hp":150},"1"={"Atk":15,"Def":1,"Hp":200},"2"={"Atk":13,"Def","Hp"},"3"={"Atk","Def","Hp"},"4"={"Atk","Def","Hp"},"5"={"Atk","Def","Hp"},"6"={"Atk","Def","Hp"},"7"={"Atk","Def","Hp"},"8"={"Atk","Def","Hp"},"9"={"Atk","Def","Hp"},"10"={"Atk","Def","Hp"}]
mons = ["1","2","3","4","5","6","7","8","9"]

def rand():
	randomnum = random.randint(0,9)
	return randomnum
while True:
	Escolha=input("Escolha seu pokemon")
	i = input("Vamos batalhar? Ou vamos dormir?\n")

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
				print("corre negadaaaaaaaa")
				break
			if n == "a":
				print("{} eu escolho você".format(Escolha))
