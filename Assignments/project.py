import urllib.request,urllib.error,urllib.parse
import json
import ssl
import sqlite3

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

API_KEY = 42
s_url = 'http://py4e-data.dr-chuck.net/json?'

connection = sqlite3.connect('project.sqlite')
crs = connection.cursor()
crs.executescript("""
DROP TABLE IF EXISTS Locations;
CREATE TABLE Locations(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Location TEXT UNIQUE,
    Address TEXT
);
""")

f_name = input('Enter file name :')
if len(f_name)<4:   f_name = 'where.data'
hand = open(f_name)
#new_file = open("Address",'a+')
ex = dict()

for location in hand:
    ex['address'], ex['key'] = location, API_KEY
    f_url = s_url + urllib.parse.urlencode(ex)

    url = urllib.request.urlopen(f_url, context=ctx)
    data = url.read().decode()
    print(f'Retrieving from {f_url}')
    try:
        json_data = json.loads(data)
    except:
        json_data = None
    if json_data is None or 'results' not in json_data or json_data['status'] != 'OK':
        print("Failed to retrieve...........")
        continue
    # print(json.dumps(json_data, indent=2))
    try:
        f_add = json_data['results'][0]["formatted_address"]
        crs.execute('INSERT INTO Locations (Location,Address) VALUES (?,?)',(location,f_add))
    except:
        pass
    #new_file.write(location+'::' + f_add +'\n')
connection.commit()