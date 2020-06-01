import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as e
# URL = http://py4e-data.dr-chuck.net/comments_402691.xml
url = input("Enter URL :: ")
if len(url) < 3:    url = 'http://py4e-data.dr-chuck.net/comments_402691.xml'

hand = urllib.request.urlopen(url,None).read()
print(f"Retieving ::{url}")
tree = e.fromstring(hand)
content = tree.findall('.//count')
sum_num = 0
for s_num in content:
    sum_num = sum_num + int(s_num.text)
print(sum_num)