'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
certar, mostrando no final quantos palpites foram necessários para vencer.'''


from random import randint
computador = randint(0, 10)
print('-=-' *20)
print('Vou pensar em um número sntre 0 e 10, tente advinha... ')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? '))
cont = 1
while computador != jogador:
    print('Não pensei em {}'.format(jogador))
    cont += 1
    jogador = int(input('Tene novamente: '))
    if computador == jogador:
        print('PARABENS!!!')
        print('Eu pensei em {} e você escolheu {}'.format(computador, jogador))
        print('Voce usou {} tentativas'.format(cont))