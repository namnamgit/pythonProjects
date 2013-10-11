# Rodrigo, 27-mar-13
# Fa;a um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

salario =  float(input('Salário: '))
reajuste = int(input('Porcentagem do aumento: '))

aumento = salario * reajuste / 100
novo_salario = salario + aumento

print('Aumento de R$%d. Seu novo salário será de R$%.2f' % (aumento, novo_salario))

input()
