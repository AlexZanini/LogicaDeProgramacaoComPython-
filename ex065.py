'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''


num = 0
continuar = 'Y'
cont = 0
soma = 0
menor = maior = 0
while continuar in 'Y':
    num = int(input('Digite um valor inteiro: '))
    cont += 1
    soma += num
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    continuar = str(input('Quer continuar? [Y/N]: ')).strip().upper()[0]
print('Você digitou {} e o média foi {}'.format(cont, media))
print('O maior número é {} e o menor é {}'.format(maior, menor))



