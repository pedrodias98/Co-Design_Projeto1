def usermaker (form_dict):
	with open('database.txt','a', encoding="utf8") as arquivo:
		arquivo.write("""

|user|

	|name|
	#SEU NOME >>>>>COMPLETO<<<<< COM LETRA MAIUSCULA E TUDO
		"""+form_dict['name']+"""
	|name_end|

	|contact|
		|telephone|
		#SEU TELEFONE
			"""+form_dict['telephone']+"""
		|telephone_end|
		|email|
		#SEU EMAIL
			"""+form_dict['email']+"""
		|email_end|
	|contact_end|

	|description|
		#DESCRICAO DE VOCE, POR VOCE, QUE VAI FICAR NO SEU PERFIL EM "SOBRE MIM"
			"""+form_dict['description']+"""
	|description_end|


	|statistics|
		#LISTA DE INFORMACOES DE PROJETOS NOTAVEIS SEUS, PODE ESCREVER ATE CINCO PROJETOS NOTAVEIS, MAIS QUE ISSO VAI SER IGNORADO
		#SYNTAXE:
		#NOME
		#NOTA OU INFORMACAO SOBRE AVALIACAO
		#CATEGORIA NA QUAL O PROJETO SE ENCAIXA
		|stat1|
			"""+"\n".join(form_dict['stats1'].split("/"))+"""
		|stat1_end|

		|stat2|
			"""+"\n".join(form_dict['stats2'].split("/"))+"""
		|stat2_end|

		|stat3|
			"""+"\n".join(form_dict['stats3'].split("/"))+"""
		|stat3_end|

		|stat4|
			"""+"\n".join(form_dict['stats4'].split("/"))+"""
		|stat4_end|

		|stat5|
			"""+"\n".join(form_dict['stats5'].split("/"))+"""
		|stat5_end|
	|statistics_end|


	### SE FOR ADICIONAR MAIS DE UM PROJETO, DA COPY DESSA LINHA ......

	|project|
		#ESCREVE O NOME NA LINHA SEGUINTE
			"""+form_dict['project1name']+"""
		#ESCREVE A DESCRICAO DO PROJETO NA LINHA SEGUINTE
			"""+form_dict['project1description']+"""
		#ESCREVE A CATEGORIA NA QUAL O PROJETO SE ENCAIXA
			"""+form_dict['project1category']+"""
		#ESCREVE AS HABILIDADES QUE VOCE CULTIVOU COM ESTE PROJETO, COM DOIS ESPACOS ENTRE ELAS E NAO ESCREVA DEMAIS, PRA NAO DAR BUG
			"""+form_dict['project1skills']+"""
		
		#LISTA DE ARQUIVOS DO SEU PROJETO PRA DISPONIBILIZAR PRA DOWNLOAD
		
		#SYNTAXE:
		#NOMEDOARQUIVO
		#NOMEDOARQUIVO2
		#NOMEDOARQUIVO3
		#ETC! :)

		|download|
		|download_end|

		#LISTA DE FOTOS, MESMA SYNTAXE QUE OS ARQUIVOS
		|pictures|
			"""+form_dict['project1pic']+"""
		|pictures_end|
	|project_end|

	### ...... ATÉ ESSA LINHA E MUDA O QUE TA DENTRO DO BLOCO |project| CONTEUDO |project_end|
	### ENTAO VOCE VAI TER VARIOS BLOCOS |project| CONTEUDO |project_end|, UM PARA CADA PROJETO!
|user_end|""")
		arquivo.close()

# usermaker("oi")