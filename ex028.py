import random
numero = int(input('Digite seu numero: '))
pc = random.randint(1,5)
print('O numero excolhido pelo pc é {}  '.format(pc))

if numero == pc:
    print('Voce Acertou! o seu é numero {} é o numero do pc foi {} '.format(numero, pc))
else:
        print('Voce errou! ')

