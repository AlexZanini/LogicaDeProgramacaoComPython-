import random

def sorteio(lista):
    for cont in range(0, 5):
        lista.append(random.randint(1, 10))
    print(lista)


def par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando o valor das lista {lista}, temos {soma}')






num = list()
sorteio(num)
par(num)








