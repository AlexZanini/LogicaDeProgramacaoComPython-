print('<>' * 4)
print('TABUADA')
print('<>' * 4)
num = int(input('Digite um numero inteiro para gerar a tabuada: '))
for n in range(1, 11):
    print('{} x {:2} = {}'.format(num, n, num*n))
