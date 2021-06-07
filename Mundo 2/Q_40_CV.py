#Questão 40 do curso em vídeo

'''Programa que calcula médias de um aluno e diz se ele esta aprovado, reporvado ou de recuperação'''

n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1 + n2)/ 2

print('SUA MÉDIA FOI {}'.format(m))
if m >= 7:
    print('APROVADO!')
elif m > 5 and m < 7:
    print('RECUPERAÇÃO!')
else:
    print('REPROVADO!')