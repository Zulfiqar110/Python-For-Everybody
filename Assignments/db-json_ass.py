import sqlite3, json

connection = sqlite3.connect('db-json.sqlite')
crs = connection.cursor()
crs.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id));
''')
f_name = input('Enter File name :: ')
if len(f_name)<3:   f_name = 'roster_data.json'
hand = open(f_name).read()
json_data = json.loads(hand)
for item in json_data:
    name,title,role = item[0],item[1],item[2]
    crs.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''', (name,))
    crs.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = crs.fetchone()[0]
    crs.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', (title,))
    crs.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = crs.fetchone()[0]
    crs.execute('''INSERT OR REPLACE INTO Member (user_id, course_id,role) VALUES ( ?, ?, ? )''',
                 (user_id, course_id, role))
connection.commit()
