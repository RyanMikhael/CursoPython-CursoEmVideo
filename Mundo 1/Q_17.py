#Questão 17 do curso em vídeo
from math import sqrt, pow
def main():
    print('A partir dos conhecimentos sobre triangulo retangulo\n')
    cat_op = float(input('Insira o comprimento do cateto oposto: '))
    cat_ad = float(input('Insira o comprimento do cateto adjacente: '))
    hipotenusa = sqrt(pow(cat_op, 2) + pow(cat_ad, 2))
    print('O valor da hipotenusa do triangulo é {:.2f}'.format(hipotenusa))

main()   