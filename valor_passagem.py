# rodrigo, apr1013
# escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# calcule o pre;o da passagem, cobrando r$0,50 por km para viagens de até 200km e r$0,45 para viagens mais longas.

while True:
	distancia = int(input('Distância que deseja percorrer: '))
	valor1 = 0.45
	valor2 = 0.50

	if distancia > 200:
		passagem = distancia * valor1
		valor = valor1
	else:
		passagem = distancia * valor2
		valor = valor2

	input('Valor por km: R$%.2f / Valor da passagem: R$%.2f\n' % (valor, passagem))
