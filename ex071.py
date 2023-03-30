print('=' * 30)
print('{:^30}'.format('BANCO PYTHON'))
print('=' * 30)
cinquenta = 0
vinte = 0
dez = 0
um = 0
r50 = 0
r20 = 0
r10 = 0
r1 = 0
while True:
    valor = int(input('Qual valor do saque R$ '))
    cinquenta = valor // 50
    r50  = valor % 50
    if r50 != 0:
        vinte = r50 // 20
    r20 = r50 % 20
    if r20 !=0 and r20 >= 10:
        dez = r20 // 10
    r10 = r20 % 10
    if r10 != 0 and r10 < 10:
        r1 = r10
        um = r10 // 1
    break
print('')
print('<' * 12, '>' * 12)
if cinquenta != 0:
    print(f'Total de {cinquenta} cédulas de 50')
if vinte != 0:
    print(f'Total de {vinte} cédulas de 20')
if dez != 0:
    print(f'Total de {dez} cédulas de 10')
if um != 0:
    print(f'Total de {um} cédulas de 1')
print('<' * 12, '>' * 12)