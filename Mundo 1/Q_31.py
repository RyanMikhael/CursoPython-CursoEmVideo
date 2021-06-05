#Questão 31 do curso em vídeo

'''Programa que recebe a distância de uma viagem em km e calcula o preço da passagem'''

def main():
    distancia = float(input('Insira a distância da viagem em km: '))
    if distancia <= 200:
        '''Preço de 0,50'''
        preço = distancia * 0.50
        print('O preço da viagem é {}'.format(preço))
    else:
        preço = distancia * 0.45
        print('O preço da viagem é {}'.format(preço))

main()