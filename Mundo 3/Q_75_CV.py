#Questão 75 do Curso em video

'''Programa que le quatro valores e os guarda em uma tupla, ao final mostra quantas vezes apareceu
o valor 9, em que posiçao foi diitado o primeiro valor 3 e quais foram os numeros pares'''

n1 = int(input('Insira um valor inteiro entre 0 e 20: '))
n2 = int(input('Insira um valor inteiro entre 0 e 20: '))
n3 = int(input('Insira um valor inteiro entre 0 e 20: '))
n4 = int(input('Insira um valor inteiro entre 0 e 20: '))

numeros = (n1, n2, n3, n4)


print('O numero 9 apareceu {} vez(es)'.format(numeros.count(9)))
print('\nO primeiro valor 3 foi digitado na posição {}'.format(numeros.index(3)))
print('\nOs numeros pares foram:')
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
