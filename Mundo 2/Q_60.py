#Questão 60 do curso em vídeo

'''Programa que le um numero e calcula seu fatorial'''

n = int(input('Insira um numero inteiro: '))
contador = 1
fatorial = 1
while contador != n + 1:
    fatorial *= contador
    contador += 1
print('O fatorial de {} é igual a {}'.format(n, fatorial))
