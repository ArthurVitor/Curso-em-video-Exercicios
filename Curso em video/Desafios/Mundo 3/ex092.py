import datetime

dds = {}
dds['nome'] = str(input('Digite seu nome: '))
nsc = int(input('Ano de nascimento: '))
dds['idade'] = datetime.datetime.now().year - nsc
dds['ctps'] = int(input('Numero da carteira (0 caso não tenha): '))
if dds['ctps'] != 0:
    dds['contr'] = int(input('Ano de contratação: '))
    dds['sal'] = float(input('Salario: '))
    dds['apo'] = (dds['contr'] + 35) - datetime.datetime.now().year
print(dds)