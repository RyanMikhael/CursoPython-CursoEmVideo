#Questão 51 do curso em vídeo

'''Programa que mostra os 10 primeiros termos de uma progressão aritmetica de um numero inserido
pelo usuario'''

n = int(input('Insira o primeiro numero de um progressão aritmética: '))
r = int(input('insira a razão da pprogressão aritmética: '))

print('Os 10 primeiros termos de uma PA do numero {} com razão {} são:\n{}'.format(n, r, n))
for i in range(1, 10):
    print('{}'.format(n + i * r))
print('FIM!!')