#Questão 63 do curso em vídeo

'''Programa que mostra os n primeiros numeros de uma sequencia de fibonacci'''

n = int(input('Insira a quantidade de numeros a serem mostrados da sequência de fibonacci: '))

n1 = 0
n2 = 1

contador = 0

print('{}-{}'.format(n1,n2),end='')
while contador < n - 2:
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    print('-{}'.format(n3),end='')
    contador += 1
