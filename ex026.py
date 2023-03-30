frase = str(input('Digite uma frase: ')).upper().strip()
conta = frase.count( 'A')
Primeira = frase.find('A')+1
ultima = frase.rfind('A')+1
print('A letra A aparece {} vezes na frase'.format(conta))
print('A primeira letra A está na pocição: {}'.format(Primeira))
print('A  última letra A está na pocição: {}'.format(ultima))
