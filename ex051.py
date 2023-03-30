print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for n in range  (primeiro, decimo + razao, razao):
    print('{}'.format(n), end=' -> ')
print('ACABOU')
