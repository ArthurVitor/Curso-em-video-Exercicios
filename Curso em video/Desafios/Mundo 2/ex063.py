num = int(input("Digite qualquer numero:"))
n1, n2 = 0, 1
summ = 0

if num <= 0:
    print('Coloque um numero maior que 0: ')
else:
    for i in range (0, num):
       print(summ, end=" ")
       n1 = n2
       n2 = summ
       summ = n1 + n2