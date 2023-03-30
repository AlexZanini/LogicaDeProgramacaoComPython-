def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except(ValueError, TypeError):
            print('\033[0;31m ERRO! Digite um numero inteiro\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31m Entrada de dados interrompida!\033[m')
            return 0
        else:
            return n



def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except(ValueError, TypeError):
            print('\033[0;31m ERRO! Digite um numero inteiro\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31m Entrada de dados interrompida!\033[m')
            return 0
        else:
            return n


#Programa Principal
n = leiaInt('Digite um numero Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n} e o real {r}')