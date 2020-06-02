import json
import urllib.request, urllib.error, urllib.parse

while True :
    add = input("Enter Address :")
    if len(add)<2:  break
    aa = dict()
    s_url = 'http://py4e-data.dr-chuck.net/json?'
    aa['address'],aa['key'] = add, 42
    url = s_url + urllib.parse.urlencode(aa)
    hand = urllib.request.urlopen(url,None).read().decode()
    print(hand)