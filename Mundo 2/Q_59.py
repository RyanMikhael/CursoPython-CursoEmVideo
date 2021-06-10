#Questão 59 do curso em vídeo

'''Programa que lê dois numeros e mostra um menu de operações para eles'''
from time import sleep

print(137 * '\033[32m-\033[m')
menu = ('\033[33mCalculadora\033[m').center(137)
print(menu)
print(137 * '\033[32m-\033[m')

print('\nDigite dois numeros e escolha uma operação a ser executada em relação a eles!')

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
print('Digite o numero correspondente a operação que deseja executar!')

menu2 = print('[1] >> Somar\n[2] >> Multiplicar\n[3] >> Maior\n[4] >> Novos numeros\n[5] >> Sair do programa')

opcao = int(input('Insira a opcao que deseja executar: '))

while opcao != 5:
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('{} * {} = {}'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Os dois numeros são iguais')
    elif opcao == 4:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))
    else:
        print('opção inválida')
    input('Pressione <enter> se deseja continuar')
    sleep(1)
    menu2 = print('[1] >> Somar\n[2] >> Multiplicar\n[3] >> Maior\n[4] >> Novos numeros\n[5] >> Sair do programa')
    opcao = int(input('Insira a opcao que deseja executar: '))
