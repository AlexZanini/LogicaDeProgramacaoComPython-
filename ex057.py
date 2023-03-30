
sexo = str(input('Qual o seu sexo: [M/F} ')).strip().upper()[0]
while sexo not in 'MF':
    print('Dados invalidos digite apenas F ou M:')
    print('Digite novamente por favor:')
    sexo = str(input('Qual o seu sexo: [M/F} ')).strip().upper()[0]
if sexo == 'F':
        print('Seu sexo é Feminino ')
elif sexo == 'M':
        print('Seu sexo é Masculino ')

