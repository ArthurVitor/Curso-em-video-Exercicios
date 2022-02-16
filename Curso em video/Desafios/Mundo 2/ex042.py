#Recebe os lados do triangulo
s1 = int(input('Digite a primeira reta: '))
s2 = int(input('Digite a segunda reta: '))
s3 = int(input('Digite a terceira reta: '))

#Efetua o teste logico
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
     print('Formam um triangulo!')
     if s1 == s2 == s2:
          print('EQUTLATERO!')
     elif s1 != s2 != s3 != s1:
          print('ESCALENO!')
     else:
          print('ISOSCELES')
else:
     print('Não formam um triangulo!')
