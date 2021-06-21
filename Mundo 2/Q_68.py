#Questão 68 do Curso em video
'''Jogo de par ou ímpar com o computador. O jogo só é interrompido quando o jogador perder, além de 
mostrar o total de vitórias consecutivas do usuário'''

from random import randint

escolha = ' '
computador = ' '
count = 0
while True:

    escolha = str(input('Escolha ímpar ou par(I/i = Impar || P/p = Par): ')).upper()

    if escolha == 'P':
        print('Voce escolheu Par e o computador é ímpar!\n'+ 100 * '-')
        n1 = int(input('\nInsira um numero inteiro de 0 a 20: '))
        n2 = randint(0,20)
        print('\nVoce escolheu o numero {} e o computador o numero {}'.format(n1,n2))

        if (n1 + n2) % 2 == 0:
            print('\033[34mVocê venceu!\033[m ')
            count += 1
        else:
            print('\033[31mVocê perdeu!\033[m ')
            print('Voce venceu {} vezes consecutivas'.format(count))
            break



    elif escolha == 'I':
        print('Voce escolheu Ímpar e o computador é par!\n'+ 100 * '-')
        n1 = int(input('\nInsira um numero inteiro de 0 a 20: '))
        n2 = randint(0,20)
        print('\nVoce escolheu o numero {} e o computador o numero {}'.format(n1,n2))

        if (n1 + n2) % 2 != 0:
            print('\033[34mVocê venceu!\033[m ')
            count += 1
        else:
            print('\033[31mVocê perdeu!\033[m ')
            print('Voce venceu {} veze(s) consecutiva(s)'.format(count))
            break

    else:
        print('Escolha incorreta!')
        break
    



