#Questão 45 do curso em vídeo
from random import randint
from time import sleep

'''Jogo de pedra, papel e tesoura'''

escolhas = ('Pedra' , 'Papel', 'Tesoura')

print('0 === Pedra\n1 === Papel\n2 === Tesoura')
sua_escolha = int(input('Digite o numero correspondente a sua escolha: '))
print('Você escolheu {}'.format(escolhas[sua_escolha]))

computador = randint(0,2)
print('O computador escolheu {}'.format(escolhas[computador]))


if sua_escolha == 0 and computador == 2:
    print('Você venceu!!')
elif sua_escolha == 0 and computador == 1:
    print('Você perdeu!!')
elif sua_escolha == 0 and computador == 0:
    print('Empate!!')
elif sua_escolha == 1 and computador == 0:
    print('Você venceu!!')
elif sua_escolha == 1 and computador == 2:
    print('Você perdeu!!')
elif sua_escolha == 1 and computador == 1:
    print('Empate!!')
elif sua_escolha == 2 and computador == 1:
    print('Você venceu!!')
elif sua_escolha == 2 and computador == 0:
    print('Você perdeu!!')
elif sua_escolha == 2 and computador == 2:
    print('Empate!!')
else:
    print('Opção inválida!')