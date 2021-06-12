# Python 3 code
import urllib.request, urllib.parse, urllib.error
 
url = 'https://mangalivre.net/baixar/jujutsu-kaisen/154977/capitulo-1'
 
print("baixando com urllib")
urllib.request.build_opener(url)
 
with open("o-fantasma-da-opera-u2.pdf", "wb") as code:
    code.write()