altura = float(input('Digite sua altuara em metros: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('O valor de seu imc é de {:.1f} você está ABAIXO DO PESO '.format(imc))
elif imc  >= 18.5 and imc < 25:
    print('O valor de seu imc é de {:.1f} você está com o PESO IDEAL '.format(imc))
elif imc >= 25 and  imc < 30:
    print('O valor de seu imc é de {:.1f} você está com SOBREPESO  '.format(imc))
elif imc >= 30 and  imc < 40:
    print('O valor de seu imc é de {:.1f} você está  com OBESIDADE '.format(imc))
else:
    print('O valor de seu imc é de {:.1f} você está com OBESIDADE MÓRBIDA '.format(imc))
