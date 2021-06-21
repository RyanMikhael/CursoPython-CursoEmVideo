# Questão 66 do Curso em vídeo

'''Programa que pede numeros inteiros e só para quando o numero digitado for 999, além de apresentar a soma
dos numeros digitados e quantos numeros foram digitados '''

from time import sleep

'''n = int(input('Insira um valor inteiro(999 para parar): '))
soma = n
count = 1

while n != 999:
    n = int(input('Insira um valor inteiro: '))
    soma += n
    count += 1
sleep(1)

print('Foram digitados {} numeros. A soma dos numeros digitados é igual a {}'.format(count- 1, soma - 999))'''

n = 0
soma = 0
count = 0

while True:
    n = int(input('Digite um numero inteiro(999 para parar): '))
    if n == 999:
        break
    soma += n
    count += 1

print('Calculando...')
sleep(1)

print('Foram digitados {} numeros. A soma dos numeros digitados é igual a {}'.format(count, soma))