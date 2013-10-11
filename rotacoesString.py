# rodrigo, apr0713
# leia um string e imprima suas possíveis rota;ões
# ex: senac -> senac, enacs, nacse, acsen, csena

def rotacoesString():
	texto = input('Digite uma palavra: ')
	tamanho_texto = len(texto)
	print(texto, tamanho_texto)

	while 