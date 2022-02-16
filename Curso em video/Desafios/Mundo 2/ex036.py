#Entrada de dados
clr = float(input('Digite o valor da casa: ')) #Valor da casa
slr = float(input('Qual seu salario? ')) #Salario
tmp = int(input('Em quanto tempo pretende pagar a casa? ')) #Tempo de financiamento

#Conversão de anos para meses/Valor das parcelas
tmp = tmp * 12
pg = clr / tmp #Calcula o valor das parcelas

#Verifica se o pagador está apto a receber o financiamento
if pg > slr * 0.30:
    print('Seu financiamento foi negado pois o valor da parcela é superior a 30% do seu salario! ')
else:
    print('Financiamento aprovado! ')