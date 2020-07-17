'''
Finding Numbers in a Haystack
'''

import re

#fh = open("regex_sum_42.txt")
fh = open("regex_sum_227440.txt")

sum = 0
i=0


for line in fh:
    line = line.strip()
    stuff = re.findall('([0-9]+)',line)
    if len(stuff) < 1 : continue
    for i in range(0, len(stuff)):
        sum = sum + int(stuff[i])

print(sum)



'''
import re
print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )


print( sum( [ ****** for x in **********('[0-9]+',open("regex_sum_227440.txt").read()) ] ) )
'''