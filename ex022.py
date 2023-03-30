nome = str(input('Digite seu nome completo: ')).strip()
print('Seu neme com todas as letras maiúsculas:', nome.upper())
print('Seu nome com todas as letras minúsculas:', nome.lower())
'''print('Seu nome ao todo {} Letras'.format(len(nome)- nome.count(' ')))'''
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))