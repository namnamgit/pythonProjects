# rodrigo, apr0413
# calcular a redução do tempo de vida de um fumante.
# pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# considere que um fumante perde 10 min de vida a cada cigarro, calcule quantos dias
# de vida um fumante perderá. exiba o total em dias.

qtd_cigarros = int(input('Quantidade de cigarros fumados por dia: '))
anos_fumando = int(input('Quantos anos você já fumou: '))

anos2dias = anos_fumando * 365
# converte anos para dias

reducao_de_vida = qtd_cigarros * 10 / 1440 * anos2dias
# qtd_cigarros * 10 / 1440 converte minutos para dias

input('Você perdeu o equivalente à %d dias fumando.' % reducao_de_vida)
