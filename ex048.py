print('<>' * 20)
print('Mutiplos de 3 entre 1 e 500:')
print('<>' * 20)
soma = 0
contaN = 0
for cont in range(0, 501):
    if  cont % 3 == 0 and cont % 2 == 1:
        soma += cont
        contaN = contaN + 1
        print(cont, end=' ')
print('\nA soma entre todos os números é: {}'.format(soma))
print('Foram {} somados '.format(contaN))