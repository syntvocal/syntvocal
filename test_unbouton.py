if input_value == False:
	print("Le bouton vient d etre enfonce. ")
	while input_value == False:
		imput_value = GPIO.input(12)
		
		
		import RPi.GPIO as GPIO
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(12, GPIO.IN)
		while True:
			input_value = GPIO.input(12)
			  if input_value == False:
			  print("Le bouton vient d etre enfonce.")
			  while input_value == False:
				input_value = GPIO.input(12)
