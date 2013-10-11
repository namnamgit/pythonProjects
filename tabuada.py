n = int(input('Tabuada do: '))
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
num = 1

print('')
while inicio <= fim:
	print('%2d x %d = %d' % (inicio, n, inicio * n))
	inicio = inicio + 1

input('\nDone.')
