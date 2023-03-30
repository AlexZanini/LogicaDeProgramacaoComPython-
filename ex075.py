cont9 = 0
numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores {numeros}')
for n in numeros:
    if n == 9:
        cont9 += 1
print(f'O valor 9 apareceu {cont9} vezes')
# print(f'O valor 9 apareceu {numeros.count(9)} vezes') <-- modo simplificado sem for
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição ')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=', ')

