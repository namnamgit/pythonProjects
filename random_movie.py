# This code is used to pick a random movie from 3 different dirs

import random

while True:
	a = int(input("Dir: "))
	b = int(input("Range: "))

	print ("Next movie: ", end='')
	print (random.randint(a, b))

	input("Good choice, pseudo!\n")
