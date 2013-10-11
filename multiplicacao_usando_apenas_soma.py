num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
cont1 = cont2 = 1
texto1, texto2 = str(num1), str(num2)

while cont1 < num1:
	cont1 = cont1 + 1
	texto2 = texto2 + ' + ' + str(num2)
	while cont2 < num2:
		cont2 = cont2 + 1
		texto1 = texto1 + ' + ' + str(num1)

input('%d * %d = %s or %s' % (num1, num2, texto1, texto2))
