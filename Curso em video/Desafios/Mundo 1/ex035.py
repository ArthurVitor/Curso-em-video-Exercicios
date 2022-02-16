s1 = int(input('Digite a primeira reta: '))
s2 = int(input('Digite a segunda reta: '))
s3 = int(input('Digite a terceira reta: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
     print('Formam um triangulo!')
else:
     print('Não formam um triangulo!')