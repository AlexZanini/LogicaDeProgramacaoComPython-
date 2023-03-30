dias = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados nesse periodo? '))
pagar = (dias * 60) + (km * 0.15)
print('O total de aluguel a pagar é de R${:.2f} '.format(pagar))

