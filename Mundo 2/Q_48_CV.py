#Questão 48 do curso em vídeo

'''Programa que mostra todos os multiplos de 3 entre 1 e 500'''

soma = 0
for n in range(1, 500):
    if n % 3 == 0:
        soma += n
print('O somatório de todos os numeros multiplos de 3 entre 1 e 500 é igual a {}'.format(soma))