#Número por extenso

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezasseis',
           'dezassete', 'dezoito', 'dezanove', 'vinte')
while True:
    valor = int(input('Digite um número entre 0 e 20: '))
    while True:
        if valor <= 0:
            print('Valor incorreto')
            valor = int(input('Digite um número entre 0 e 20: '))
        elif valor >= 21:
            print('Valor incorreto')
            valor = int(input('Digite um número entre 0 e 20: '))
        else:
            break
    print(f'o valor digitado foi {numeros[valor]}')
    sair = str(input('Deseja continuar S/N: ')).strip().upper()[0]
    while sair not in 'SN':
        sair = str(input('Deseja continuar S/N: ')).strip().upper()[0]
    if sair == 'N':
        break