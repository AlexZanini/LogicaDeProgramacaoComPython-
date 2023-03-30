import time
print('<<<<<<<<<< LIMITE DE VELOCIDADE 8OKm >>>>>>>>>>>')
velocidade = int(input('Por favor informe sua velocidade (Apenas números inteiros): '))
multa = (velocidade - 80)
preco = float(multa * 7)
print('Sua velociade é de {}{}{}Km'.format('\033[4;34m', velocidade,'\033[m'))
if velocidade <= 80:
    time.sleep(1)
    print('\033[0;30;42mEsta dentro do limite de velocidade\033[m')
else:
    print('\033[1;30;41mVoce foi MULTADO!\033[m')
    print('Você ultrapassou o limite da Rodovia, a multa vai custar R$7,00 por cada Km ultrapassado')
    print('Processando...')
    time.sleep(5)
    print('O valor de sua multa é de R${:.2f}'.format(preco))