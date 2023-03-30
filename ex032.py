import time
ano = int(input('Digite o ano para verificar se é Bissexto: '))
bissexto = ano % 4
time.sleep(2)
if bissexto == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[0;30;42m Esse ano de {} é um ano Bissexto!\033[m'.format(ano))
else:
    print('\033[0;30;41m Esse ano de {} não é um ano Bissexto!\033[m'.format(ano))