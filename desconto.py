# rodrigo, mar2713
# Fa;a um programa que solicite o pre;o de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o pre;o a pagar.


while True:
	valor	 = float(input("Valor: "))
	desconto = int(input("Percentual de desconto: "))

	valor_do_desconto = valor * desconto / 100
	novo_valor = valor - valor_do_desconto
	print("Desconto de R$%.2f - Valor a pagar: R$%.2f\n" % (valor_do_desconto, novo_valor))
