num1 = int(input('Digite o primeiro número: ')) #4
num2 = int(input('Digite o segundo número: ')) #3
cont = 1
texto1, texto2 = str(num1), str(num2)

while cont < num1:
	cont = cont + 1
	texto2 = texto2 + ' + ' + str(num2)

cont = 1 # reinicia variável contador
while cont < num2:
	cont = cont + 1
	texto1 = texto1 + ' + ' + str(num1)

input('%d * %d = %s or %s' % (num1, num2, texto1, texto2))
