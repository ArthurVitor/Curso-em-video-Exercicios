lista = [[], [], []]

esl = ''
while esl != 'N':
        esl = str(input('Deseja continuar? ')).strip().upper()[0]
        if esl == 'S':
            aluno = str(input('Digite o nome do aluno: ')).capitalize()
            lista[0].append(aluno)
            not1 = float(input('Qual a primeira nota? '))
            lista[1].append(not1)
            not2 = float(input('Qual a segunda nota? '))
            lista[2].append(not2)
        else:
            break

for c in range(0, len(lista[0])):
    print(f'Aluno(a): {lista[0][c]} media {(lista[1][c] + lista[2][c]) / 2}')


print('Deseja ver a nota de qual aluno? ')

for pos, alun in enumerate(lista[0]):
    print(f'Aluno(a) {alun} = {pos+1}')

medn = int(input('Qual aluno você escolhe? '))
print(f'Notas do aluno {medn} {lista[1][medn-1], lista[2][medn-1]}')
