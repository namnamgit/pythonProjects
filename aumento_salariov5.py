# n01, jul0513
# escreva um programa que calcule o aumento de um salário.
# ele deve solicitar o valor do salário e a percentagem do aumento.
# exiba o valor do aumento e do novo salário.

print('[AUMENTO DE SALÁRIO]')
salario = float(input('Digite o salário: '))
percentagem_aumento = int(input('Digite a percentagem do aumento: '))

valor_aumento = salario * percentagem_aumento / 100
salario_atual = salario + valor_aumento

print('\n-> Salário anterior: R$ %.2f' % salario)
print('--> Valor do aumento: R$ %.2f' % valor_aumento)
print('---> Salário atual: R$ %.2f' % salario_atual)

input()
