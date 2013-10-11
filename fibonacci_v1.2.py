#sequência de fibonacci

a, b = 0, 1

while a < 100:
	print(a, end=', ')
	a, b = a + b, a

input()
