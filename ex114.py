import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('Deu ERRO')
else:
    print('Tudo Ok')
    print(site.read())