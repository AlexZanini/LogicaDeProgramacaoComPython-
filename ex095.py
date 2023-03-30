futebol = {}
partidas = []
time = []
while True:
    futebol.clear()
    futebol['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {futebol["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partidas {c + 1}? ')))
    futebol['Gols'] = partidas[:]
    futebol['Total'] = sum(partidas)
    time.append(futebol.copy())
    resp = str(input('Quer continuar? Y/N ')).strip().upper()[0]
    while resp not in 'YN':
        resp = str(input('Quer continuar? Y/N ')).strip().upper()[0]
    if resp == 'N':
        break

print('<<' *10, '>>' *10)
print('Cod ', end='')
for i in futebol.keys():
    print(f'{i:<14}', end='')
print('')


for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<14}', end='')
    print('')
while True:
    print('Mostar dados de qual jogador? digite o código: (999 STOP)')
    busca = int(input('Código do Jogador: '))
    if busca == 999:
        break
    if busca>= len(time):
        print('ERRRo ´codigo não encontrado ')
    else:
        print('<' *10, f'Levantamento do Jogador {time[busca]["Nome"]}', '>'*10)
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No Jogo {i+1} fez {g} gols')
    print('<<' * 10, '>>' * 10)