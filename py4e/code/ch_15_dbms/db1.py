import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts
''')

cur.execute('''CREATE TABLE Counts(email TEXT, count INTEGER)''')


fh = open("mbox.txt")
for line in fh:
    if "From: " in line.strip():
        words = line.split()
        email = words[1]
        cur.execute('select * from Counts where email = ?', (email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (email, count) values (?,1)',(email,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 where email = ?',(email,))

        conn.commit()
    
sqlstr = 'SELECT email, count from Counts order by count desc'


for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
