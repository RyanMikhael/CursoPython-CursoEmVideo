#Questão 73 do Curso em video

'''Programa que guarda em uma tupla a tabela preenchida com os 20 primeiros colocados do campeonato  
brasileiro, devolvendo ao usuário o seguinte, os 5 primeiros times da tabela, os 4 ultimos colocados
times em ordem alfabetica em que posição está o time da chapecoense'''

tabela = ('Flamengo', 'Internacional', 'Palmeiras', 'São Paulo', 'Atletico MG', 'Gremio',
'Santos', 'Bragantino', 'Corinthians', 'Fluminense', 'Cruzeiro', 'Chapecoense', 'Ceará',
'Fortaleza', 'Atletico PA', 'Bahia', 'Sport', 'Vasco', 'Botafogo', 'Goiás')

print('Os 5 primeiros colocados são {}'.format(tabela[:5]))
print('\nOs ultimos 4 colocados são {}'.format(tabela[-4:]))
print('\nOs times em ordem alfabetica ficam na seguinte formação: ')
ordenacao = sorted(tabela)
for time in ordenacao:
    print(time)

print('\nA chapecoense está na posição {}'.format(tabela.index('Chapecoense')+1))
