import xml.etree.ElementTree as e
import sqlite3

connection = sqlite3.connect('tracks.sqlite')
crs = connection.cursor()
crs.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')
f_name = input('Enter File name ::')
if len(f_name)<3:   f_name = 'tracks.xml'
hand = open(f_name).read()
tree = e.fromstring(hand)
stuff = tree.findall('dict/dict/dict')
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

for lst in stuff:
    if lookup(lst, 'Track ID') is None: continue
    name = lookup(lst, 'Name')
    artist = lookup(lst, 'Artist')
    album = lookup(lst, 'Album')
    count = lookup(lst, 'Play Count')
    rating = lookup(lst, 'Rating')
    length = lookup(lst, 'Total Time')
    genre = lookup(lst, 'Genre')
    if name is None or artist is None or album is None or genre is None:
        continue
    crs.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
    crs.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',(genre,))
    crs.execute('SELECT id FROM Artist WHERE name=?',(artist,))
    artist_id = crs.fetchone()[0]
    crs.execute('INSERT OR IGNORE INTO Album (artist_id,title) VALUES (?,?)',(artist_id,album))
    crs.execute('SELECT id FROM Album WHERE title=?',(album,))
    album_id = crs.fetchone()[0]
    crs.execute('SELECT id FROM Genre WHERE name=?',(genre,))
    genre_id = crs.fetchone()[0]
    # print(genre_id)
    crs.execute('''INSERT OR REPLACE INTO Track (title,album_id,genre_id,len,rating,count)
                VALUES (?,?,?,?,?,?)''',(name,album_id,genre_id,length,rating,count))
connection.commit()