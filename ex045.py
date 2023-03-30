import random
import time
print('\033[0;30;44m Desafio você a jogar Jokepô comigo.  Lembre-se que eu sou o melhor... escolha 1, 2 ou 3 \033[m')
time.sleep(1)
print('1: Pedra ')
pedra = 'Pedra'
time.sleep(1)
print('2: Papel')
papel = 'Papel'
time.sleep(1)
print('3: Tesoura')
tesoura = 'Tesoura'
time.sleep(1)
jogador = int(input('Qual sua Jogada? '))
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)
#lista = [pedra, papel, tesoura]
cpu = random.choice([pedra, papel, tesoura])
if  jogador == 1 and cpu == pedra:
    print('Eu escolhir {} e você também escolheu {}'.format(pedra,pedra))
    time.sleep(1)
    print('\033[1;30;43m EMPATAMOS!!!\033[m')
elif jogador == 2 and cpu == papel:
    print('Eu escolhir {} e você também escolheu {}'.format(papel,papel))
    time.sleep(1)
    print('\033[1;30;43m EMPATAMOS!!!\033[m')
elif jogador == 3 and cpu == tesoura:
    print('Eu escolhir {} e você também escolheu {}'.format(tesoura, tesoura))
    time.sleep(1)
    print('\033[1;30;43m EMPATAMOS!!!\033[m')
elif jogador == 1  and cpu == papel:
    print('Eu escolhi {} e você escolheu {}'.format(papel, pedra))
    time.sleep(1)
    print('\033[1;30;41m YOU LOSE!!! \033[m')
elif jogador == 1 and cpu == tesoura:
    print('Eu escolhi {} e você escolheu {}'.format(tesoura, pedra))
    time.sleep(1)
    print('\033[1;30;42m WINNER!!! \033[m')
elif jogador == 2 and cpu == pedra:
    print('Eu escolhi {} e você escolheu {}'.format(pedra, papel))
    time.sleep(1)
    print('\033[1;30;42m WINNER!!! \033[m')
elif jogador == 2 and cpu  == tesoura:
    print('Eu escolhi {} e você escolheu {}'.format(tesoura, papel))
    time.sleep(1)
    print('\033[1;30;41m YOU LOSE!!! \033[m')
elif jogador == 3 and cpu == pedra:
    print('Eu escolhi {} e você escolheu {}'.format(pedra, tesoura))
    time.sleep(1)
    print('\033[1;30;41m YOU LOSE!!! \033[m')
elif jogador == 3 and cpu == papel:
    print('Eu escolhi {} e você escolheu {}'.format(papel, tesoura))
    time.sleep(1)
    print('\033[1;30;42m WINNER!!! \033[m')
time.sleep(1)
print('')
print('')
print('By Alex Zanini...')









