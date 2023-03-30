cadastro = {}
galera = []
soma = media =0
while True:
    cadastro.clear()
    cadastro['Nome'] = str(input('Nome: '))
    while True:
        cadastro['Sexo'] = str(input('Sexo: M/F ')).upper().strip()[0]
        if cadastro['Sexo'] in 'MF':
            break
        print('ERRO! apenas M ou F')
    cadastro['Idade'] = int(input('Idade: '))
    soma += cadastro['Idade']
    galera.append(cadastro.copy())
    resp = str(input('Quer continuar? Y/N ')).strip().upper()[0]
    while resp not in 'YN':
        resp = str(input('Quer continuar? Y/N ')).strip().upper()[0]
    if resp == 'N':
        break

print(galera)
print('==')
print(f' - O grupo tem {len(galera)} pessoas')
media = soma / len(galera)
print(f' - A media de idede é de {media:5.2f}')
print(' - As mulhers cadastradas foram ', end=' ')
for n in galera:
    if n['Sexo'] == 'F':
        print(f'{n["Nome"]} ', end=' ')
for b in galera:
    if b['Idade'] > media:
        print('    ')
        for k, v in b.items():
            print(f'{k} = {v}, ', end=' ')