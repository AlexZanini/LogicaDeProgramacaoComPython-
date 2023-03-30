matris1 = [[], [], []]
matris2 = [[], [], []]
matris3 = [[], [], []]

for n in range(0, 3):
    matris1[n].append(int(input(f'Digite o valor para [0, {n}]: ')))
for n in range(0, 3):
    matris2[n].append(int(input(f'Digite o valor para [1, {n}]: ')))
for n in range(0, 3):
    matris3[n].append(int(input(f'Digite o valor para [2, {n}]: ')))
print(f'{matris1[ 0 ]} {matris1[ 1 ]} {matris1[ 2 ]}')
print(f'{matris2[ 0 ]} {matris2[ 1 ]} {matris2[ 2 ]}')
print(f'{matris3[ 0 ]} {matris3[ 1 ]} {matris3[ 2 ]}')