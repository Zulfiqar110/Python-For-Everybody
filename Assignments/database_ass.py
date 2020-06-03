import sqlite3
connection = sqlite3.connect('mail_data.sqlite')
crs = connection.cursor()

crs.execute('DROP TABLE IF EXISTS Counts')
crs.execute('CREATE TABLE Counts (org TEXT,count INTEGER)')
name = input('Enter file name :: ')
if len(name)<3: name = 'mbox.txt'
hand = open(name)
for lines in hand:
    if not lines.startswith("From "):   continue
    email = lines.split()[1].split('@')[1]

    crs.execute('SELECT count FROM COUNTS WHERE org= ? ',(email,))
    row = crs.fetchone()
    if row is None:
        crs.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(email,))
    else:
        crs.execute('UPDATE Counts SET count=count + 1 WHERE org= ?',(email,))
connection.commit()
#Query for retrieving data from database
query = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in crs.execute(query):
    print(str(row[0]), row[1])
crs.close()