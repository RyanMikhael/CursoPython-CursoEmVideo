#Questão 53 do curso em vídeo

'''Programa que identifica palíndormos'''

frase = str(input('Insira uma frase: ')).strip().upper()
palin = frase.split()
junção = ''.join(palin)
inverso = ''

for letra in range(len(junção) - 1, -1, -1):
    inverso += junção[letra]

if inverso == junção:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')