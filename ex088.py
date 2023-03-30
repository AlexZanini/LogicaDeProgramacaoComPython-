import random
import time
from random import sample
print('<'* 15, '>'* 15)
name = 'JOGOS MEGA SENA'
print(f'{name:^30}')
print('<'*15, '>'*15)
num = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10,
       11, 12, 14, 14, 15, 16, 17, 18, 19, 20,
       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
       31, 32, 34, 34, 35, 36, 37, 38, 39, 40,
       41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 54, 54, 55, 56, 57, 58, 59, 60 ]

quant = int(input('Quantos jogos você quer sortear? '))
print()
for n in range(0, quant):
    jogo = sorted(sample(num, 6))
    print(f'Jogo {n+1}: {jogo}')
    time.sleep(1)