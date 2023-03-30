print('<' *10, '>' *10)
print('Analisador de Triângulos')
print('<' *10, '>' *10)
print('')
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo')