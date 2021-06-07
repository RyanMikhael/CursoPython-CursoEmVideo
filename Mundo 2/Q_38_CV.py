#Questão 38 do curso em vídeo

'''Comparação de dois numeros'''

n1 = int(input('Insira um valor inteiro: '))
n2 = int(input('Insira outro valor inteiro: '))

if n1 > n2:
    print('O primeiro valor é maior!\n{} é maior que {}'.format(n1, n2))
elif n1 == n2:
    print(f'Não existe valor maior, os dois numeros são iguais!\n{n1} = {n2}')
else:
    print('O segundo valor é maior!\n{} é maior que {}'.format(n2, n1))