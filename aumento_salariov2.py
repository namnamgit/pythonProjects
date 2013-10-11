# rodrigo, apr1013
# escreva um programa que pergunte o salário do funcionário e calcule
# o valor do aumento. para salários superiores a r$ 1.250,00, calcule
# um aumento de 10%. para os inferiores ou iguais, de 15%.

while True:
	salario = float(input('Digite o seu salário: '))
	base = salario

	if base > 1250:
		aumento = base * 10 / 100
		salario_aumento = base + aumento
	if base <= 1250:
		aumento = base * 15 / 100
		salario_aumento = base + aumento

	input('Salário: %.2f / Aumento: %.2f / Novo salário: %.2f\n' % (salario, aumento, salario_aumento))
