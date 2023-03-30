distancia = float(input('Qual a distancia de sua viagem? '))
maior = distancia * 0.45
menor = distancia * 0.50
print('Sua viagem tem {}Km de distancia'.format(distancia))
if distancia > 200:
    print('O valor de sua viagem é de {:.2f}'.format(maior))
else:
    print('o valor de sua viagem é de {:.2f}'.format(menor))

