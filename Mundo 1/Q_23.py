#Questão 23 do curso em vídeo

def main():
    numero = int(input('Insira um numero que esteja entre 0 e 9999: '))
    if( numero > 9999):
        print('O numero inserido é maior que 9999')
    elif( numero < 0):
        print('O numero inserido é menor que 0: ')
    else:
        unidade = numero // 1 % 10
        dezena = numero // 10 % 10
        centena = numero // 100 % 10
        milhar = numero // 1000

        print(f'Unidade: {unidade}'+
        f'\nDezana: {dezena}'+
        f'\nCentena {centena}'+
        f'\nMilhar {milhar}')

main()