# -*- coding: utf-8 -*-

tags = ["user","name","contact","telephone","email","description","statistics","stat","project","p_name","p_description","category","skills","download","pictures"]

for tag in tags:
	exec(tag+"_flag = False")

usuarios = {}
current_line = -1

with open("database.txt", "r") as arquivo:
	linhas_do_arquivo = [x.strip() for x in arquivo]
	
	for linha in linhas_do_arquivo:
		if len(linha) > 0:
			if linha[0][0] == "#" or linha[0] == "#":
				linhas_do_arquivo.remove(linha)

	for linha in linhas_do_arquivo:

		current_line += 1

		if linha == ("|"+tags[0]+"|"):
			user_index = tags[0] + str(len(usuarios))
			usuarios[user_index] = {}
			user_flag = True

		if user_flag == True:

			if linha == ("|"+tags[1]+"|"):
				usuarios[user_index][tags[1]] = linhas_do_arquivo[current_line + 1]
				name_flag = True

			elif linha == ("|"+tags[2]+"|"):
				usuarios[user_index][tags[2]] = {}
				contact_flag = True

			elif contact_flag == True:
				if linha == ("|"+tags[3]+"|"):
					usuarios[user_index][tags[2]][tags[3]] = linhas_do_arquivo[current_line + 1]
				elif linha == ("|"+tags[4]+"|"):
					usuarios[user_index][tags[2]][tags[4]] = linhas_do_arquivo[current_line + 1]

			elif linha == ("|"+tags[5]+"|"):
				usuarios[user_index][tags[5]] = linhas_do_arquivo[current_line + 1]
				description_flag = True

			elif linha == ("|"+tags[6]+"|"):
				usuarios[user_index][tags[6]] = {}
				statistics_flag = True

			elif statistics_flag == True:
				for i in range(1,6):
					if linha == ("|"+tags[7]+str(i)+"|"):
						usuarios[user_index][tags[6]][tags[7]+str(i)] = {"project":(linhas_do_arquivo[current_line + 1]),
																"evaluation":(linhas_do_arquivo[current_line + 2]),
																"type":(linhas_do_arquivo[current_line + 3])}

			elif linha == ("|"+tags[8]+"|"):
				try:
					usuarios[user_index][tags[8]+"s"][tags[8] + str(len(usuarios[user_index][tags[8]+"s"]))] = {
					tags[9] : linhas_do_arquivo[current_line + 1],
					tags[10] : linhas_do_arquivo[current_line + 2],
					tags[11] : linhas_do_arquivo[current_line + 3],
					tags[12] : linhas_do_arquivo[current_line + 4]
					}
				except KeyError:
					usuarios[user_index][tags[8]+"s"] = {}
					usuarios[user_index][tags[8]+"s"][tags[8] + str(len(usuarios[user_index][tags[8]+"s"]))] = {
					tags[9] : linhas_do_arquivo[current_line + 1],
					tags[10] : linhas_do_arquivo[current_line + 2],
					tags[11] : linhas_do_arquivo[current_line + 3],
					tags[12] : linhas_do_arquivo[current_line + 4]
					}
				project_flag = True

			elif project_flag == True and linha != ("|"+tags[8]+"_end|"):
				if linha == ("|"+tags[13]+"|"):
					usuarios[user_index][tags[8]+"s"][tags[8] + str(len(usuarios[user_index][tags[8]+"s"])-1)][tags[13]] = []
					download_flag = True
				elif linha == ("|"+tags[14]+"|"):
					usuarios[user_index][tags[8]+"s"][tags[8] + str(len(usuarios[user_index][tags[8]+"s"])-1)][tags[14]] = []
					pictures_flag = True
				elif download_flag == True and linha != ("|"+tags[13]+"_end|"):
					usuarios[user_index][tags[8]+"s"][tags[8] + str(len(usuarios[user_index][tags[8]+"s"])-1)][tags[13]].append(linha)
				elif pictures_flag == True and linha != ("|"+tags[14]+"_end|"):
					usuarios[user_index][tags[8]+"s"][tags[8] + str(len(usuarios[user_index][tags[8]+"s"])-1)][tags[14]].append(linha)

			for tag in tags[1:]:
				if linha == "|"+tag+"_end|":
					exec(tag+"_flag = False")
			
			if linha == "|user_end|":
				user_flag = False
				print(current_line)

