numero = int(input('Digite um número inteiro: '))
par = numero % 2
if  par == 0:
    print('O número digitado {} é par '.format(numero))
else:
    print('O número digitado {} é impar '.format(numero))
