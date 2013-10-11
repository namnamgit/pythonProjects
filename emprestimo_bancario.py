# rodrigo, may0313
# escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# o programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# o valor da presta;ão mensal não pode ser superior a 30% do salário.
# calcule o valor da presta;ão como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

print('[APROVACAO DE EMPRESTIMO]\n')
valor_casa = float(input('Valor da casa: '))
salario_cliente = float(input('Salário do cliente: '))
qtd_anos = int(input('Quantidade de anos a pagar: '))

qtd_meses = qtd_anos * 12
prest_mensal = valor_casa / qtd_meses
test_emprestimo = salario_cliente * 30 / 100

if prest_mensal < test_emprestimo:
	print('Valor da casa: %.2f / Prestacao mensal: %.2f\nEmpréstimo aprovado.' % (valor_casa, prest_mensal))
else:
	print('Valor da casa: %.2f / Prestacao mensal: %.2f\nEmpréstimo negado.' % (valor_casa, prest_mensal))

input()
