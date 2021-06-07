#Questão 42 do curso em vídeo
from time import sleep

'''Verificação dos lados de um triangulo e classificação desse mesmo''' 

t1 = float(input('Qual o valor do primeiro segmento reta:  '))
t2 = float(input('Qual o valor do segundo segmento de reta: '))
t3 = float(input('Qual o valor do terceiro segmento de reta: '))

if (t1 + t2 > t3) and (t1 + t3 > t2) and (t2 + t3 > t1):
    print('Os segmentos de reta formam um triangulo!')
    if (t1 != t2) and (t1 != t3) and (t2 != t3):
        print('O triangulo formado é escaleno!')
    elif t1 == t2 and t2 == t3:
        print('O triangulo é equilatero!')
    else:
        print('O triangulo formado é isósceles!')
else:
    print('Os segmentos de reta não formam um triangulo!')

