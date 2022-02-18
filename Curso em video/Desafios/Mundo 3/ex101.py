import datetime

def voto(id=0):
    idade = datetime.datetime.now().year - id
    if idade < 18:
        return "Negado"
    elif idade >= 18 and idade < 65:
        return  "Obrigatorio"
    elif idade >= 65:
        return  "Opicional"


idade = int(input('Ano de nascimento: '))
print(f'Seu voto é {voto(idade)}')