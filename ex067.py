''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''
resuldado = 0
tabuada = 0
while True:
    num = int(input('Quer ver a Tabuada de qual valor? '))
    print('=' * 10)
    if num < 0:
        break
    for tabuada in range(1, 11):
        resuldado = tabuada * num
        print(f'{num} x {tabuada} = {resuldado}')
print('\nO numero escolhido foi NEGATIVO!')
print('\nFIM')