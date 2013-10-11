# n01, jul0513
# escreva um programa que calcule o tempo de uma viagem de carro.
# pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia_percorrer = int(input('Digite a distância a percorrer: '))
velocidade_media = int(input('Digite a velocidade média prevista: '))

tempo_de_viagem = distancia_percorrer / velocidade_media
decimal = tempo_de_viagem % 1 * 60 # pega a parte decimal do resultado e converte para minutos

print('Tempo de viagem previsto: %dh%dmin' % (tempo_de_viagem, decimal))

input()
