#Questão 27 do curso em vídeo

def main():
    nome = str(input('Insira um nome completo: ')).strip().title()
    dividido = nome.split()
    primeiro = dividido[0]
    ultimo = dividido[-1]
    print('O primeiro nome da pessoa é {} e o ultimo nome da pessoa é {}'.format( primeiro, ultimo))

main()