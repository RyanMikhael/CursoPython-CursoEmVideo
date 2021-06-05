#Questão 34 do curso em vídeo

'''Programa que faz um ajuste salarial(aumento) de acordo com o salário inserido'''

def main():
    s = float(input('Insira o salário do trabalhador: '))
    '''Aumento de 10% ppara salários superiores a 1250 R$'''
    if s > 1250:
        aumento = s + (s/10)
        print('O salario do trabalhador era {} R$\nCom o aumento ficou {} R$'.format(s, aumento))
    else:
        porcentagem = (s * 15) / 100
        aumento = s + porcentagem
        print('O salario do trabalhador era {:.2f} R$\nCom o aumento ficou {:.2f} R$'.format(s, aumento))
    
main()