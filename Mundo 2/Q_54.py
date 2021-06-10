#Questão 54 do curso em vídeo
from datetime import date

'''Programa que lê sete anos de nascimento e diz quantos ja são maiores de idade e quantos não são'''

maior = 0
menor = 7 
ano_atual = date.today().year

for i in range(7):
    ano = int(input('Insira o ano de nascimento de uma pessoa: '))
    if ano_atual - ano > 18:
        maior += 1
        menor -= 1
print('Do ano de nascimento das pessoas inseridas\n{} são maiores de idade e {} são menores'.format(maior,menor))

