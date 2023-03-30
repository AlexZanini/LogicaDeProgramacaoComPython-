num = int(input('Digite um numero: '))
tot = 0
for cont in range(1, num +1):
    if num % cont == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end='')
    print(' {} '.format(cont), end='')
print('\n\33[m O número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso {} é um número PRIMO!'.format(num))
else:
    print('NÂO é um número primo')
