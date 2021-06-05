#Questão 15 do curso em vídeo
def main():
    # 1 dia alugado é 60R$ e o valor cobrado por kilometro rodado é 0.15 R$
    dia = int(input('Insira a quantidade de dias que o carro foi alugado: '))
    km = float(input('Insira a quantidade de km percorridos pelo carro alugado: '))
    resultado = (dia * 60) + (km * 0.15)
    print('O preço a se pagar de acordo com a quantidade de dias alugados e os km percorridos é \n{} R$'.format(resultado))
main()