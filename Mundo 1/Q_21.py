#Questão 21 do curso em vídeo
import pygame
menu1 = str(input('Chame o computador: '))
print('Oi mestre!\nO que deseja?')
menu2 = str(input('Digite o que deseja: '))
if(menu2 == 'toca aquela musica'):
    pygame.init()
    pygame.mixer.music.load('/home/ryan/Música/nega.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
else:
    print('Até mais!')
    
