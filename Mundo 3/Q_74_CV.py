#Questão 74 do Curso em video

'''Programa que dá 5 numeros aleatórios e os adiciona na tupla, após isso mostra a listagem
dos numeros gerados e indica o menor e o maior entre eles '''

from random import randint

Numbers = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))

maior = Numbers[0]
menor = Numbers[0]

for num in Numbers:

    if num > maior:
        maior = num
        
    if num < menor:
        menor = num

print('Os numeros gerados foram {}'.format(Numbers))
print('O maior numero gerado foi {}'.format(maior))
print('O menor numero gerado foi {}'.format(menor))
