from time import sleep
cor = ('\033[m',          # 0 - sem cores
        '\033[0:30:41m',  # 1 - vermelho
        '\033[0;30;42m',  # 2 - verde
        '\033[0:30:43m',  # 3 - amarelo
        '\033[0:30:44m',  # 4 - vermelho
        '\033[0:30:45m',  # 5 - roxo
        '\033[0:30:46m',  # 6 - branco
       )

def ajuda(com):
    titulo(f'Acessando o manual do comando  \'{com}\'', 4)
    print(cor[6], end='')
    help(com)
    print(cor[0], end='')
    sleep(2)

def titulo(msg, c=0):
    tam = len(msg) + 4
    print(cor[c], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cor[0], end='')
    sleep(1)

#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() =='FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)