#Questão 16 do curso em video
#Usando modulo math
from math import trunc
def main():
    n = float(input('Insira um numero real: '))
    resultado = trunc(n)
    print('O numero real sem sua parte fracionária é igual a {}'.format(resultado))

main()

#usando int() para transformar em um valor inteiro
'''def main():
    n = float(input('Insira um numero real: '))
    print('O numero real sem sua parte fracionária é igual a {}'.format(int(n)))

main()'''

#Usando :.0f para deixar so a parte inteira
'''def main():
    n = float(input('Insira um numero real: '))
    print('O numero real sem sua parte fracionária é igual a {:.0f}'.format(n))
main()'''
