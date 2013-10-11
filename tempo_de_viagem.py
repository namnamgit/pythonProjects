# rodrigo, mar2813
# escreva um programa que calcule o tempo de uma viagem de carro.
# pergunte a distância a percorrer e a velocidade média esperada para a viagem.

while True:
	distancia = int(input("Distância a percorrer: "))
	velocidade_media = int(input("Velocidade média esperada: "))

	viagem = distancia / velocidade_media
	decimal = viagem % 1 * 60 #pega a parte decimal das horas e converte para minutos
	
	input('Tempo aproximado de viagem: %dh%dmin\n' % (viagem, decimal))
