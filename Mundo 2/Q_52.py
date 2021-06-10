#Questão 52 do curso em vídeo

'''Verificando se um numero é ou não primo'''

n = int(input('Insira um numero inteiro: '))
div = 0
for i in range(1, n+1):
    if n % i == 0:
        div += 1
if div > 2:
    print('O numero não é primo!!')
else:
    print('O numero é primo!!')
