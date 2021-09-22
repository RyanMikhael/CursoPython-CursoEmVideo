#Questão 76 do Curso em video

'''Programa que coloca produto e seu respectivo preço em sequencia dentro de uma tupla e devolve
ao usuário um conjunto de preços dos respectivos produtos em forma tabular'''

produtos = ('Arroz', '4 R$', 'Acucar', '1 R$', 'Biscoito', '2.20 R$', 'Meia duzia de bananas', '6 R$',
'Bone', '25 R$', 'Camisa', '50 R$', 'Energ. Monster', '8 R$', 'Pct Copos 180ml', '2.5 R$')

count = 1
while count < len(produtos):
    print('{} ---- {}\n'.format(produtos[count-1], produtos[count]))
    count += 2
