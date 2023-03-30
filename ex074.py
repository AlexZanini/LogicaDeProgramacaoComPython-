'''Maior e menor valores em Tupla'''
import random
menor = 0
maior = 0
aleatorio = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
             random.randint(1, 10), random.randint(1, 10))
print(f'Valores sorteados {aleatorio}')
print(f'\nO mairo valor sorteado foi {max(aleatorio)}')
print(f'O menor valor sorteado foi {min(aleatorio)}')
# As linhas 8 e 9 simplifica as condicoes de if abaixo

if aleatorio[0] >= 1:
    menor = aleatorio[0]
if aleatorio[1] <= menor:
    menor = aleatorio[1]
if aleatorio[2] <= menor:
    menor = aleatorio[2]
if aleatorio[3] <= menor:
    menor = aleatorio[3]
if aleatorio[4] <= menor:
    menor = aleatorio[4]
print(f'\nMenor {menor}')
if aleatorio[0] >= 1:
    maior = aleatorio[0]
if aleatorio[1] >= maior:
    maior = aleatorio[1]
if aleatorio[2] >= maior:
    maior = aleatorio[2]
if aleatorio[3] >= maior:
    maior = aleatorio[3]
if aleatorio[4] >= maior:
    maior = aleatorio[4]
print(f'Maior {maior}')