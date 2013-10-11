def pol2cm(polegada):
	#polegada = int( input('Polegadas: '))
	centimetro = polegada * 2.54
	print('Centimetros: %.2f' % centimetro)

def pe2metro(pe):
	#pe = int( input('Pés: '))
	metro = pe * 0.3048
	print('Metros: %.2f' % metro)

def miles2km(miles):
	#miles = int( input('Milhas: '))
	km = miles * 1609.33
	print('km: %d' % km)

def celsius2fahr(celsius):
	#celsius = int( input('Celsius: '))
	fahrenheit = 9 * celsius / 5 + 32
	print('Fahrenheit: %d' % fahrenheit)
