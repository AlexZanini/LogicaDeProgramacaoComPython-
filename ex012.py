preco = float(input('Qual o preço do produto? R$'))
desconto = (preco * 5) /100
valor = preco - desconto
print('O produto que custava R${:.2f}, na promação de 5% de deconto custara R${:.2f} '.format(preco, valor))
