import codecs

files = ["sobrejhow.html","jhowarea1.html","jhowarea2.html","jhowarea3.html","jhowdsoft.html","jhowgde.html","jhowinstrumed.html","jhowinstrumed2.html","jhowmodsim.html","jhownatdes.html"]
nomes = ["Pedro V.","Matteo I.","Alegro."]
nomesinho = ["pedro","matteo","alegro"]
palavras = ["Jhow.","jhowarea1.html"]
links = ["jhowdsoft.html","jhowgde.html","jhowinstrumed.html","jhowinstrumed2.html","jhowmodsim.html","jhownatdes.html"]

def replacer(stringe,objeto,rep):
	return stringe[:stringe.index(objeto)] + rep + stringe[(stringe.index(objeto) + len(objeto)):]

# print(replacer("comendo um abacaxi","um","nnnnnnnnnnnnnn"))

life_saber = []

for nome in nomes:
	for arquivo in files:
		
		cod_sobre = list(open(arquivo,"r", encoding='utf8'))
		cod_sobre_novo = []

		for item in cod_sobre:
			if "Jhow." in item:
				item = replacer(item,"Jhow.",nome)
			if "jhowarea1.html" in item:
				item = replacer(item, "jhowarea1.html", nomesinho[nomes.index(nome)]+"area1.html")
			if "jhowarea2.html" in item:
				item = replacer(item, "jhowarea2.html", nomesinho[nomes.index(nome)]+"area2.html")
			if "jhowarea3.html" in item:
				item = replacer(item, "jhowarea3.html", nomesinho[nomes.index(nome)]+"area3.html")
			if '<a class = "volta" href="sobrejhow.html">Voltar</a>' in item:
				item = replacer(item, '<a class = "volta" href="sobrejhow.html">Voltar</a>', '<a class = "volta" href="sobre'+nomesinho[nomes.index(nome)]+'.html">Voltar</a>')

			for coisa in links:
				if coisa in item:
					item = replacer(item, "jhow", nomesinho[nomes.index(nome)])
			
			cod_sobre_novo.append(item)

		print(cod_sobre_novo)
		cod_sobre_novo = "".join(cod_sobre_novo)
		f = open(replacer(arquivo,"jhow",nomesinho[nomes.index(nome)]),'w')
		f.write(cod_sobre_novo)
		f.close()
# # print(cod_sobre_novo)