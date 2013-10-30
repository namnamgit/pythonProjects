#sequência de fibonacci

a, b = 0, 1

while a < 10000000000000900000:
	print(a, end=', ')
	a, b = a + b, a

input()
