def voto(n):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - n
    if idade >= 18 and idade <= 65:
        return f'Com {idade} anos: Seu voto é obrigatorio'
    elif idade < 18:
        return f'Com {idade} anos: Não vota'
    else:
        return f'Com {idade} anos: Seu voto é opcional '

    
#programa principal
nascimento = int(input('Em que nao voce nasceu? '))
print(voto(nascimento))

