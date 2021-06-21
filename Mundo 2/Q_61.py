#Questão 61 do curso em vídeo

'''Programa que mostra os 10 primeiros termos de uma Progressão aritmética'''

n = int(input('Insira um numero inteiro: '))
r = int(input('Insira a razão da progressão aritmética: '))
contador = 1

print('Os 10 primeiros termos de uma PA com razão igual a {} são: {}'.format(r, n), end= ' ')
while contador != 10:
    print('{}'.format(n + contador * r), end= ' ')
    contador += 1
