lst = list()
lst1 = list()
f = open('romeo.txt','r')
for line in f:
    line2 = line.lstrip()
    lst1 = line2.split()
    #print(lst1)
    for word in lst1:
        #print(word)
        if lst.count(word) == 0:
            lst.append(word) 
        else:
            continue
        


lst.sort()
print(lst)