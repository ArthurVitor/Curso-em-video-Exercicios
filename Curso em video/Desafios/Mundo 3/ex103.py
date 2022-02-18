def ficha(nome, gols):
    return print(f'O jogador: {nome} fez {gols}')



jgd = {}

jgd['nome'] = str(input('Qual o nome do jogador? '))
if jgd['nome'] == '':
    jgd['nome'] = 'desconhecido'

jgd['gols'] = str(input('Quantos jogos o jogador fez? '))
if jgd['gols'] == '':
    jgd['gols'] = '0'

ficha(jgd['nome'], jgd['gols'])