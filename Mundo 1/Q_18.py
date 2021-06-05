#Questão 18 do curso em vídeo
from math import sin, cos, tan, radians
def main():
    a = float(input('Insira o valor do angulo: '))
    seno = sin(radians(a))
    cosseno = cos(radians(a))
    tangente = tan(radians(a))
    print('A partir do angulo inserido\nO seu seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(seno, cosseno, tangente))

main()