'''Jogo Par ou Impar'''
import random
import time
print('=' * 24)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=' * 24)
cont = 0
while True:
    pc = random.randint(0, 5)
    jogador = int(input('Digite um valor entre 0 e 5: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = jogador + pc
    imppar = soma % 2
    if imppar == 0 and escolha == 'P':
        print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} deu PAR')
        time.sleep(1)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    elif imppar != 0 and escolha == 'I':
        print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} deu ÍMPAR')
        time.sleep(1)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    elif imppar == 0 and escolha == 'I':
        print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} deu PAR')
        time.sleep(1)
        print('YOU LOSER!')
        break
    elif imppar != 0 and escolha == 'P':
        print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} deu ÍMPAR')
        time.sleep(1)
        print('YOU LOSER!')
        break
time.sleep(1)
print(f'GAME OVER! Você venceu {cont} vezes')



