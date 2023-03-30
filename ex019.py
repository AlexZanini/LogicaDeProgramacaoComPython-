import random
primeiro = input('Primeiro aluno: ')
segundo = input('segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista =  [primeiro, segundo,terceiro,quarto]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}: '.format(escolhido))


