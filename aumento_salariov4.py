salario = float(input('Digite o valor do salário: '))
aumento_porcento = int(input('Aumento de (%): '))

aumento = salario * aumento_porcento / 100
novo_salario = salario + aumento

print('\nSalário antigo: %.2f\nAumento de: %d por cento\nNovo salário: %.2f' % (salario, aumento_porcento, novo_salario))
input()
