while True:
	num1 = int(input('Digite o primeiro número: '))
	num2 = int(input('Digite o segundo número: '))
	num1_sup = resto = num1
	acum = 0

	while num1 >= num2:
		acum = acum + 1
		num1 = num1 - num2
		resto = resto - num2

	input('%d / %d = %d [Resto: %d]' % (num1_sup, num2, acum, resto))
