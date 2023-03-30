''' Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

print('=' * 16)
print('LOJA PYTHON')
print('=' * 16)
soma = 0
maior = 0
menor = 0
cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    soma += preco
    cont += 1
    if preco > 1000:
        maior += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = str(input('Quer continuar comprando? [Y/N] ')). strip().upper()[0]
    while resp not in 'YN':
        resp = str(input('Quer continuar comprando? [Y/N] ')). strip().upper()[0]
    if resp == 'N':
        break
print('<<<<<<< FIM DO PROGRAMA >>>>>>>')
print(f'Total das compras R${soma}')
print(f'Temos {maior} produtos que custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
