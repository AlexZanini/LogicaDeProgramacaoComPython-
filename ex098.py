import time

def contador (i, f, p):
    print(f'Contar de {i} até {f}, de {p} em {p}')
    print('')
    time.sleep(1)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=False)
            time.sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=False)
            time.sleep(0.5)
            cont -= p
        print('FIM!')


#Programa principal
inicio  = int(input('Inicio: '))
final = int(input('Final: '))
pulando = int(input('Pulando de: '))
contador(inicio, final, pulando)




