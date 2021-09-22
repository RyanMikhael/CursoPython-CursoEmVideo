#Questão 72 do Curso em video

'''Programa que pede a um usuário um numero entre 0 e 20 e devolve o numero por extenso que vai
estar guardado dentro de uma tupla'''

tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
'dez', 'onze', 'doze', 'treze', 'quatorze,', 'quinze',' dezesseis', 'dezessete', 'dezoito',
'dezenove', 'vinte')

num = int(input('Insira um numero entre 0 e 20: '))
if num < 0 or num > 20:
    print('Numero digitado incorreto!')
else:
    print('o numero inserido por extenso é {}'.format(tupla[num]))