import random
primeiro = input('Primeiro aluno: ')
segundo = input('segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista =  [primeiro, segundo,terceiro,quarto]
random.shuffle(lista)
print(lista)