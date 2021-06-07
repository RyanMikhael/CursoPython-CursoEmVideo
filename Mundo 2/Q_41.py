#Questão 41 do curso em vídeo
from datetime import date

'''Classificação de atleta de acordo com sua idade'''
ano_atual = date.today().year
ano_nasc = int(input('Insira o seu ano de nascimento: '))
idade = ano_atual - ano_nasc

print('Com {} anos você é classificado como atleta: '.format(idade))
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')