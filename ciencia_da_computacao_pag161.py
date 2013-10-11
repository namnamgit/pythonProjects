print('-----------------')
print('1. Dia ensolarado')
print('2. Dia chuvoso')
print('-----------------')

condicao_dia = int(input('Dia: '))

if condicao_dia == 1:
	print('---------------------')
	print('1. Temperatura quente')
	print('2. Temperatura amena')
	print('---------------------')
	
	condicao_temp = int(input('Temperatura: '))
	
	if condicao_temp == 1:
		print('Vá nadar.')
	else:
		print('Jogue golfe.')
else:
	print('Veja televisão.')

input()
