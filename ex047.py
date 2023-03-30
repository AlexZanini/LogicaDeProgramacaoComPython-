print('<>' * 20)
print('Mostrando números pares de 1 a 50:')
print('<>' * 20)
#par = (cont % 2)
for cont in range(2, 51, 2):
    if cont % 2 == 0:
        print(cont, end=' ')
