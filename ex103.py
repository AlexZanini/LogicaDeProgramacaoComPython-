import signal


def ficha(jogador='Desconhecido', gols=0):
    print(f'O jogador  {jogador} e ele marcou {gols} gol(s) no campeonato')



j = str(input('Qual o nome do jogador: '))
g = str(input('Quantos gols ele marcou: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)

