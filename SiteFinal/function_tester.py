import usermaker as u
# import new_power_page as ppp
# print("  b b  ".strip())
# from math import *


# [print(e**(v0 + (2*t*(beta/massa)))) for t in range(0,60)]


# home_file = open('homepage.html','r', encoding="utf8")

# print(str(home_file))

tags = ["name","telephone","email","description","stats1","stats2","stats3","stats4","stats5","project1name","project1description","project1category","project1skills","project1pic"]

inputs = []

demo = {}

for item in tags:
	inputs.append("""
				<div class="formitem">
		       		<div class="formheader">
						"""+item+"""
					</div>
					<input class="input" type="text" name='"""+item+"""'>
				</div>
				""")

with open('templates/signup.html','w', encoding="utf8") as arquivo:
	arquivo.write("""
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">
		<title>Add Profile</title>
		<link rel="stylesheet" type="text/css" href="../static/design.css"/>
	</head>
	<body>
		<div class="signupheader">
    		<h1 class="head1">Demo da pagina sign up!</h1>
    		<h2 class="head2">Bem vindo ao demo da nossa pagina de sign up, no momento<br>nos so estamos aceitando portfolios novos com 1 projeto
    						<br>e ate 5 estatisticas.
    						<br>Por favor sinta se livre para por seu portfolio no nosso site!
    						<br>
    						<br>
    						<br>INSTRUCOES: escreva as stats no formato "Nome do projeto/Nota/area do estudo" separados por uma barra como se escreve uma data!
    						<br>OBS.: Por favor clique o botao enviar uma vez só!
    		</h2>
    	</div>
    	<div class="holdform">
    		<form action="/pagesetup" method="POST">
        		"""+"".join(inputs)+"""
        		<input type="submit" name="my-form" value="Send">
    		</form>
		</div>
		<a class = "volta" href='homepage.html'>Voltar</a>
	</body>
</html>""")
	arquivo.close()
	# demo[item] = "demonstração" + item

# contact_flag = False

# u.usermaker(demo)
# ppp.pager()