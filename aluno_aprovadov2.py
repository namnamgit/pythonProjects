# n01, jun3013
# escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
# para ser aprovado, todas as médias do aluno devem ser maiores que 7.
# considere que o aluno cursa apenas três matérias e que a nota de cada uma está
# armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3

materia1 = int(input('Matemática: '))
materia2 = int(input('Física: '))
materia3 = int(input('Biologia: '))

soma_notas = materia1 + materia2 + materia3
media_notas = soma_notas / 3

if media_notas > 7:
	print('-> Aluno aprovado com média %d' % media_notas)
else:
	print('-> Aluno reprovado com média %d' % media_notas)

input()
