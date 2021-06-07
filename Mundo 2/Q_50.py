#Questão 50 do curso em vídeo

'''Programa que pede 6 numeros pro usuário e soma somentes os pares'''

s = 0
for i in range(6):
    n = int(input('Insira um numero: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos numeros pares inseridos é igual a {s}')
