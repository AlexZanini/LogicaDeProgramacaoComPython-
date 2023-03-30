from random import randint
itens = ('Pedra',  'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opçôes :
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('<>' * 15 )
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('<>' * 13 )
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador ==1:
        print('Parábens voê GANHOU! ')
    elif jogador == 2:
        print('PERDEU!')
    else:
        print('JODADA INVALIDA!')

elif computador == 1:
    if jogador == 0:
        print('PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Parábens voê GANHOU! ')
    else:
        print('JODADA INVALIDA!')
elif computador == 2:
    if jogador == 0:
        print('Parábens voê GANHOU! ')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JODADA INVALIDA!')



