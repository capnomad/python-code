'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

d = dict()
lst_emails=list()

for line in fh:
    if 'From ' in line and 'From:' not in line:
        lst_words = line.split()
        d[lst_words[1]] = d.get(lst_words[1],0)+1


bigword = None
bigcount = None
for word,count in d.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount  =count

print(bigword,bigcount)
