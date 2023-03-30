print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>')
print('   Analisador de Triângulos')
print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[0;30;42m Os segmentos acima PODEM forma um triângulo, \033[m')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif    r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('\033[0;30;41m Os seguimentos acima NÂO podem format um triãngulo \033[m')

