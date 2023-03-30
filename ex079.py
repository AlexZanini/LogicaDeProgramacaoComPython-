#079 - Valores únicos em uma Lista
valor = []

while True:
    valor.append(int(input('Digite um valor: ')))
    contsair = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while contsair not in 'SN':
        contsair = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if contsair == 'N':
        break
ordenados = set(valor)


print('Você digitou os valores ', sorted(ordenados),  '\nOs valores duplicados não foram inceridos na lista ')