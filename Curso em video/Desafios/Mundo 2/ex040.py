#Recebe as notas do aluno
nt1 = float(input('Digite a primeira nota! '))
nt2 = float(input('Digite a segunda nota! '))

#Calcula a media
med = (nt1 + nt2) / 2

#Efetua o teste logico
if med < 5.0:
    print('Reprovado!')
elif med >= 5.0 and med <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')