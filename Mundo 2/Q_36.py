#Questão 36 do curso em vídeo

'''Programa que aprova um emprestimo bancário de acordo com as informações inseridas'''

def main():
    valor = float(input('Insira o valor da casa em R$: '))
    salario = float(input('Digite o salário do comprador: '))
    qtd_anos = int(input('Insira a quantidade de anos em que pretende pagar: '))
    porcentagem = (salario * 3)/10
    prestacao = valor / (qtd_anos * 12)

    if prestacao > porcentagem:
        print('\033[31mEmprestimo negado!!\nPrestação mensal ultrapassou os 30% do salario\033[m')
    else:
        print('\033[34mEmpréstimo pode ser aprovado!!\033[m')
    print('A prestação mensal é de {:.2f} R$ para {} anos\n30% de seu salario corresponde a {:.2f} R$'.format(prestacao,qtd_anos,porcentagem))

main()