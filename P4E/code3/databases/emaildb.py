import sqlite3


# connect/create database
conn = sqlite3.connect('emaildb.sqlite')

#get handle to database
cur = conn.cursor()



# drop if exists
cur.execute('''
DROP TABLE IF EXISTS Counts''')

# create table
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')


# insert data
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    #commit changes    
    conn.commit()


# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# rows in cur.execute(sqlstr)
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# close connection
cur.close()
