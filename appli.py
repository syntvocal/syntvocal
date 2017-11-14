
#####################################################
#v
# Au demarrage du programme, on regarde sur quelle adresse IP
# le programme s'execute. Si c'est sur 192.168.10.50, alors
# on est sur le Raspberry et la fonction scan() va retourner
# l'etat du GPIO et donc l'etat du clavier definitif
# Si on n'est pas sur le raspberry, alors la fonction scan()
# effectue un raw_input pour simuler la touche enfoncee.
# On peut ainsi faire du debug en pas a pas dans la machine d'etat;
#
#####################################################



import os
on_raspberry=False
which_ip = os.popen("ifconfig | grep \"192.168.1\"").read()
print which_ip
if '192.168.10.50' in which_ip:
	on_raspberry=True
	print 'Le programme s execute sur le raspberry'
else:
	print 'Le programme ne s\'execute PAS sur le raspberry'
#########################################################
def scan():    # lafonction scan va indiquer l'etat du clavier: "a", "e", "b", "f" ou "rien"
	global on_raspberry
	if  on_raspberry==False : # Sous linux on debugue
		etat_clavier = raw_input("scan ?")
		if etat_clavier =='':
			etat_clavier="rien"
		
		permis = ['rien', 'a', 'e', 'b', 'f']
		if etat_clavier not in permis:
			print "seules les lettres a, e, b, f sont autorisees"
	else:
		print "placer ici le programme issu de calculette2.py lisant le GPIO"
		etat_clavier="rien"
	return etat_clavier
#########################################################
#
#  La machine d'etats. 
# Au debut de chaque tour dans la boucle infinie, l etat systeme
# va etre lu. pour chaque etat system vu, correspond une fonction
# a executer. Dans cette fonction, l'etat systeme peut changer ou non
# comme dans une machine a laver.
# Au depart, on definit les variables correspondant aux donnees a memoriser
# (etat_systeme, etat_clavier, consonne_memorisee, voyelle memorisee)
#Ci apres sont les definitions des fonctions correspondant a chaque etat systeme
#Ces fonctions doivent declarer les donnees en global pour pouvoir y acceder.
#
#
#########################################################

import time

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
	print "etat_clavier:" + str(etat_clavier)
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
		print "etat_systeme passe de  " + etat_systeme + " a /consonne_vue_voyelle_appuyee/"
		print "on attent la liberation du bouton pour emettre le son " + consonne_memorisee +" "+ voyelle_memorisee
		etat_systeme="/consonne_vue_voyelle_appuyee/"
	elif etat_clavier in ["b","f"]:
		consonne_memorisee=etat_clavier
		print "etat_systeme passe de  " + etat_systeme + " a /consonne_appuyee/ mais avec la nouvelle consonne"
		print "on attend la liberation du bouton " + consonne_memorisee + " puis l'arrivee de la voyelle" 
		etat_systeme="/consonne_appuyee/"



		

def voyelle_appuyee():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	etat_clavier=scan()
	print "etat_clavier:" + str(etat_clavier)
	if etat_clavier !="rien":
		print "etat_systeme reste sur " + etat_systeme + " " + voyelle_memorisee
	else:
		print "etat_systeme passe de " + etat_systeme + " a /voyelle_vue/"
		etat_systeme="/voyelle_vue/"


def voyelle_vue():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	print "etat_clavier:" + str(etat_clavier)
	print " On emet le son de la voyelle "+ voyelle_memorisee +" , et l'etat_systeme repasse sur /attente/ " 
	etat_systeme="/attente/"

def consonne_vue_voyelle_appuyee():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	etat_clavier=scan()
	print "etat_clavier:" + str(etat_clavier)
	if etat_clavier !="rien":
		print "etat_systeme reste sur " + etat_systeme 
	else:
		print "etat_systeme passe de " + etat_systeme + " a /consonne_vue_voyelle_vue/"
		etat_systeme="/consonne_vue_voyelle_vue/"

def consonne_vue_voyelle_vue():
	global etat_systeme
	global voyelle_memorisee
	global consonne_memorisee
	print "etat_clavier:" + str(etat_clavier)
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

	time.sleep(1) # Pendant toute la duree du debug, on arrete chaque boucle pendant 1 seconde pour eviter
	# d'etre inonde de messages sur une boucle defectueuse.

