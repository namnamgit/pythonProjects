while True:
	minutos = int(input('Quantos minutos você utilizou este mês: '))
	if minutos < 200:
		valor = 0.20
	else:
		if minutos < 400:
			valor = 0.18
		else:
			valor = 0.15

	input('Valor do minuto: %.2f / Valor a pagar: %.2f\n' % (valor, minutos * valor))
