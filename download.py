# Python 3 code
import urllib.request, urllib.parse, urllib.error
 
url = 'http://www.carlissongaldino.com.br/modules/pubdlcnt/pubdlcnt.php?file=http://www.carlissongaldino.com.br/sites/default/files/o-fantasma-da-opera.pdf&nid=1287'
 
print("baixando com urllib")
urllib.request.urlretrieve(url, "o-fantasma-da-opera-u.pdf")
 
print("baixando com urllib2")
f = urllib.request.urlopen(url)
data = f.read()
with open("o-fantasma-da-opera-u2.pdf", "wb") as code:
    code.write(data)