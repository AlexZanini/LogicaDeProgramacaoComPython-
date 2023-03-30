from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de seu nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade ,atual))
menor  = 18 - idade
maior = idade -18
if idade < 18:
    print('Ainda falta {} anos para se alistar no serviço militar '.format(menor))
    print('Seu alistamento é em {}'.format(atual + menor))
elif idade > 18:
    print('Já passou {} anos da hora de se alistar'.format(maior))
    print('Seu alistamento foi em {}'.format(atual - maior))
else:
    print('Você tem que se alistar IMEDIATAMENTE ')


