#Questão 67 do Curso em video
''' Programa que pede para ser inserido um numero positivo e devolve a sua tabuada, só para quando
o numero digitado é negativo '''
from time import sleep

n = 0

while True:
    n = int(input('Insira um numero inteiro positivo(Para parar insira um negativo): '))
    if n < 0:
        break
    print('Gerando tabuada do numero {}'.format(n))
    sleep(1)
    for i in range(1, 11):
        print('{} * {} = {}'.format(n, i, n * i))
    
        

print('O numero inserido é negativo!')