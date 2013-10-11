# n01, jul0513
# escreva um programa que leia a quantidade de dias, h, m e s do usuário.
# calcule o total em segundos.

days = int(input('Type the amount of days: '))
hours = int(input('Type the amount of hours: '))
minutes = int(input('Type the amount of minutes: '))
seconds = int(input('Type the amount of seconds: '))

d2seconds = days * (24 * 60 * 60) # conversions to seconds
h2seconds = hours * (60 * 60)
m2seconds = minutes * 60

total_in_seconds = d2seconds + h2seconds + m2seconds + seconds

print('-> The total amount in seconds is %d.' % total_in_seconds)

input()
