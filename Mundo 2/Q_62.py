#Questão 62 do curso em vídeo
from time import sleep
'''Programa que mostra os 10 primeiros termos de uma Progressão aritmética e mais alguns caso
seja seu desejo'''

n = int(input('Insira um numero inteiro: '))
r = int(input('Insira a razão da progressão aritmética: '))
termo = n
contador = 1
total = 0
mais = 10

print('Os 10 primeiros termos de uma PA são: ')
while mais != 0:
    total += mais
    while contador <= total:
        print('{}'.format(termo),end= ' ')
        termo += r
        contador += 1

    mais = int(input('\nQuantos termos a mais você quer mostrar: '))
print('FIM!!')

