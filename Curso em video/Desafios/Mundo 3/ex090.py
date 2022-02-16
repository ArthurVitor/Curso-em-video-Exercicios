aln = {}
aln['aluno'] = str(input('Qual o nome do aluno? ')).capitalize().strip()
aln['media'] = float(input('Qual a media do aluno? '))
if aln['media'] < 7:
    aln['situaçao'] = 'Reprovado'
else:
    aln['situaçao'] = 'Aprovado'
print(f'O aluno(a) {aln["aluno"]} está com a media {aln["media"]} e foi {aln["situaçao"]}')