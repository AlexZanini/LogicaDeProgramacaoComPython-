n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print('O PRIMEIRO valor {} é maior que o segundo valor {}'.format(n1, n2))
elif n1 < n2:
    print('O SEGUNDO valor {} é maior que o primeiro valor {}'.format(n2, n1))
elif n1 == n2:
    print('Ambos os valore são iguais')
