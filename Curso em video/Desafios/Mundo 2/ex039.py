#Recebe o ano de nascimento do usuario
ano = int(input('Digite o ano de nascimento! '))

#Calcula a idade do usuario
id = 2022 - ano

#Efetua o teste logico
if id < 18:
    print(f'Ainda faltam {18 - id} anos para você se alistar!')
elif id == 18:
    print('Está na hora de se alistar!')
else:
    print(f'Você atrasou {id - 18} anos do alistamento!')