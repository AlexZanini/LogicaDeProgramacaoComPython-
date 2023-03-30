import math
co = float(input('Comprimeto do cateto oposto: '))
ca = float(input('comptimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))