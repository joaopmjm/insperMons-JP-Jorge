ipmons={"fransauro","toranxu","peterodáctil","lecachop","annatchu","jorgenite"}
attck={"fransauro":50,"toranxu":10,"peterodáctil":20,"lecachop":60,"annatchu":35,"jorgenite":100}
defesa={"fransauro":150,"toranxu":75,"peterodáctil":500,"lecachop":125,"annatchu":300,"jorgenite":250}
vida={"fransauro":500,"toranxu":300,"peterodáctil":1000,"lecachop":650,"annatchu":600,"jorgenite":750}
def batalha(ipmons,attck,defesa):
	while vida[ipmons]>0:
		vida[ipmons]=vida[ipmons]-(attck[random]