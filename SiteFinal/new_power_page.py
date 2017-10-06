# -*- coding: utf-8 -*-

import time as t


###########################################################################################################################################################################
#																																										  #
#																	Começo do interpretador																				  #
#																																										  #
###########################################################################################################################################################################

while True:
	# t.sleep(5)
	#Tags usados para o interpretador extrair as informacoes do arquivo .txt
	tags = ["user","name","contact","telephone","email","description","statistics","stat","project","p_name","p_description","category","skills","download","pictures"]

	#Para cada tag, criar uma variavel booleana para servir de flag, indicando para o interpretador quando um lote de informacoes começa ou acaba
	for tag in tags:
		exec(tag+"_flag = False")

	#Dicionario vazio para guardar as informacoes de usuarios
	usuarios = {}

	#Contador para o interpretador saber em qual linha do arquivo .txt ele ta
	current_line = -1

	#Com a base de dados ("database.txt") aberta para leitura:
	with open("database.txt", "r", encoding="utf8") as arquivo:

	#	Criar uma lista na qual cada item é uma linha do arquivo .txt sem espacos a esquerda ou direita
		linhas_do_arquivo = [x.strip() for x in arquivo]

	#	Se for um comentario ou linha vazia, deletar item na lista
		for linha in linhas_do_arquivo:
			if len(linha) == 0:
				linhas_do_arquivo.remove(linha)
				linha = linhas_do_arquivo[current_line]
			elif linha[0] == "#":
				linhas_do_arquivo.remove(linha)
				linha = linhas_do_arquivo[current_line]

	#	Para cada linha do arquivo .txt
		while current_line < (len(linhas_do_arquivo)-1):

	#		Soma 1 no valor do contador, nesse ponto current_line == 0
			current_line += 1
			linha = linhas_do_arquivo[current_line]

	#		Se a linha contém |user|
			if ("|"+tags[0]+"|") in linha:
				user_index = tags[0] + str(len(usuarios))
				print(user_index + " START " + str(current_line))

	#			Criar usuario novo no dicionario 'usuarios'
				usuarios[user_index] = {}
				user_flag = True

	#		Aqui o interpretador lê cada tag e de acordo com a tag, insere a informacao nela guardada no dicionario 'usuarios', no usuario devido
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
						if (linha == ("|"+tags[7]+str(i)+"|")):
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
					print(user_index + " END " + str(current_line))


	#Imprimir usuarios por motivos de debug
	for users in usuarios:
		print("\n" + users + ":")
		print(usuarios[users])
		print("")
	# print(current_line)

	###########################################################################################################################################################################
	#																																										  #
	#																	Fim do interpretador																				  #
	#																																										  #
	###########################################################################################################################################################################

	###########################################################################################################################################################################
	#																																										  #
	#																	Começo do gerador da homepage																		  #
	#																																										  #
	###########################################################################################################################################################################

	home_html = """
	<html>
		<head>
			<meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">
			<link rel="stylesheet" type="text/css" href="../static/design.css"/>
			<title>Design Tech</title>
		</head>

		<body style="margin:0;padding:0">
			<h1 class="titulo_home">Design Tech</h1>
			<h2 class="subtitulo">your source of portfolios</h2>

			<a href="signup.html">
				<img class="addprofile" src="../static/Images/addprofile.png"/>
			</a>
	"""
	for index in range(0,len(usuarios)):
		print(index)
		home_html += """
			<div class="home_container">
				<a href="sobre"""+"_".join(usuarios["user"+str(index)]["name"].split())+""".html"><img class="home_pic" src="../static/Images/"""+usuarios["user"+str(index)]["name"]+""".jpeg"></img></a>
				<div class="home_name"><a class="black" href="sobre"""+"_".join(usuarios["user"+str(index)]["name"].split())+""".html"><b>"""+usuarios["user"+str(index)]["name"][:2+(usuarios["user"+str(index)]["name"][1:].index(usuarios["user"+str(index)]["name"].split()[1][0]))]+""".</b></a></div>
			</div>"""

	home_html += """
		</body>
	</html>
	"""

	home_file = open("templates/"+'homepage.html','w', encoding="utf8")
	home_file.write(home_html)
	home_file.close()


	###########################################################################################################################################################################
	#																																										  #
	#																	Fim do gerador da homepage																			  #
	#																																										  #
	###########################################################################################################################################################################



	###########################################################################################################################################################################
	###########################################################################################################################################################################
	##																																										 ##
	##																	Inicio do gerador de paginas de usuarios															 ##
	##																																										 ##


		###################################################################################################################################################################
		#																																								  #
		#																Perfil do usuario																				  #
		#																																								  #
	for index in range(0,len(usuarios)):
		statisticas = []
		for x in usuarios["user"+str(index)]["statistics"]:
			if usuarios["user"+str(index)]["statistics"][x]["project"] != "":
				statisticas.append("<br>Em "+usuarios["user"+str(index)]["statistics"][x]["project"]+" do tipo "+usuarios["user"+str(index)]["statistics"][x]["type"]+" tirou "+usuarios["user"+str(index)]["statistics"][x]["evaluation"]+".")

		profile_html = open("templates/"+"sobre"+"_".join(usuarios["user"+str(index)]["name"].split())+'.html',"w", encoding="utf8")
		profile_html.write("""
	<html>
		<head>
			<meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">
			<title>"""+usuarios["user"+str(index)]["name"][:(1+usuarios["user"+str(index)]["name"].index(usuarios["user"+str(index)]["name"].split()[-1][0]))]+""".</title>
			<link rel="stylesheet" type="text/css" href="../static/design.css"/>
		</head>

		<body style="margin:0;padding:0">
			<div class = "sobremim_titulo_container">
				<div class = "titulo_sobremim">
					<b>"""+usuarios["user"+str(index)]["name"][:(1+usuarios["user"+str(index)]["name"].index(usuarios["user"+str(index)]["name"].split()[-1][0]))]+""".</b>
				</div>
			</div>

			<div class="sobremim_container1">
				<img class="sobremim_imagem" src="../static/Images/"""+usuarios["user"+str(index)]["name"]+""".jpeg"></img>

				<div class="sobremim_subtitulo">
					Contato
				</div>
		
				<div class="sobremim_subtexto" href="homepage.html">
					Telefone:<br>"""+usuarios["user"+str(index)]["contact"]["telephone"]+"""
					<br>Email:<br>"""+usuarios["user"+str(index)]["contact"]["email"]+"""
				</div>			
			</div>

			<div class="sobremim_container2">
				<div class="sobremim_titulo" href="homepage.html">
					Sobre mim:
				</div>

				<div class="sobremim_texto">
						"""+usuarios["user"+str(index)]["description"]+"""
				</div>
			</div>

			<div class="sobremim_container3">
				<div class="sobremim_subtitulo2">
					Areas de atuacao (Links):
				</div>

				<div class="sobremim_container4">
					<a class="a_p" href='"""+"_".join(usuarios["user"+str(index)]["name"].split())+"""area1.html'>
							<img class="a_p_img" src="../static/Images/design.jpg"></img>
							Software e Design
					<a/>
				</div>

				<div class="sobremim_container4">
					<a class="a_p" href='"""+"_".join(usuarios["user"+str(index)]["name"].split())+"""area3.html'>
							<img class="a_p_img" src="../static/Images/sistems.jpg"></img>
							Sistemas do mundo
					<a/>
				</div>

				<div class="sobremim_container4">
					<a class="a_p" href='"""+"_".join(usuarios["user"+str(index)]["name"].split())+"""area2.html'>
							<img class="a_p_img" src="../static/Images/theory.jpg"></img>
							Trabalhos teoricos
					<a/>
				</div>
			
				<div class="sobremim_subtitulo3">
					Projetos Notaveis:
				</div>

				<div class="sobremim_texto3" href="homepage.html">
					"""+"".join(statisticas)+"""
				</div>
			</div>
			<a class = "volta" href="homepage.html">Voltar</a>
		</body>
	</html>""")
		profile_html.close()
		#																																								  #
		#																Fim do perfil de usuario																		  #
		#																																								  #
		###################################################################################################################################################################



		###################################################################################################################################################################
		#																																								  #
		#																Paginas:																						  # 
		#																		<usuario> em <x> e <y>.																	  #
		#																Onde x e y são categorias de projeto semelhantes												  #
		#																																								  #
		subject_areas1 = {"software" : ["Software","software", "Uma sequência de instruções escritas para serem interpretadas por um computador com o objetivo de executar tarefas específicas. Também pode ser definido como os programas que comandam o funcionamento de um computador."],
						"design" : ["Design", "design", "A idealização, criação, desenvolvimento, configuração, concepção, elaboração e especificação de artefatos, normalmente produzidos industrialmente ou por meio de sistema de produção seriada que demanda padronização dos componentes e desenho normalizado."]}
		subject_areas2 = {"electric2" : ["Eletricidade (téses)","electric2", "Trabalhos escritos relacionados a eletricidade. Relatorios de projetos sao encontrados aqui."],
						"essay" : ["Trabalhos escritos","essay", "Trabalhos escritos, em sua maior parte debatendo visoes de mundo e buscando uma perspectiva propria de certos problemas."]}
		subject_areas3 = {"modelagem" : ["Modelagem e simulação do mundo fisico","modelagem", "Modelagem matematica de fenomenos que ocorrem no mundo fisico."],
						"electric" : ["Eletricidade","electric", "Tudo que se relaciona a eletricidade, que nao seja teorico, fica aqui."]}
		listinha = [subject_areas1,subject_areas2,subject_areas3]

		for area in range(1,4):

			debug1 = usuarios["user"+str(index)]["name"][:(1+usuarios["user"+str(index)]["name"].index(usuarios["user"+str(index)]["name"].split()[-1][0]))]

			for_area = listinha[area-1]

			area_html = open("templates/"+"_".join(usuarios["user"+str(index)]["name"].split())+'area'+str(area)+'.html',"w", encoding="utf8")
			area1_html = ("""
	<html>
		<head>
			<title>"""+debug1+"""</title>
			<meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">
			<link rel="stylesheet" type="text/css" href="../static/design.css"/>
			
		</head>
		<body style="margin:0;padding:0">
			<div class = "titulo">
				<b>""" + debug1 +""". em """+" e ".join([for_area[x][0] for x in for_area])+"""</b>
			</div>

	""")

			###########################################################################################################################################################
			#																																						  #
			#															Paginas:																					  # 
			#																	<usuario> em <x>.																	  #
			#															Onde x é uma categoria de projeto															  #
			#																																						  #

			for x in for_area:
				materia = for_area[x]

				has_project = False

				area2_html = ("""
	<html>
		<head>
			<title>"""+debug1+""". """+materia[0]+"""</title>
			<meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">
			<link rel="stylesheet" type="text/css" href="../static/design.css"/>
			
		</head>
		<body style="margin:0;padding:0">
			<div class = "titulo">
				<b>"""+debug1+""". em """ +materia[0]+ """</b>
			</div>

	""")

				###################################################################################################################################################
				#																																				  #
				#														Posts de projetos																		  #
				#																																				  #
				for y in  usuarios["user"+str(index)]["projects"]:

	#				IF A CATEGORIA DE UM DADO PROJETO 'y' É IGUAL À CATEGORIA DA PAGINA SENDO CRIADA:
					if usuarios["user"+str(index)]["projects"][y]["category"].lower() == materia[1].lower():
						
	#					PRINTS POR MOTIVOS DE DEBUG
						print(usuarios["user"+str(index)]["projects"][y]["category"].lower() + " = " + materia[1].lower())

						has_project = True


	#					CRIA UM "MODULO" POR PROJETO
						area2_html += str("""

			<div class="subtitle" href="homepage.html">
		""" + usuarios["user"+str(index)]["projects"][y]["p_name"] + """
			</div>
			<div class="texto">
				<img class="imagem" src="../static/Images/"""+usuarios["user"+str(index)]['name']+" "+usuarios["user"+str(index)]["projects"][y]["p_name"]+""".png"/>
				"""+usuarios["user"+str(index)]["projects"][y]["p_description"]+"""
			</div>""")

				if has_project == False:
	#			IF (NAO TIVER NENHUM PROJETO NESSA CATEGORIA):
					area2_html += ("""
			<div class="no_p">
						"""+debug1.split()[0]+""" nao tem nenhum projeto aqui!
			</div>""")
	#					"USUARIO NAO TEM NENHUM PROJETO AQUI!"


				#																																				  #
				#														Posts de projetos																		  #
				#																																				  #
				###################################################################################################################################################
				
	#			BOTAO VOLTAR, ADICIONADO NO FINAL DE TODAS AS PAGINAS, PARA NAVEGACAO DO SITE
				area2_html += """
			<a class = "volta" href='""" + "_".join(usuarios["user"+str(index)]["name"].split())+'area'+str(area)+""".html'>Voltar</a>
		</body>
	</html>"""

	#			SALVAR UM ARQUIVO .html COM A INFORMACAO DA VARIAVEL area2_html , NA PASTA 'templates/' COM O FORMATO "<nome do usuario><categoria de projetos>.html"
				area3_html = open("templates/"+"_".join(usuarios["user"+str(index)]["name"].split())  + materia[1] + ".html", 'w', encoding="utf8")
				area3_html.write(area2_html)
				area3_html.close()

			#																																						  #
			#															Paginas:																					  # 
			#																	<usuario> em <x>.																	  #
			#															Onde x é uma categoria de projeto															  #
			#																																						  #
			###########################################################################################################################################################

				area1_html += str("""
			<div class="subtitle" href="homepage.html">
	""" + materia[0] + """
			</div>
			<a href='""" + "_".join(usuarios["user"+str(index)]["name"].split()) + materia[1] + """.html'>
				<div class="texto">
					<img class="imagem" src="../static/Images/"""+materia[1]+"""_imagem_1.png"/>
					"""+materia[2]+"""
				</div>
			</a>""")

			area1_html += """

			<a class = "volta" href="sobre""" + "_".join(usuarios["user"+str(index)]["name"].split()) + """.html">Voltar</a>
		</body>
	</html>"""

			area_html.write(area1_html)
			area_html.close()
		#																																								  #
		#																Paginas:																						  # 
		#																		<usuario> em <x> e <y>.																	  #
		#																Onde x e y são categorias de projeto semelhantes												  #
		#																																								  #
		###################################################################################################################################################################


	##																																										 ##
	##																	Fim do gerador de perfil de usuario																	 ##
	##																																										 ##
	###########################################################################################################################################################################
	###########################################################################################################################################################################
	break