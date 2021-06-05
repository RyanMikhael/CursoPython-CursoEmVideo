#Questão 14 do curso em vídeo
def main():
    c = float(input('Insira um temperatura em grau Celsius(C°): '))
    f = (c * (9/5)) + 32
    print('{}° Celsius equivale a {}° Fahrenheit'.format(c, f))
main()