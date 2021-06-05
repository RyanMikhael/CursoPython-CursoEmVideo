#Questão 33 do curso em vídeo

''' Program a que verifica qual o maior e qual o menor entre 3 numeros'''

def main():
    n1 = float(input('Insira um numero: '))
    n2 = float(input('Insira outro numero: '))
    n3 = float(input('Insira outro numero: '))

    maior = n1 
    if n2 > n1 and n2 > n3:
        print('{} é o maior'.format(n2))
    elif n3 > n1 and n3 > n2:
        print('{} é o maior'.format(n3))
    else:
        print('{} é o maior'.format(n1))

    menor = n1
    if n2 < n1 and n2 < n3:
        print('{} é o menor'.format(n2))
    elif n3 < n1 and n3 < n2:
        print('{} é o menor'.format(n3))
    else:
        print('{} é o menor'.format(n1))

main()