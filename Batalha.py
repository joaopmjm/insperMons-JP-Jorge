def batalha(Starter,Opt):
	while True:
		Opt[2]=Opt[2]-(Starter[0]-Opt[1])
		if Opt[2]=<0:
			return "Você venceu a batalha!"
		if Opt[2]>0:
			Starter[2]=Starter[2]-(Opt[0]-Starter[1])
			if Starter[2]=<0:
				return "Você perdeu!"
			if Starter[2]>0:
				continue