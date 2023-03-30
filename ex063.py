'''
Exercício Python 063: Escreva um programa que leia um
número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci.
É uma sucessão de números que aparece codificada em muitos fenômenos da natureza.
Descrita no final do século 12 pelo matemático italiano Leonardo Fibonacci,
ela é infinita e começa com 0 e 1.
Os números seguintes são sempre a soma dos dois números anteriores.
Portanto: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

'''

num = int(input('Digite a Quantidade: '))
cont = 3
n1 = 0
n2 = 1
print('{} - {}'.format(n1, n2), end=' ')
while cont <= num:
    n3 = n1 + n2
    print('- {} '.format(n3), end=' ')
    n1 = n2
    n2 = n3
    cont += 1
print('\nFIM')