# rodrigo, apr2513
# escreva um programa que leia dois números e que pergunte qual opera;ão você
# deseja realizar. você deve poder calcular a soma(+), subtra;ão(-), multiplica;ão(*)
# e divisão(/). exiba o resultado da opera;ão solicitada.

while True:
	num1 = int(input('Digite o primeiro número: '))
	num2 = int(input('Digite o segundo número: '))
	operacao = input('Escolha uma operacao (+, -, *, /): ')

	if operacao == '+':
		resultado = num1 + num2
		simbolo = '+'
	elif operacao == '-':
		resultado = num1 - num2
		simbolo = '-'
	elif operacao == '*':
		resultado = num1 * num2
		simbolo = '*'
	elif operacao == '/':
		resultado = num1 / num2
		simbolo = '/'

	input('[%d %s %d = %d]\n' % (num1, simbolo, num2, resultado))