for users in usuarios:
	print(users + ":")
	print(usuarios[users])
	print("")
print(current_line)

#####################################################################################################################################################
#####################################################################################################################################################

def replacer(stringe,objeto,rep):
	return stringe[:stringe.index(objeto)] + rep + stringe[(stringe.index(objeto) + len(objeto)):]

subject_areas1 = {"software" : ["Software","software", "DESCRICAO DA AREA DO CONHECIMENTO"],
				"design" : ["Design", "design", "DESCRICAO DA AREA DO CONHECIMENTO"]}
subject_areas2 = {"electric2" : ["Eletricidade (téses)","electric2", "DESCRICAO DA AREA DO CONHECIMENTO"],
				"essay" : ["Trabalhos escritos","essay", "DESCRICAO DA AREA DO CONHECIMENTO"]}
subject_areas3 = {"modelagem" : ["Modelagem e simulação do mundo fisico","modelagem", "DESCRICAO DA AREA DO CONHECIMENTO"],
				"electric" : ["Eletricidade","electric", "DESCRICAO DA AREA DO CONHECIMENTO"]}

# Electric
# Electric2 #se quiser por relatórios
# Essay #significa tése em inglês, seria equivalente a GDE
# Modelagem
# Design



home_html = """
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="design.css"/>
		<title>Design Tech</title>
	</head>

	<body style="margin:0;padding:0">
		<h1 class="titulo_home">Design Tech</h1>
		<h2 class="subtitulo">your source of portfolios</h2>
"""
for index in range(0,len(usuarios)):
	home_html += """
		<div class="home_container">
			<a href="sobre"""+"_".join(usuarios["user"+str(index)]["name"].split())+""".html"><img class="home_pic" src="Images/"""+usuarios["user"+str(index)]["name"]+""".png"></img></a>
			<div class="home_name"><a class="black" href="sobre"""+"_".join(usuarios["user"+str(index)]["name"])+""".html"><b>"""+usuarios["user"+str(index)]["name"][:(1+usuarios["user"+str(index)]["name"].index(usuarios["user"+str(index)]["name"].split()[-1][0]))]+""".</b></a></div>
		</div>"""

home_html += """
	</body>
</html>
"""

home_file = open('homepage.html','w')
home_file.write(home_html)
home_file.close()





