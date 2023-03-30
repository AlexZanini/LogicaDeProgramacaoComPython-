'''import math
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, math.trunc(n)))'''

n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {:.0f}'.format(n, n))