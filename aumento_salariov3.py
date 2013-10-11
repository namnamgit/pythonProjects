# rodrigo, apr2513
# escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# para salários superiores a r$ 1.250,00 calcule um aumento de 10%. para os inferiores ou iguais, de 15%

while True:
	salario = float(input('Salário: '))

	if salario > 1250.00:
		aumento = salario * 10 / 100
		salario_atual = salario + aumento
		print('Aumento de %.2f / Salário atual: %.2f\n' % (aumento, salario_atual))

	if salario <= 1250.00:
		aumento = salario * 15 / 100
		salario_atual = salario + aumento
		print('Aumento de %.2f / Salário atual: %.2f\n' % (aumento, salario_atual))