for index in range(0,len(usuarios)):
	profile_html = open("sobre"+"_".join(usuarios["user"+str(index)]["name"].split())+'.html',"w")
	profile_html.write("""
<html>
	<head>
		<meta charset="UTF-8">
		<title>"""+usuarios["user"+str(index)]["name"][:(1+usuarios["user"+str(index)]["name"].index(usuarios["user"+str(index)]["name"].split()[-1][0]))]+""".</title>
		<link rel="stylesheet" type="text/css" href="design.css"/>
	</head>

	<body style="margin:0;padding:0">
		<div class = "titulo_sobremim">
			<b>"""+usuarios["user"+str(index)]["name"][:(1+usuarios["user"+str(index)]["name"].index(usuarios["user"+str(index)]["name"].split()[-1][0]))]+""".</b>
		</div>

		<div class="sobremim_container2">
			<img class="sobremim_imagem" src="Images/"""+usuarios["user"+str(index)]["name"]+""".png"></img>

			<div class="sobremim_subtitulo">
				Contato
				<div class="sobremim_subtexto" href="homepage.html">
					<br>Telefone: """+usuarios["user"+str(index)]["contact"]["telephone"]+"""
					<br>Email: """+usuarios["user"+str(index)]["contact"]["email"]+"""
				</div>
			</div>
		</div>

		<div class="sobremim_container1">
			<div class="sobremim_titulo" href="homepage.html">
				Sobre mim:
				<div class="sobremim_texto">
					"""+usuarios["user"+str(index)]["description"]+"""
				</div>
			</div>
		</div>

		<div class="sobremim_subtitulo2">
			Areas de atuacao:
			<div class="sobremim_container3">
				<a class="a_p" href='"""+"_".join(usuarios["user"+str(index)]["name"].split())+"""area1.html'>
						<img class="a_p_img" src="Images/design.jpg"></img>
						Software e Design
				<a/>
				<a class="a_p" href='"""+"_".join(usuarios["user"+str(index)]["name"].split())+"""area3.html'>
						<img class="a_p_img" src="Images/sistems.jpg"></img>
						Sistemas do mundo
				<a/>
				<a class="a_p" href='"""+"_".join(usuarios["user"+str(index)]["name"].split())+"""area2.html'>
						<img class="a_p_img" src="Images/theory.jpg"></img>
						Trabalhos teoricos
				<a/>
			</div>
		</div>

		<div class="sobremim_subtitulo3">
			Projetos Notaveis:
			<div class="sobremim_texto3" href="homepage.html">
				"""+" ".join([("<br>Em "+usuarios["user"+str(index)]["statistics"][x]["project"]+" do tipo "+usuarios["user"+str(index)]["statistics"][x]["type"]+" tirou "+usuarios["user"+str(index)]["statistics"][x]["evaluation"]+".") for x in usuarios["user"+str(index)]["statistics"]])+"""
			</div>
		</div>
		<a class = "volta" href="homepage.html">Voltar</a>
	</body>
</html>""")
	profile_html.close()
	






	subject_areas1 = {"software" : ["Software","software", "DESCRICAO DA AREA DO CONHECIMENTO"],
					"design" : ["Design", "design", "DESCRICAO DA AREA DO CONHECIMENTO"]}
	subject_areas2 = {"electric2" : ["Eletricidade (téses)","electric2", "DESCRICAO DA AREA DO CONHECIMENTO"],
					"essay" : ["Trabalhos escritos","essay", "DESCRICAO DA AREA DO CONHECIMENTO"]}
	subject_areas3 = {"modelagem" : ["Modelagem e simulação do mundo fisico","modelagem", "DESCRICAO DA AREA DO CONHECIMENTO"],
					"electric" : ["Eletricidade","electric", "DESCRICAO DA AREA DO CONHECIMENTO"]}
	listinha = [subject_areas1,subject_areas2,subject_areas3]


	for area in range(1,4):

		debug1 = usuarios["user"+str(index)]["name"][:(1+usuarios["user"+str(index)]["name"].index(usuarios["user"+str(index)]["name"].split()[-1][0]))]

		for_area = listinha[area-1]

		area_html = open("_".join(usuarios["user"+str(index)]["name"].split())+'area'+str(area)+'.html',"w")
		area1_html = ("""
<html>
	<head>
		<title>"""+debug1+"""</title>
		<link rel="stylesheet" type="text/css" href="design.css"/>
		<link rel="icon" type="image/png" href="design_tab_icon.png"/>
	</head>
	<body style="margin:0;padding:0">
		<div class = "titulo">
			<b>""" + debug1 +""". em """+" e ".join([for_area[x][0] for x in for_area])+"""</b>
		</div>

""")


		for x in for_area:
			materia = for_area[x]
