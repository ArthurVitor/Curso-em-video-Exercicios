def nota():
    geral = {'aluno': [], 'nota': []}

    esl = ''
    while esl != 'N':
        esl = str(input('Deseja continuar? ')).strip().upper()[0]
        if esl == 'S':
            geral['aluno'].append(str(input('Digite o nome do aluno: ')))
            geral['nota'].append(float(input('Qual a nota do aluno? ')))
            ntes = ''
            while ntes != 'N':
                ntes = str(input('Deseja adicionar mais uma nota? ')).strip().upper()[0]
                if ntes == 'S':
                    geral['nota'].append(float(input('Qual a nota do aluno? ')))
    print(f'Existem um total de {len(geral["nota"])} cadastradas, \n'
          f'A maior nota foi {max(geral["nota"])} \n'
          f'A menor nota foi {min(geral["nota"])} \n'
          f'A média da turma foi de {(sum(geral["nota"])) / len(geral["nota"])}')



#Progama principal
geral = {'aluno':[],'nota':[]}

if __name__ == '__main__':
    nota()