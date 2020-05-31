from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
hand = urllib.request.urlopen('http://www.dr-chuck.com').read()
soup = BeautifulSoup(hand,'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))