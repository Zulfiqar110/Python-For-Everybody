import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

API_KEY = 42
url = 'http://py4e-data.dr-chuck.net/json?'

while True:
    location = input('Enter Location :: ')
    if len(location) < 1: break
    l_api = dict()
    l_api["address"], l_api["key"] = location, API_KEY
    f_url = url + urllib.parse.urlencode(l_api)

    print('Retrieving', f_url)
    hand = urllib.request.urlopen(f_url, context=ctx)
    data = hand.read().decode()
    print(f"Retrieved :: {len(data)} characters")

    try:
        j_info = json.loads(data)
    except:
        j_info = None
    if not j_info or 'results' not in j_info or j_info['status']!="OK":
        print("Failed to Retrieve.......")
        print(data)
        continue
    print(json.dumps(j_info,indent=2))
    #Now Retrieving the data asked in assignment i.e place-id
    for item in j_info['results']:
        print(f"place_ID of {location} = {item['place_id']}")
