import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts
''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')



fh = open("mbox.txt")
for line in fh:
    if "From: " in line.strip():
        words = line.split()
        email = words[1]
        org = email.split('@')[1]
        
        cur.execute('select * from Counts where org = ?', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) values (?,1)',(org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 where org = ?',(org,))

        conn.commit()
    
sqlstr = 'SELECT org, count from Counts order by count desc'


for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
    