''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre:'''
import datetime
ano = datetime.datetime.today().year
contH = 0
contM18 = 0
mulher18 = 0
while True:
    print('=' * 20)
    print('CADASTRE UMA PESSOA')
    print('=' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('=' * 20)
    if sexo == 'M':
        contH += 1
    if idade >= 18:
        contM18 += 1
    if sexo == 'F' and idade < 20:
        mulher18 += 1
    parar = str(input('Quer continuar? [Y/N] ')).strip().upper()[0]
    while parar != 'Y' and parar != 'N':
        parar = str(input('Quer continuar? [Y/N] ')).strip().upper()[0]
    if parar == 'N':
        break
print('')
print('======= FIM DO PROGRAMA =======')
print(f'Total de pessoas maiores de 18 anos: {contM18}')
print(f'Ao todo temos {contH} homen(s) cadastrados')
print(f'E temos {mulher18} mulher(es) com menos de 20 anos')