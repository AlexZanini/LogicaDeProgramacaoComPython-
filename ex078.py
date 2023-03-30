valores = []
min = 0
max = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if  c == 0:
        min = valores[c]
        max = valores[c]
    else:
        if valores[c] < min:
            min = valores[c]
        if valores[c] > max:
            max = valores[c]

print('')
print(f'Você digitou os valores {valores}')

print(f'O menor valor foi {min} nas posoções ', end=' ')
for i, v in enumerate(valores):
    if v == min:
        print(f'{i}...', end=' ')
print(f'\nO maior valor foi {max} nas posoções ', end=' ')
for i, v in enumerate(valores):
    if v == max:
        print(f'{i}...', end=' ')