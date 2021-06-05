#Questão 13 do curso em vídeo
def main():
    salario = float(input('Insira o salario do funcionário: '))
    aumento = (15 * salario) / 100
    print('O salario do funcionário com 15% de aumento é {}'.format(salario + aumento))
main()