import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def demo(handl):
    soup = BeautifulSoup(handler, 'html.parser')
    tags = soup('a')
    name = list()
    for tag in tags:
        url = tag.get('href', None)
        name.append(url)
    print(f"Scraping ::{name[17]}")
    return name[17]

handler = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Bo.html').read()
for i in range(7):
    handler = urllib.request.urlopen(demo(handler))