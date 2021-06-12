import urllib.request
f = urllib.request.urlopen('http://www.python.org/')
print(f.read(300).decode('utf-8'))