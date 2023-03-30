'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0
resultado = 0
soma = n1 + n2
multiplicar = n1 * n2

while escolha != 5:
    print('''
    [ 1 ] SOMA
    [ 2 ] MULTIPLICA
    [ 3 ] MAIOR
    [ 4 ] novos números
    [ 5 ] SAIR
    ''')
    escolha = int(input('Qual opção voce escolhe: '))
    if escolha == 1:
        print('A Soma dos dois números é {}'.format(soma))
    elif escolha == 2:
        print('A Multiplicação dos dois números é {}'.format(multiplicar))
    elif escolha == 3:
        if n1 > n2:
            print('O numero {} é MAIOR que {}'.format(n1, n2))
        else:
            print('O numero {} é MENOR que {}'.format(n1, n2))
    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

print('')
print('END')