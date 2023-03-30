def notas(*n, sint=False):
    dicionario = {}
    dicionario['Toatal'] = len(n)
    dicionario['Maior'] = max(n)
    dicionario['Menor'] = min(n)
    dicionario ['Media'] = sum(n) / len(n)
    if sint:
        if dicionario['Media'] >= 7:
            dicionario['Sintuacao'] = 'BOA'
        elif dicionario['Media'] >= 5:
            dicionario['Media'] = 'Razoável'
        else:
            dicionario['Media'] = 'Ruim'
    return dicionario




#Programa principal
resp = notas(5.5, 4, 6, 7.4, sint=True)
print(resp)
