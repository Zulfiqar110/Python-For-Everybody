import urllib.request, urllib.parse, urllib.error
import re
hand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in hand:
    print(line.decode().strip())
