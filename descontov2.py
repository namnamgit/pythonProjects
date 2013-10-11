# n01, jul0513
# faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# exiba o valor do desconto e o preço a pagar.

sair = True
while sair == True:
	valor_mercadoria = float(input('Digite o valor da mercadoria: '))
	percentual_desconto = int(input('Digite o percentual de desconto: '))

	valor_desconto = valor_mercadoria * percentual_desconto / 100
	valor_mercadoria_final = valor_mercadoria - valor_desconto

	print('\n-> Valor do desconto - R$ %.2f' % valor_desconto)
	print('--> Valor à pagar - R$ %.2f' % valor_mercadoria_final)
	sair = input('\nDeseja fazer novo cálculo? (s/n): ')
	if sair == 'n':
		sair = False
	else:
		sair = True
	print('-' * 29)
