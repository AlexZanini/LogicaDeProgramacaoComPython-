def maior(* num):
    cont = 0
    maior = 0
    print ('\n Analisando os valore passados... ')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao total.')
    print(f'o maior valor inforado foi {maior}')




#programa principal
maior(2, 9, 5, 7, 1)
maior(4, 15, 52, 77, 11)
maior()