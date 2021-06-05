# Questão 04 do Curso em vídeo

def main():
    i = input('Digite algo: ')
    print('O tipo primitivo do que foi digitado é ',type(i))
    print('É numero: ',i.isnumeric())
    print('É alfa: ',i.isalpha())
    print('É decimal: ', i.isdecimal())
    print('É maiusculo: ',i.isupper())

main()