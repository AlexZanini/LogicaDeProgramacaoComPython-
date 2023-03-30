boletim = {'Nome':' ', 'Média': '','Sintuação':' ' }
boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))
print(f'Nome é igual {boletim["Nome"]}')
print(f'Média é igual {boletim["Média"]}')
if boletim['Média'] >= 6:
    boletim['Sintuação'] = 'Aprovado'
else:
    boletim['Sintuação'] = 'Reprovado'

print(f'Sintuação é igual a {boletim["Sintuação"]}')