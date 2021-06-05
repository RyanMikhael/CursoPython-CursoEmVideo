#Questão 28 do curso em vídeo
from random import randint
from time import sleep

'''Programa que faz o computador pensar em um numero e o usuário tem que acertar 
qual numero foi escolhido pela máquina'''

def main():
    n = randint(0,5)
    user = int(input('Insira um numero entre 0 e 5 e veja se acerta o valor escolhido pelo computador: '))
    print('\033[1;34mProcessando...\033[m')
    sleep(3)
    if user == n:
        print('\033[4;36;40mVocê venceu!\033[m')
    else:
        print('\033[31;43mVocê perdeu!\033[m')
    print('\033[4;32mO numero escolhido pela máquina foi {}'.format(n))

main()