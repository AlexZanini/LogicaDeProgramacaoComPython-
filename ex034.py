salario = float(input('Digite seu salário R$ '))
almento15 = (salario * 15)/100
almento10 = (salario * 10)/100
if salario <= 1250.00:
    print('Parabens voce recebeu 15% de aumento seu salário agora sera de{:.2f}'.format(almento15 + salario))
else:
    print('Parabens voce recebeu 10% de aumento seu salário agora sera de{:.2f}'.format(almento10 + salario))
