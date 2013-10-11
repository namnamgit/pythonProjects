# Rodrigo, 27-mar-13
# Escreva um programa que leia a quantidade de dias, horas,
# minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

total_em_segundos = ((dias * 24) * 60**2) + (horas * 60**2) + minutos * 60 + segundos

print("Total: %d segundos" %total_em_segundos)

input()
