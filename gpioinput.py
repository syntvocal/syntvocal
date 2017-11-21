import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN)
		GPIO.
#while True:
input_value = GPIO.input(18)
if input_value == False:
	print("Le bouton vient d etre enfonce.")
	while input_value == False:
		input_value = GPIO.input(18)
