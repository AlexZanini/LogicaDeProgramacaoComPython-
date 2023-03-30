valor = []

while True:
    valor.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar [Y/N]')).strip().upper()[0]
    while resposta not in 'YN':
        resposta = str(int(input('Deseja continuar [Y/N]'))).strip().upper()[0]
    if resposta == 'N':
        break
print('Você digitaou {} elementos'.format(len(valor)))
valor.sort(reverse=True)
print(f'Os valores digitads em orden decresente  {valor}')
if 5 in valor:
    print('O valor cinco(5) faz parte da lista!')
else:
    print('O valor cinco(5) NÃO foi encontrado na lista!')
