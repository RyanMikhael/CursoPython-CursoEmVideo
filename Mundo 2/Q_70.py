#Questão 70 do Curso em video

'''Programa que le o nome e o preço de vários produtos até que o usuário não deseje continuar,
ao final mostra o total gasto na compra, quantos produtos custam mais de 1000 R$ e qual é o nome
do produto mais barato'''

from time import sleep

total = 0
countProd = 0
nome = ''
preço = 0
maisBarato = nome
menorpreço = preço
count = 0


while True:

    nome = str(input('Insira o nome do produto: '))
    preço = float(input('Insira o preço do produto em R$: '))

    total += preço
    count += 1

    if count == 1:
        maisBarato = nome
        menorpreço = preço

    if preço < menorpreço:
        menorpreço = preço
        maisBarato = nome

    if preço > 1000.0:
        countProd += 1
        
    continuar = str(input('Deseja continuar( S - Sim / N - Não ): ')).upper()

    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('opção inserida errada!')
        break


print('...')
sleep(1)

print('O preço gasto na compra foi {:.2f} R$'.format(total))
print('{} produto(s) custa(m) mais de 1000 R$'.format(countProd))
print('O nome do produto mais barato é {}'.format(maisBarato))