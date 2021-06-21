#Questão 69 do Curso em video

'''Programa que le a idade e o sexo de várias pessoas, até que o usuário não queira continuar,
ao final ele mostra quantas pessoas tem mais de 18, quantos homens foram cadastrados, quantas
mulheres tem menos de 20 anos'''

from time import sleep

''' Quantos homens foram cadastrados'''
countMan = 0
'''Quantas mulheres com menos de 20 anos'''
countWoman20 = 0
'''Quantas pessoas com mais de 18 anos'''
countPeople18 = 0

while True:
    idade = int(input('Insira a idade: '))
    sexo = str(input('Insira o sexo\n(M - masculino / F - Feminino): ')).upper()
    continuar = str(input('Deseja continuar( S - Sim / N - Não ): ')).upper()

    if sexo == 'M':
        countMan += 1
    
    if sexo == 'F' and idade < 20:
        countWoman20 += 1
    
    if idade > 18:
        countPeople18 += 1

    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('opção inserida errada!')
        break


print('...')
sleep(1)

print('Foram cadastrados {} homens!'.format(countMan))
print('Foram cadastrados {} mulheres com menos de 20 anos !'.format(countWoman20))
print('Foram cadastrados {} pessoas com mais de 18 anos!'.format(countPeople18))