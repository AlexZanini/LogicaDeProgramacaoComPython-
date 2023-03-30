casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do seu salário: R$ '))
anos = int(input('Em quantos anos vai compra a casa? '))
meses  = anos * 12
valor = (salario * 30) / 100  #Calculo para aprovar o valor
aprovado = casa / meses

if valor > aprovado:
    print('\033[0;30;42m Paraben seu emprestimo foi aprovado \033[m')
    print('O valor da parcela sera de R${:.2f} que está dentro de 30% do seu salário'.format(valor))
elif valor == aprovado:
    print('Seu valor foi aprovado, está batendo 30% do seu salário ')
else:
    print('\033[0;30;41m Emprestimo negado \033[m')
    print('O valor da parcele R${:.2f} corresponde a mais de 30% do seu salário'.format(valor))




'''
print(meses)
print(valor)
print(aprovado)
'''