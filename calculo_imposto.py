salario = float(input('Digite o salário para cálculo do imposto: '))
base = salario
imposto = 0
if base > 3000:
	imposto = imposto + ((base - 3000) * 0.35)
	base = 3000
if base > 1000:
	imposto = imposto + ((base - 1000) * 0.20)
input('Salário: R$%.2f / Imposto a pagar: R$%.2f' % (salario, imposto))
