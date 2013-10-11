#sequência de fibonacci

a, b, c = 0, 1, 0

while a < 100:
	print(a, end=', ')
	c = a
	a = a + b
	b = c

input()
