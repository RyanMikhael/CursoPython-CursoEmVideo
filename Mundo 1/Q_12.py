#Questão 12 do curso em vídeo
def main():
    preço = float(input('Insira o preço do produto: '))
    desconto = (5 * preço) / 100
    print('O preço do produto com desconto de 5% é {}'.format(preço - desconto))
main()