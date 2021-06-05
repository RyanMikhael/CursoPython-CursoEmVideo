#Questão 26 do curso em vídeo
def main():
    frase = str(input('Digite uma frase: ')).strip().upper()
    contagem = frase.count('A')
    primeira = frase.find('A')
    segunda = frase.rfind('A')
    print('A letra "A" aparece {} vezes, sendo a primeira no indice {} e a ultima no indice {}'.format(contagem, primeira, segunda))

main()