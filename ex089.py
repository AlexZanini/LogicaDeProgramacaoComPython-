ficha = []
cont = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2], media ])
    cont += 1
    resp = str(input('Deseja continuar [Y/N] ')).strip().upper()[0]
    while resp not in 'YN':
        resp = str(input('Deseja continuar [Y/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('')
print(f'{"No.":<4} {"NOME:":<10} {"MÉDIA:":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
print('')
while True:
    aluno = int(input('Mosta as notas de qual aluno? (999 finaliza) '))
    if aluno == 999:
        print('Finalizado')
        break
    if aluno <= len(ficha) - 1:
        print(f'notas de {ficha[aluno][0]} são {ficha[aluno][1]}')

