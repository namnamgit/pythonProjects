# n01, jun3013
# escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
# considere que pagam imposto pessoas cujo salário é maior que r$ 1200.

salario = float(input('Digite o seu salário: '))

if salario > 1200:
	print('-> Você deve pagar imposto!')
else:
	print('-> Não é necessário pagar imposto!')

input('\nFim.')
