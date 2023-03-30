def fatorial(n, show=False):
    """
    <<<<< Calcula o fatorial de um Número >>>>>
    :param n: Número indicado para o calculo
    :param show: Mostra a caonta fatorial (Opcional)
    :return: Retorna o valor Fatorial
    """
    f = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= cont
    return f


#numero = int(input('Digite oum número: '))
print(fatorial(5, show=True))
print('')
help(fatorial)
