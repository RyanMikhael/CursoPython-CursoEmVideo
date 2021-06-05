#Questão 11 do Curso em video
def main():
    altura = float(input('Insira a altura em metros de uma parede: '))
    largura = float(input('Insira a largura em metros de uma parede: '))
    area = altura * largura
    print('A area da parede é {} m²'.format(area))
    tinta = area / 2
    print('São necessários {} litros de tinta para pintar a parede'.format(tinta))

main()
