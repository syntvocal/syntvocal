import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#
#  MINI CLAVIER 4 TOUCHES POUR DEBUTER
#
#      A-----E--------------GPIO4            
#      |     |              Blanc
#      |     |
#      B-----F--------------GPIO22
#      |     |              Rouge
#      |     |   
#      |   GPIO27  
#      |    Violet
#   GPIO17 
#    vert    
#

GPIO.setup(17, GPIO.IN   # toutes les colonnes initialisees en entree
GPIO.setup(27, GPIO.IN)

GPIO.setup(4, GPIO.OUT) # toutes les lignes initialisees en sortie
GPIO.setup(22, GPIO.OUT)

GPIO.output(4,1)        # toutes les lignes initialisees a 1
GPIO.output(22,1)       # (ces 2 instructions sont inutiles: pourquoi?)

clv={}         # On definit la variable tableau clv (vide pour l'instant)

# on remplit les cases du tableau
clv[4,17]="A"
clv[4,27]="E"
clv[22,17]="B" 
clv[22,27]="F"

res="rien"     # on initialise la valeur du resultat (si aucune touche
               # n'est appuyee)

for x in [4,22]:   # boucle sur les sorties (les lignes)

    GPIO.output(4,1)  # on remet toutes les sorties a 1 (x a pu mettre 0
    GPIO.output(22,1) # lors d'un precedent passage dans la boucle
    GPIO.output(x,0)  # on met a 0 la sortie correspondant a x
	# la boucle exterieure est prete: toutes les lignes sont a 1 sauf celle
	# correspondant a x
        
    for y in [17,27]:   #pour chaque ligne: boucle sur les entrees (les colonnes)
        ligne=GPIO.input(y) #la variable "ligne" lit la valeur de la ligne y
        if ligne==1:  # si on lit 1, c'est que le bouton de la colonne est appuye
            col=x   # on enregistre ligne et colonne du bouton qui est appuye
            lig=y
           # print "col="+str(x) # on ecrit la colonne trouvee
           # print "lig="+str(y)
           # print str(clv[x,y])
       
            res= str(clv[x,y])  # si e résultat n'est pas "rien", on lit dans la
                                # la table "clv" la touche enfoncee

print res   # apres la sortie complete des 2 boucles, on affiche le resultat



GPIO.cleanup() # on remet GPIO a zéro (si on veut changer les modes entrees/sorties plus tard)
 
