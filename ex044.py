print('{:=^40}'.format(' LOJA '))
preco = float(input('Digite o valor do produto R$'))
print('')
print('[ 1 ]À vista no dinheiro com 10% de desconto  digite 1 ')
print(('[ 2 ]À vist ano cartão de credito com 5% de desconto digite 2 '))
print('[ 3 ]Em até 3x no cartão preço normal 3 ')
print(('[ 4 ]Em 4x no cartão de credito ou mais 20% de juros digite 4 '))
print('')
escolha = int(input('Qual forma de pagamento voce escolhe? '))
avista = preco - (preco * 10 / 100)
avistacartao = preco - (preco * 5 / 100)
cartao4x = preco + (preco * 20 / 100)
if escolha == 1:
    print('O valor de seu pagamento  é de R${:.2f} a vista com 10% de desconto é de R${:.2f}'.format(preco ,avista))
elif escolha == 2:
    print('Seu pagamento de R${:.2f} tera 5% de desconto seu valor agora é de R${:.2f} '.format(preco, avistacartao))
elif escolha == 3:
    print('Seu pagamento de R${:.2f} em até 3x no cartão não tem desconto '.format(preco))
elif escolha == 4:
    print('O Pagamento no valor de R${:.2f} tera 20% de juros a praso {:.2f}'.format(preco, cartao4x))
else:
    escolha = 0
    print('informação invalida, apenas 1, 2, 3, e 4')







