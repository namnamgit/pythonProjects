# rodrigo, may1413
# escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# exiba os valores mês a mês para os 24 primeiros meses.
# escreva o total ganho com juros no período.

contador = 1
juros = float(input('Porcentagem de juros: '))
deposito_inicial = float(input('Valor do depósito inicial: '))
deposito_mais_juros = deposito_inicial

while contador <= 24:
	deposito_mais_juros = deposito_mais_juros + (deposito_mais_juros * juros / 100)
	apenas_juros = deposito_mais_juros - deposito_inicial
	print('%do mês: %.2f' % (contador, deposito_mais_juros))
	contador = contador + 1

input('\nSeu dinheiro rendeu R$%.2f em juros.' % apenas_juros)
