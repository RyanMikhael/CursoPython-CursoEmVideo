#Questão 58 do curso em vídeo

'''Programa que pede para que voce escolha o numero escolhido pela maquina até acertar'''

from random import randint

computador = randint(1, 10)
contador = 1
menu = '\033[35mJOGO DE ADIVINHAÇÃO\033[m'.center(137)
print(menu)
print(137 * '-')
jogador = int(input('Escolha um numero de 1 a 10 e veja se é o mesmo numero escolhido pela máquina: '))

while jogador != computador:
    print('\033[31mVoce errou!\033[m')
    contador += 1
    jogador = int(input('Escolha um numero de 1 a 10: '))
print('\033[34mVocê acertou!\033[m')
print('Foram necessárias {} chances para acertar o numero escolhido!'.format(contador))
