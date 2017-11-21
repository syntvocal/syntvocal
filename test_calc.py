
Skip to content
This repository

    Pull requests
    Issues
    Marketplace
    Explore

    @vyledar

1
0

    0

syntvocal/syntvocal
Code
Issues 0
Pull requests 0
Projects 0
Wiki
Insights
Settings
syntvocal/test_clav.py
69f1164 6 hours ago
@bernardgibert bernardgibert creation du fichier test_clav.py
90 lines (81 sloc) 3.9 KB
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#
#  MINI CLAVIER 4 TOUCHES POUR DEBUTER
#
#      A-----E------<-------GPIO4            
#      |     |              Blanc
#      |     |
#      B-----F------<-------GPIO22
#      |     |              Rouge
#      |     |   
#      +--------------[ 10K ]-----|
#      |     |                    +---3.3V
#      |     +--------[ 10k ]-----|  jaune
#      V     V   
#      |     |   
#      |     |   
#      |   GPIO21  
#      |    Violet
#   GPIO17 
#    vert    
#

GPIO.setup(17, GPIO.IN)   # toutes les colonnes initialisees en entree
GPIO.setup(21, GPIO.IN)

GPIO.setup(4, GPIO.OUT) # toutes les lignes initialisees en sortie
GPIO.setup(22, GPIO.OUT)

GPIO.output(4,1)        # toutes les lignes initialisees a 1
GPIO.output(22,1)       # 

print "Debut: les sorties GPIO 4 (fil blanc) et GPIO 22 (fil rouge) sont mises à 1"
print "Cela signifie qu'elles sont au niveau 3.3V. Mesurons la tension à leur niveau"
print "entre le fil blanc (GPIO4) et le fil jaune (3.3V) on doit mesurer zero ou presque"
blanc = raw_input("Est ce le cas ? O/N")
print "entre le fil rouge (GPIO22) et le fil jaune (3.3V) on doit mesurer zero ou presque"
jaune = raw_input("Est ce le cas ? O/N")
if blanc=="N":
	print "debrancher le fil blanc côté clavier et refaire la mesure. Si le résultat attendu"
	print "n est pas correct, brancher le fil blanc sur une autre sortie du GPIO"
	print "et remplacer dans test_clav.py GPIO4 par GPIOx"
if jaune=="N":
	print "debrancher le fil jaune côté clavier et refaire la mesure. Si le résultat attendu"
	print "n est pas correct, brancher le fil blanc sur une autre sortie du GPIO"
	print "et remplacer dans test_clav.py GPIO22 par GPIOx"
GPIO.output(4,0)        
print "la sortie GPIO4 a été mise à zéro- On doit constater 3.3V entre le blanc et le jaune"
blanc_zero = raw_input("Est ce le cas ? O/N")
if blanc_zero=="N":
	print "essayer une autre sortie du GPIO, modifiez test_clav.pi et re essayez"
GPIO.output(22,0)        
print "la sortie GPIO22 a été mise à zéro- On doit constater 3.3V entre le rouge et le jaune"
blanc_zero = raw_input("Est ce le cas ? O/N")
if blanc_zero=="N":
	print "essayer une autre sortie du GPIO, modifiez test_clav.pi et re essayez"
print "Les entrées GPIO17 (fil vert) et GPIO21 (fil violet) sont ramenées à 3.3V via leurs"
print "résistances de pullup respective si aucun bouton n'est enfoncé."
print "On doit alors mesurer 0V entre le jaune et le vert et entre le jaune et le violet"
entrees = raw_input("Est ce le cas ? O/N")
if entrees=="N":
	print "confirmez le probleme indépendamment du clavier (sortir fils vert et violet du clavier et re mesurer)"
print "Si tout est OK jusqu'ici, les sorties sont à zéro et les entrées sont à 1"
print "C'est l'etat du clavier avec aucune touche enfoncée."
GPIO.output(4,0)        
GPIO.output(22,1)        
print "Maintenant la sortie GPIO4 (fil blanc) està 0 et la sortie GPIO22 (fil rouge) est a 1"
print "on doit observer (si on appuie sur A) l'entree GPIO17 (fil vert) passer à zero" 	
test_A = raw_input("Est ce le cas ? O/N")
if test_A=="N":
	print "debrancher le fil vert coté GPIO et tester à l'ohmmetre entre le fil blanc et le fil vert" 	
	print "si on appuie sur A , l'ohmmetre doit mesurer 0" 	
print "on doit observer (si on appuie sur E) l'entree GPIO21 (fil violet) passer à zero" 	
test_E = raw_input("Est ce le cas ? O/N")
if test_E=="N":
	print "debrancher le fil violet coté GPIO et tester à l'ohmmetre entre le fil blanc et le fil vert" 	
	print "si on appuie sur E , l'ohmmetre doit mesurer 0" 	
GPIO.output(4,1)        
GPIO.output(22,0)        
print "Maintenant c'est la sortie 22 qui est à zero et la sortie 4 qui est à 1"
print "Les fils vert ou violet passent à 0 si on appuie sur B ou F "
test_E = raw_input("Est ce le cas ? O/N")
if test_E=="N":
	print "Attention, j'arrive" 	


GPIO.cleanup() # on remet GPIO a zero (si on veut changer les modes entrees/sorties plus tard)
 

    © 2017 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    API
    Training
    Shop
    Blog
    About

