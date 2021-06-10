#Questão 56 do curso em vídeo

'''Programa que lê o nome, idade e sexo de 4 pessoas e faz uma analise, devolvendo para o usuário 
a média da idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos'''

soma = 0
h_velho = ''
idade_velho = 0
contador = 0
for i in range(1, 5):
    nome = str(input(f'Insira o nome da {i} pessoa: '))
    idade = int(input(f'Insira a idade da {i} pessoa: '))
    sexo = str(input(f'Insira o sexo da {i} pessoa(M == Masculino/F == Feminino): '))
    soma += idade
    if i == 1 and sexo == 'M':
        idade_velho = idade
        h_velho = nome
    elif idade > idade_velho and sexo == 'M' and nome != h_velho:
        idade_velho = idade
        h_velho = nome
        
    if sexo == 'F' and idade < 20:
        contador += 1


media = soma / 4
print(f'A média das idades é {media:.1f}')
print(f'O nome do homem mais velho é {h_velho}')
print(f'Dentre as 4 pessoas há {contador} mulhere(s) com menos de 20 anos!')