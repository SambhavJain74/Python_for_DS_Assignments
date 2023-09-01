s=input()
list1=s.split()
s=""
for i in list1:
    t=chr(ord(i[0])-ord('a')+ord('A'))
    s+=t+i[1:]+" "

print(s)
    