#Questão 64 do curso em vídeo

'''Programa que lê varios numeros e só para quando uma condição é atendida,alem de registrar quantos
numeros foram digitados pelo usuário. A condição a ser atendida no caso é que seja digitado o numero 999'''

n = 0
contador = 0
soma = 0
while n != 999:
    n = int(input('Insira um numero: '))
    
    if n != 999:
        contador += 1
        soma += n
print('Foram digitados {} numeros.'.format(contador))
print('A soma dos numeros digitados é igual a {}'.format(soma))
