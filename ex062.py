primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
amais = 10
while amais != 0:
    total = total + amais
    while cont <= total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    amais = int(input('\nQuantos termos voce quer mostra a Mais?:  '))
print('\nFIM')



