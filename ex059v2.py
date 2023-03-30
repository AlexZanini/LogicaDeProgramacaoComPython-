from time import  sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while  opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {} '.format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A Multiplicação entre {} x {} = {} '.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

    elif opcao == 5:
        print('Finalizado')

    else:
        print('Opção invalida. Tente novamente')
    print('<>' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
