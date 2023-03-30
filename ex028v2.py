from random import randint
from time import sleep
import pygame
pygame.mixer.init()
pygame.init()
computador = randint(0, 5) # faz o computador escolher um numero de 0 a 5
print('-=-' *20)
print('Vou pensar em um número sntre 0 e 5, tente advinha... ')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS!!! Você venceu!')
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
else:
    print('GANHEI eu pencei no número {} e não em {}!'.format(computador, jogador))