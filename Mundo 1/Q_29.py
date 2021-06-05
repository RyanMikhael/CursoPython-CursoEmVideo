#Questão 29 do curso em vídeo

'''Programa que recebe a velocidade de um carro e caso ele esteja com velocidade acima de 80km/h
printe uma mensagem dizendo que ele esta multado e quanto é a multa'''

def main():
    vel = float(input('Insira a velocidade do carro: '))
    '''Valor da multa é 7 R$'''
    multa = (vel - 80) * 7
    if vel > 80:
        print('Você foi multado!\nUltrapassou o limite de 80km/h\nSua multa é de {} R$'.format(multa))
    else:
        print('Sua velocidade está ok')
    
main()