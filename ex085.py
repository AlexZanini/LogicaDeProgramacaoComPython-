#Lista com pares e impares (Lista dentro de outra lista)
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}ª valor: '))
    if valor %2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares são: {num[0]} ')
print(f'os valores ímpares são: {num[1]}')
#