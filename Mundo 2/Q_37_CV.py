#Questão 37 do curso em vídeo

'''Programa que pede ao usuário escolher qual base deseja que o numero digitado seja convertido
Podendo ser base binária, octal ou hexadecimal'''

def main():
    n = int(input('Digite um numero inteiro: '))
    print('\033[1;34mEscolha uma das opções seguintes para conversão:\033[m')
    print('1 >>>> Binário\n2 >>>> Octal\n3 >>>> Hexadecimal')
    opcao = int(input('Digite a opção que deseja: '))

    if opcao == 1: 
        print('O numero {} convertido para binário é {}'.format(n, bin(n)[2:])) 
    elif opcao == 2:  
        print('O numero {} convertido para octal é {}'.format(n, oct(n)[2:])) 
    elif opcao == 3:
        print('O numero {} convertido para hexadecimal é {}'.format(n, hex(n)[2:])) 
    else:
        print('Opção escolhida inválida!!')  
    
main()