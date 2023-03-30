nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
media = (nota1 + nota2) /2
if media < 5.0:
    print('Sua média foi de {:.1f} \033[0;30;41m REPROVADO \033[m'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média foi de {:.1f} \033[0;30;43m RECUPERAÇÂO \033[m'.format(media))
else:
    print('Parapéns sua média é de {:.1f} \033[0;30;42m APROVADO \033[m'.format(media))

