'''
Exercício Python 064: Crie um programa que leia vários números
inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag).
'''
'''
num = 0
cont = - 1
n1 = 0
while num != 999:
    num = int(input('Digite um número e [999 para parar]: '))
    n1 += num
    cont += 1
print('\nVoce digitou {} numeros, A soma entre ele é {}'.format(cont, (n1 - 999)))
#print('A soma entre ele é {}'.format(n1 - 999))
'''
# posso també demonstra a variavel dessa forma (num = cont = soma = 0)
cont = 0
soma = 0
num = int(input('Digite um número e [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número e [999 para parar]: '))
print('\nVoce digitou {} numeros, A soma entre ele é {}'.format(cont, soma))
#print('A soma entre ele é {}'.format(n1 - 999))

