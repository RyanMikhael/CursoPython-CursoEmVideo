#Questão 57 do curso em vídeo

'''Programa que pede o sexo de uma pessoa mas só aceita M ou F'''

sexo = str(input('Insira o sexo de uma pessoa(M == Masculino/F == Feminino): ')).strip().upper()

while sexo not in 'MF':
    print('Sexo inválido\nDigite novamente')
    sexo = str(input('Insira o sexo da pessoa: ')).strip().upper()
if sexo == 'M':
    print('O sexo informado foi masculino!')
else:
    print('O sexo informado foi feminino!')
    