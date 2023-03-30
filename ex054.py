# Quantidade de pessoas maiores e menores de 21 anos
from datetime import date
print('<<<<<<<<<< Ano de Nascimento >>>>>>>>>>')
menor = 0
maior = 0
atual = date.today().year
for cont in range(1 ,8):
    nascimento = int(input('Digite o ano de Nascimento da {}° pessoa: '.format(cont)))
    if atual - nascimento < 21:
        menor = menor + 1
    elif atual - nascimento >= 21:
        maior = maior + 1
print('{} Pessoas ainda não atingiram a maioridade e {} já são maiores.'.format(menor, maior))














