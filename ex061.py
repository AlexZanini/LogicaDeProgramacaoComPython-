'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end=' ')
    termo = termo + razao
    #print(termo, end=' ')
    cont = cont + 1
print('\nFIM')