###############################################################
			for y in  usuarios["user"+str(index)]["projects"]:
				if usuarios["user"+str(index)]["projects"][y]["category"].lower() == materia[1].lower():
					area2_html = ("""
	<html>
		<head>
			<title>"""+debug1+""". """+materia[0]+"""</title>
			<link rel="stylesheet" type="text/css" href="design.css"/>
			<link rel="icon" type="image/png" href="design_tab_icon.png"/>
		</head>
		<body style="margin:0;padding:0">
			<div class = "titulo">
				<b>"""+debug1+""". em """ +materia[0]+ """</b>
			</div>

	""")

					print(usuarios["user"+str(index)]["projects"][y]["category"].lower())
					print(materia[1].lower())


					area2_html += str("""
			<div class="subtitle" href="homepage.html">
	""" + usuarios["user"+str(index)]["projects"][y]["p_name"] + """
			</div>
			<div class="texto">
				<img class="imagem" src="Images/"""+usuarios["user"+str(index)]["projects"][y]["p_name"]+""".png"/>
				"""+usuarios["user"+str(index)]["projects"][y]["p_description"]+"""
			</div>
			""")
					area2_html += """

			<a class = "volta" href='""" + "_".join(usuarios["user"+str(index)]["name"].split())+'area'+str(area)+""".html'>Voltar</a>

			<a class = "nome1" href="sobrepedro.html">Pedro V</a>
			<a class = "nome2" href="sobreMatteo_Iannoni.html">Matteo I</a>
			<a class = "nome3" href="sobrejhow.html">Jhow</a>
			<a class = "nome4" href="sobrealegro.html">Alegro</a>
		</body>
	</html>"""
					area3_html = open("_".join(usuarios["user"+str(index)]["name"].split())  + materia[1] + ".html", 'w')
					area3_html.write(area2_html)
					area3_html.close()
				else:
					try:
						open("_".join(usuarios["user"+str(index)]["name"].split())  + materia[1] + ".html", 'r')
					except FileNotFoundError:
						area2_html = ("""
	<html>
		<head>
			<title>"""+debug1+""". """+materia[0]+"""</title>
			<link rel="stylesheet" type="text/css" href="design.css"/>
			<link rel="icon" type="image/png" href="design_tab_icon.png"/>
		</head>
		<body style="margin:0;padding:0">
			<div class = "titulo">
				<b>"""+debug1+""". em """ +materia[0]+ """</b>
			</div>

			<a class = "volta" href='""" + "_".join(usuarios["user"+str(index)]["name"].split())+'area'+str(area)+""".html'>Voltar</a>

			<a class = "nome1" href="sobrepedro.html">Pedro V</a>
			<a class = "nome2" href="sobreMatteo_Iannoni.html">Matteo I</a>
			<a class = "nome3" href="sobrejhow.html">Jhow</a>
			<a class = "nome4" href="sobrealegro.html">Alegro</a>
		</body>
	</html>""")
					area3_html = open("_".join(usuarios["user"+str(index)]["name"].split())  + materia[1] + ".html", 'w')
					area3_html.write(area2_html)
					area3_html.close()
###############################################################
			

###############################################################
			area1_html += str("""
		<div class="subtitle" href="homepage.html">
""" + materia[0] + """
		</div>
		<a href='""" + "_".join(usuarios["user"+str(index)]["name"].split()) + materia[1] + """.html'>
			<div class="texto">
				<img class="imagem" src="Images/"""+materia[1]+"""_imagem_1.jpg"/>
				"""+materia[2]+"""
			</div>
		</a>""")

		area1_html += """

		<a class = "volta" href="sobre""" + "_".join(usuarios["user"+str(index)]["name"].split()) + """.html">Voltar</a>

		<a class = "nome1" href="sobrepedro.html">Pedro V</a>
		<a class = "nome2" href="sobreMatteo_Iannoni.html">Matteo I</a>
		<a class = "nome3" href="sobrejhow.html">Jhow</a>
		<a class = "nome4" href="sobrealegro.html">Alegro</a>
	</body>
</html>"""
#################################################################
		area_html.write(area1_html)
		area_html.close()


print(usuarios["user1"])