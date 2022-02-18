jgd = {}
prt = []
jgd['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jgd["nome"]} jogou? '))
for c in range(0, tot):
    prt.append(int(input(f'Quantas gol na partida {c}: ')))
jgd['gols'] = prt[:]
print(jgd)
print(prt)
print(f'Fez um total de {sum(jgd["gols"])} gols')