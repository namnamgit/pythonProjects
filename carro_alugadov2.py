# n01, jul0513
# escreva um programa que pergunte a quantidade de km percorridos por um carro
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
# calcule o preço a pagar, sabendo que o carro custa r$ 60,00 por dia e r$ 0,15 por km rodado.

sair = True
while sair == True:
	km_percorridos = int(input('Digite a quantidade de km percorridos: '))
	qtd_dias_alugado = int(input('Digite a qtd de dias que o carro ficou alugado: '))

	valor_km = km_percorridos * 0.15
	valor_dias = qtd_dias_alugado * 60
	total_pagar = valor_km + valor_dias

	print('\n-> Valor kilometros percorridos » R$ %.2f' % valor_km)
	print('-> Valor à pagar por dias alugado » R$ %.2f' % valor_dias)
	print('-> Valor total à pagar » R$ %.2f' % total_pagar)

	sair = input('\nDeseja fazer novo cálculo? (s/n): ')
	if sair == 'n':
		sair = False
	else:
		sair = True
	print('-' * 29)
