#
somaidade = 0
mairoidadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print('<<<< {}ª PESSOA >>>>'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        mairoidadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > mairoidadehomem:
        mairoidadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

mediaidade = somaidade /4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velhor tem {} anos e se chama {}'.format(mairoidadehomem, nomevelho))
print('Ao todo são {} mulher com menos de 20 anos'.format(totmulher))





