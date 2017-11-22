#
#    UTILISEZ LES TABULATIONS POUR INDENTATION
#     LES RESISTANCES PULLUP TOUJOURS SUR LES ENTREES
#
#             |----+----------- 3.3V
#             |    |            jaune
#            10k  10k
#             |    |
#  A-----E----+----|--------26
#  |     |         |        blanc
#  |     |         |
#  B-----F---------+--------24
#  |     |                  rouge
#  |     |
#  23     22
#  vert   violet
#

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(24,GPIO.IN)
GPIO.setup(26,GPIO.IN)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

clv={}
clv[23,26]="A"
clv[23,24]="B"
clv[22,26]="E"
clv[22,24]="F"

res="rien"
for x in [22,23]
	GPIO.output(22,1)
	GPIO.output(23,1)
	GPIO.output(x,0)
		for y in [24,26]
			ligne=GPIO.input(y)
			if ligne==0:
				res=str(clv[x,y])
print res
GPIO.cleanup()





 

