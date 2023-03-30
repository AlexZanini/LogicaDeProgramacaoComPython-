from datetime import date
import time
cadastro = {}
ano = date.today().year
cadastro['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
cadastro['Idade'] = ano - nascimento
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['CTPS'] == 0:
    for a, b in cadastro.items():
        print(f'{a} tem o valor  {b}')
        time.sleep(1)
else:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: R$ '))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] + 35) - nascimento
    print('')
    print('<' *15, '>'*15)
    for a, b in cadastro.items():
        print(f'{a} tem o valor  {b}')
        time.sleep(1)
