# rodrigo, apr0713
# escolher filme
import random

while True:
	a = int(input("First: "))
	b = int(input("Second: "))

	print ("Next movie: ", end='')
	print (random.randint(a, b))

	input("Good choice, pseudo!\n")
