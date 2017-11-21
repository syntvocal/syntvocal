import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)



GPIO.setup(4, GPIO.IN)   
GPIO.setup(22, GPIO.IN)

GPIO.setup(17, GPIO.OUT) 
GPIO.setup(21, GPIO.OUT)

GPIO.output(17,1)        
GPIO.output(21,1)       

clv={}         


clv[4,17]="A"
clv[4,21]="E"
clv[22,17]="B" 
clv[22,21]="F"

res="rien"     


for x in [4,22]:   

    GPIO.output(4,1)  
    GPIO.output(22,1) 
    GPIO.output(x,0)  
	
	   
    for y in [17,21]: 
        ligne=GPIO.input(y) 
        if ligne==1:  
            col=x   
            lig=y
           
       
            res= str(clv[x,y])  
            
            
print res   



GPIO.cleanup() 
 
