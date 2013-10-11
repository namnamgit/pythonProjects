# rodrigo, may0313
# escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# pergunte a quantidade de kwh consumidas e o tipo de instalação:
# r para residências, i para indústrias e c para comércios.
# calcule o preço a pagar de acordo com a tabela...

while True:
	kwh_consumidos = int(input('Quantidade de kWh consumidos: '))
	print('\n<Escolha o tipo de instalacao>')
	tipo_instalacao = input('r = residência / i = indústria / c = comércio: ')

	if tipo_instalacao == 'r':
		if kwh_consumidos <= 500:
			valor_pagar = kwh_consumidos * 0.40
		else:
			valor_pagar = kwh_consumidos * 0.65
	elif tipo_instalacao == 'i':
		if kwh_consumidos <= 5000:
			valor_pagar = kwh_consumidos * 0.55
		else:
			valor_pagar = kwh_consumidos * 0.60
	elif tipo_instalacao == 'c':
		if kwh_consumidos <= 1000:
			valor_pagar = kwh_consumidos * 0.55
		else:
			valor_pagar = kwh_consumidos * 0.60

	input('\nTipo de instalação: %s / kWh: %d / Valor a pagar: %.2f\n' % (tipo_instalacao, kwh_consumidos, valor_pagar))
