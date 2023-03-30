#Lista composta a analise de dados
temp = list()
pessoas = list()
cont1 = 0
maior = 0
menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()

    resposta = str(input('Deseja continuar [Y/N]')).strip().upper()[0]
    while resposta not in 'YN':
        resposta = str(int(input('Deseja continuar [Y/N]'))).strip().upper()[0]
    if resposta == 'N':
        break
print('')
print(f'Ao total, você cadstrou {len(pessoas)} pessoas.')
print('')
print(f' O maior peso foi {maior}Kg.  Peso de ', end='')
for p in pessoas:
    if p[1]  == maior:
        print(f'{p[0]}', end='')
print('')
print(f' O menor peso foi {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end='')