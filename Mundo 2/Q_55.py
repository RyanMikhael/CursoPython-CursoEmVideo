#Questão 55 do curso em vídeo

'''Programa que lê o peso de 5 pessoas e diz qual o maior e qual o menor'''

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Insira o peso da {} pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é o de {} kg e o menor peso é o de {} kg'.format(maior, menor))

