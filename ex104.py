def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO! Digite um numero inteiro\033[m')
        if ok:
            break
    return valor






#Programa Principal
n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {n} ')