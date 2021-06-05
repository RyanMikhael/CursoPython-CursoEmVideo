#Questão 35 do curso em vídeo
from time import sleep

'''Verificar a existência de um triângulo a partir das medidas de seu lado'''

def main():
    t1 = float(input('Qual o valor da primeira reta: '))
    t2 = float(input('Qual o valor do segunda reta: '))
    t3 = float(input('Qual o valor do terceira reta: '))
    print('\033[0;34mProcessando...\033[m')
    sleep(2)

    if (t1 + t2 > t3) and (t2 + t3 > t1) and (t1 + t3 > t2):
        print('Os valores das tres retas podem formar um triangulo!')
    else: 
        print('Os valores inseridos não podem formar um triângulo!')
    
main()