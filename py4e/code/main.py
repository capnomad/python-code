import constant

print(constant.PI)
print(constant.GRAVITY)

print("hello world")

a='abcdefghijKLMNOPqrstuVWXYZ'
print(a.lower())
print(a.capitalize())
print(a.upper())
print(a.find('p'))
print(a.find('P'))
print(a.replace('O','xx'))


#placeholder and string comparison
a='banana'
b=input()
if b == a:
    print("a = b")
elif b < a:
    print("%s comes before %s" % (b,a))
elif b > a:
    print("%s comes after %s" % (b,a))
