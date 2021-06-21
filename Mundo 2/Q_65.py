#Questão 65 do curso em vídeo
from time import sleep

'''Programa que lê vários numeros até que o usuário queira parar, além de imprimir a média, o maior valor
lido e o menor valor lido'''

#Declaração de variáveis
r = ''
n = int(input('Insira um numero: '))
contador = 1
soma = n
media = soma / contador
maior = n
menor = n

while r != 'N':
    r = str(input('Deseja continuar(S/n): ')).upper()
    if r == 'S':
        n = int(input('Insira um numero: '))
        soma += n
        contador += 1
        media = soma / contador
        
        if n > maior:
            maior = n
        
        if n < menor:
            menor = n

    elif r == 'N':
        break
    else:
        print('Opção inválida!')

print('\033[34mCARREGANDO RESULTADO...\033[m')  
sleep(1)
print('A média dos numeros digitados é {:.1f}'.format(media))
print('O maior valor lido foi {}'.format(maior))
print('O menor valor lido foi {}'.format(menor))
