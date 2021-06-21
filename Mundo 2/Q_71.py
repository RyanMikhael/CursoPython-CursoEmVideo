#Questão 71 do Curso em video

'''Programa que simula o funcionamento de um caixa eletrônico, perguntando quanto o usuário deseja
sacar(numero inteiro) e programa informa quantas cédulas de cada valor serão entregues. Considerando
que o caixa emite cédulas de 50 R$, 20 R$, 10 R$ e 1 R$.'''

valor = int(input('Insira o valor que deseja sacar: '))
total = valor
ced = 50
totalCed = 0

while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} nota(s) de {ced} R$')
        
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        totalCed = 0

        if total == 0:
            break

