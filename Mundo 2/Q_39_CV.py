#Questão 39 do curso em vídeo

'''Alistamento militar'''

def main():
    ano_nasc = int(input('Insira o seu ano de nascimento: '))
    ano_atual = int(input('Insira o ano atual: '))

    diferença = ano_atual - ano_nasc
    calculo = diferença - 18
    anos = abs(calculo)

    if calculo > 0:
        print(f'Você ja passou do tempo do alistamento\nDeveria ter se alistado há {anos} anos!')
    elif calculo < 0:
        print(f'Voçê ainda vai se alistar para o serviço militar\n Faltam {anos} anos para seu alistamento!')
    else:
        print('É a hora exata de se alistar ao serviço militar!\nEsse é seu ano para o alistamento!')

main()