def area (a, b):
    c = (a * b)
    print(f'A área de um terreno {a}x{b} é de {c}m²')


print('Controle de Terrenos')
print('<' * 10, '>' * 10)
larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
area(larg, compr)


