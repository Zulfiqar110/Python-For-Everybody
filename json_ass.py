import urllib.request, urllib.parse, urllib.error
import json
url = input("Enter Location :: ")
if len(url)<5:  url = 'http://py4e-data.dr-chuck.net/comments_402692.json'
hand = urllib.request.urlopen(url,None).read().decode()
print(f"Retrieving :: {url}")
print(f'Retrieved:: {len(hand)} characters')
json_data = json.loads(hand)
sum_num = 0
for num in json_data['comments']:
    sum_num = int(num['count']) + sum_num
print(sum_num)