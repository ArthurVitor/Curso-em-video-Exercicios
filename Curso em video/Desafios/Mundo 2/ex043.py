#Recebe o peso e altura da pessoa
ps = int(input('Digite seu peso em kg: '))
alt = float(input('Digite sua altura em metros: '))

#Calcula o imc
imc = ps / (alt * alt)

#Efetua o teste logico
if imc < 18.5:
    print('Abaixo do peso! ')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade morbida')