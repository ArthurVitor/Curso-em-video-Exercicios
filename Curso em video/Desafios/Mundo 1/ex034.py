sal = int(input('Quanto é o seu salario? '))
if sal > 1250:
    print(f'Seu aumento será de 10% seu novo salario com aumento será de R$ {(sal * 0.10) + sal}')
else:
    print(f'Seu aumento será de 15% seu novo salario com aumento será de R$ {(sal * 0.15) + sal}')