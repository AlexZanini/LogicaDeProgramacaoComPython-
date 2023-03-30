from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
anocorrent = date.today().year
mirim = anocorrent - ano
infantil = anocorrent - ano
junior = anocorrent - ano
senior = anocorrent - ano
master = anocorrent - ano
if mirim <= 9:
    print('Sua idade é {} anos e sua categoria é MIRIM'.format(mirim))
elif infantil <= 14 and infantil >= 10:
    print('Sua idade é {} anos e sua categoria é INFANTIL'.format(infantil))
elif junior <= 19 and junior >= 15:
    print('Sua idade é {} anos e sua categoria é JUNIOR'.format(junior))
elif senior <= 23 and   senior >= 20:
    print('Sua idade é {} anos e sua categoria é SENIOR'.format(senior))
else:
    print('Sua idade é {} anos e sua categoria é MASTER'.format(master))


