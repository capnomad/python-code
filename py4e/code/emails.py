fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

    
fh=  open(fname)
lst_emails=list()


for line in fh:
    if 'From ' in line:
        lst_line = line.split()
        #print(lst_line)
        lst_emails.append(lst_line[1])
        #print(lst_emails)
count=0
for email in lst_emails:
    print(email)
    count += 1


print("There were", count, "lines in the file with From as the first word")