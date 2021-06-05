#Questão 19 do curso em vídeo
import random
def main():
    nome1 = str(input('Insira o nome do primeiro aluno: '))
    nome2 = str(input('Insira o nome do segundo aluno: '))
    nome3 = str(input('Insira o nome do terceiro aluno: '))
    nome4 = str(input('Insira o nome do quarto aluno: '))
    lista = [nome1, nome2, nome3, nome4]
    resultado = random.choice(lista)
    print('\nO aluno sorteado foi',resultado)
main()