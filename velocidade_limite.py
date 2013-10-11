# rodrigo, apr0813
# escreva um programa que pergunte a velocidade do carro de um usuário.
# caso ultrapasse 80km/h, exiba uma msg dizendo que o usuário foi multado.
# nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 80.

while True:
	velocidade = int(input('Velocidade do carro em km: '))
	multa = 5 * (velocidade - 80)

	if velocidade > 80:
		print('Você ultrapassou a velocidade limite.')
		print('Você será multado em R$%.2f\n.' % multa)
	else:
		print('Você passou abaixo da velocidade limite.\n')
