#079 - Valores únicos em uma Lista
# Versão 2
valor = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valor:
        valor.append(num)
    else:
        print('Valor duplicado ')
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'Nn':
        break
print('Os valores digitafos foram {}'.format(sorted(valor)))