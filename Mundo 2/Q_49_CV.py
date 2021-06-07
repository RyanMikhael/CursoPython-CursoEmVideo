#Questão 49 do curso em vídeo

'''Tabuada'''

n = int(input('Insira o numero que deseja apresentar a tabuada: '))
print('\033[34mTabuada do numero {}\033[m'.format(n))
for i in range(1, 11):
    print('{} * {} = {}'.format(n,i, n*i))
print('FIM!!')


