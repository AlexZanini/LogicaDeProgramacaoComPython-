print('<'*15, '>'*15)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('<'*15, '>'*15)
papelaria = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
          'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30,
          'Livro', 34.90)
for pos in range(0, len(papelaria)):
    if pos % 2 ==0:
        print(f'{papelaria[pos]:.<25}', end='')
    else:
        print(f'R${papelaria[pos]:>7.2f}')

