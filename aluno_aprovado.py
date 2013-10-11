# rodrigo, mar2213
# aluno aprovado

matéria1 = int(input("Matemática: "))
matéria2 = int(input("Geografia: "))
matéria3 = int(input("História: "))

média = (matéria1 + matéria2 + matéria3) / 3

if média >= 7:
	print("\nAluno aprovado com média:", média)
else:
	print("\nAluno reprovado com média:", média)

input("\nFim.")
