import time
def scan():    # lafonction scan va indiquer l'etat du clavier: "a", "e", "b", "f" ou "rien"
	etat_clavier = raw_input("scan ?")
	if etat_clavier =='':
		etat_clavier="rien"
		
	permis = ['rien', 'a', 'e', 'b', 'f']
	if etat_clavier in permis:
		print etat_clavier
	else:
		print "seules les lettres a, e, b, f sont autorisees"
	return etat_clavier
###################

boucle_no=0;
etat_systeme="/attente/"
etat_clavier='rien'
consonne_memorisee=''
voyelle_memorisee=''

def attente():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	etat_clavier=scan()
	print "etat_clavier:" + str(etat_clavier)
	if etat_clavier in ["a","e"]:
		voyelle_memorisee=etat_clavier
		etat_systeme="/voyelle_appuyee/"
		print "etat_systeme passe de /attente/ a /voyelle_appuyee/"
		print "on attent la liberation du bouton pour emettre le son " + voyelle_memorisee
	elif etat_clavier in ["b","f"]:
		consonne_memorisee=etat_clavier
		etat_systeme="/consonne_appuyee/"
		print "etat_systeme passe de /attente/ a /consonne_appuyee/"
		print "on attend la liberation du bouton " + consonne_memorisee + " puis l'arrivee de la voyelle" 


def consonne_appuyee():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	etat_clavier=scan()
	if etat_clavier !="rien":
		print "etat_systeme reste sur /consonne_appuyee/ " + str(etat_clavier)
	else:
		etat_systeme="/consonne_vue/"
		print "etat_systeme passe de /consonne_appuyee/ a /consonne_vue/"

def consonne_vue():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	etat_clavier=scan()
	print "etat_clavier:" + str(etat_clavier)
	if etat_clavier in ["a","e"]:
		voyelle_memorisee=etat_clavier
		etat_systeme="/consonne_vue_voyelle_appuyee/"
		print "etat_systeme passe de /consonne_vue/ a /consonne_vue_voyelle_appuyee/"
		print "on attent la liberation du bouton pour emettre le son " + consonne_memorisee +" "+ voyelle_memorisee
	elif etat_clavier in ["b","f"]:
		consonne_memorisee=etat_clavier
		etat_systeme="/consonne_appuyee/"
		print "etat_systeme passe de /consonne_vue/ a /consonne_appuyee/ mais avec la nouvelle consonne"
		print "on attend la liberation du bouton " + consonne_memorisee + " puis l'arrivee de la voyelle" 



		

def voyelle_appuyee():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	etat_clavier=scan()
	if etat_clavier !="rien":
		print "etat_systeme reste sur /voyelle_appuyee/ " + voyelle_memorisee
	else:
		etat_systeme="/voyelle_vue/"
		print "etat_systeme passe de /voyelle_appuyee/ a /voyelle_vue/"


def voyelle_vue():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	print " On emet le son de la voyelle "+ voyelle_memorisee +" , et l'etat_systeme repasse sur /attente/ " 
	etat_systeme="/attente/"

def consonne_vue_voyelle_appuyee():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	etat_clavier=scan()
	if etat_clavier !="rien":
		print "etat_systeme reste sur /voyelle_appuyee/ " + voyelle_memorisee
	else:
		etat_systeme="/consonne_vue_voyelle_vue/"
		print "etat_systeme passe de /consonne_vue_voyelle_appuyee/ a /consonne_vue_voyelle_vue/"

def consonne_vue_voyelle_vue():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	print " On emet le son " + consonne_memorisee + " " + voyelle_memorisee +" , et l'etat_systeme repasse sur /attente/ " 
	etat_systeme="/attente/"



###########################################################
#
#   La boucle infinie commence ici
#
#
###########################################################
while (1):
	print "-------------------------------------------\ndebut de boucle: etat_systeme : " + etat_systeme
	if etat_systeme=="/attente/":
		attente()
	elif etat_systeme=="/consonne_appuyee/":
		consonne_appuyee()
	elif etat_systeme=="/voyelle_appuyee/":
		voyelle_appuyee()
	elif etat_systeme=="/voyelle_vue/":
		voyelle_vue()
	elif etat_systeme=="/consonne_vue/":
		consonne_vue()
	elif etat_systeme=="/consonne_vue_voyelle_appuyee/":
		consonne_vue_voyelle_appuyee()
	elif etat_systeme=="/consonne_vue_voyelle_vue/":
		consonne_vue_voyelle_vue()
	else:
		print "l'etat systeme "+ etat_systeme + " n'est pas pris en compte dans la boucle infinie"

	time.sleep(1)

