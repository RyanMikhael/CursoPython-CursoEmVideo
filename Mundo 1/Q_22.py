#Questão 22 do curso em vídeo

def main():
    nome = str(input('Insira o seu nome completo: ')).strip()
    maiusculo = nome.upper()
    minuscula = nome.lower()
    dividida = nome.split()
    tam = len(nome) - nome.count(' ')
    pr_nome = len(dividida[0])
    

    print('''O nome com todas as letras maiusculas é {}
    \nO nome com todas as letras minusculas é {}
    \nA quantidade de letras sem considerar os espaços é {}
    \nO primeiro nome possui {} letras'''.format(maiusculo, minuscula, tam, pr_nome))

main()