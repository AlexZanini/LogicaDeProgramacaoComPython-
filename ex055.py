# ler cinco pessos e mostar o maior e o menos peso
menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input('Informe o seu peso da {}º pessoa: Kg '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print('O Maior peso lido foi {}Kg'.format(maior))
print('o Menor peso lido foi {}KG'.format(menor))