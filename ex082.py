valor = []
imp = []
par = []

while True:
    valor.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar [Y/N]')).strip().upper()[0]
    while resposta not in 'YN':
        resposta = str(int(input('Deseja continuar [Y/N]'))).strip().upper()[0]
    if resposta == 'N':
        break
for i, v in enumerate(valor):
    if v% 2 == 0:
        par.append(v)
    else:
        imp.append(v)


print(f'lista completas {valor}')
print(f'Valores PARES digitados {par}')
print(f'valores IMPARES digitados {imp}')

