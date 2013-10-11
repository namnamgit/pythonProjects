# rodrigo, apr0413
# pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# calcule o preço, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

print('ALUGUEL DE CARROS\n')
while True:
	dias = int(input('Quantidade de dias: '))
	km_percorridos = int(input('km percorridos: '))

	valor = dias * 60 + km_percorridos * 0.15
	print('Total a pagar: R$%.2f\n' % valor)
