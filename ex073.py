times = ('Palmeiras', 'São Paulo','Santos', 'Grêmio', 'Internacional', 'Flamengo', 'Vasco',
        'Fluminense', 'Botafogo', 'Juventude', 'Athletico-PR', 'Atlético-MG', 'Chapecoense', 'Cruzeiro',
         'Bragantino', 'Fortaleza', 'América-MG', 'Sport', 'Bahia', 'Corinthians')

print('<' * 15, '>' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('<' * 15, '>' * 15)
print(f'Os cinco primeiros são {times[0:5]}')
print('<' * 15, '>' * 15)
print(f'Os quatro ultimos são {times[-4:]}')
print('<' * 15, '>' * 15)
print(f'Times em ordem Alfabetica {sorted(times)}')
print('<' * 15, '>' * 15)
print(f'o chapeconhece está na {times.index("Chapecoense")+1}º posição ')
