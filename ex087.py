matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
terceira = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print('')
for p in range(0, 3):#Calculo dos numeros pares
    if matriz[0] [p] %2 ==0:
        par += matriz[0] [p]
    if matriz[1] [p] %2 ==0:
        par += matriz[1] [p]
    if matriz[2] [p] %2 ==0:
        par += matriz[2] [p]
for t in range(0, 3):#Calculo da Terceira coluna
    terceira += matriz[t] [2]
for m in range(0, 3):
    if matriz[1] [m] > maior:
        maior = matriz[1] [m]

print(f'A soma dos valoers pares é {par}')
print(f'A soma dos valoers da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')