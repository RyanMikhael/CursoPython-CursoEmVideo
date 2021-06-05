#Questão 32 do curso em vídeo

def main():
    '''Programa que lê um ano qualquer e diz se ele é um ano bissexto'''
    ano = int(input('Insira um ano: '))
    dividido = ano % 100
    if dividido > 0:
        if dividido % 4 == 0:
            print('{} é um ano bissexto!'.format(ano))
        else:
            print('{} não é um ano bissexto!'.format(ano))
    else:
        if ano % 400 == 0:
            print('{} é um ano bissexto!'.format(ano))
        else:
            print('{} não é um ano bissexto!'.format(ano))

main()