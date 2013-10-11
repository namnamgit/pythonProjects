# rodrigo, apr1013
# escreva um programa que leia três números e que imprima o maior e o menor

while True:
	numero1 = int(input('Digite o primeiro número: '))
	numero2 = int(input('Digite o segundo número: '))
	numero3 = int(input('Digite o terceiro número: '))

	if numero1 > numero2 and numero1 > numero3:
		print('%d é o maior número.' % numero1)
	if numero2 > numero1 and numero2 > numero3:
		print('%d é o maior número.' % numero2)
	if numero3 > numero1 and numero3 > numero2:
		print('%d é o maior número.' % numero3)

	if numero1 < numero2 and numero1 < numero3:
		print('%d é o menor número.\n' % numero1)
	if numero2 < numero1 and numero2 < numero3:
		print('%d é o menor número.\n' % numero2)
	if numero3 < numero1 and numero3 < numero2:
		print('%d é o menor número.\n' % numero3)
