import random
import time
from operator import itemgetter
cont = 0
game = {'Jogador1': '', 'Jogador2': '', 'Jogador3': '', 'Jogador4': ''}
game['Jogador1'] = random.randint(1, 6)
game['Jogador2'] = random.randint(1, 6)
game['Jogador3'] = random.randint(1, 6)
game['Jogador4'] = random.randint(1, 6)
print('Jogo de DADOS')
time.sleep(1)
ranking = list()
for n, i in game.items():
    print(f'O {n} tirou {i} no dado')
    time.sleep(1)
print('Ranking dos jogadores:')
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
for a, b in enumerate(ranking):
    print(f'{a+1}ª Lugar: {b[0]} com {b[1]}')
    time.sleep(1)

