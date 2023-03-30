futebol = {}
partidas = []
futebol['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {futebol["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partidas {c + 1}? ')))
futebol['Gols'] = partidas[:]
futebol['Total'] = sum(partidas)
print('=='*20)
print(futebol)
print('=='*20)
for a, b in futebol.items():
    print(f'o campo {a} te o valor {b}')
print('=='*20)
print(f'O jogador {futebol["Nome"]} jogou {tot} partidas ')
for n, m in enumerate(futebol['Gols']):
    print(f'Na partida {n+1}, fez {m} gols,')
