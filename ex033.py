primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))
# verificar o menor valor
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor= segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
print('o menor valor é {} '.format(menor))
# Verificar maior valor
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
print('E o maior valor é {} '.format(maior))