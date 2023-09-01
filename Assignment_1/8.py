s=input()
list2=s.split()
list1=['a','e','i','o','u','A','E','I','O','U']
list3=[]
for i in list2:
    s=""
    for j in i:
        if(j not in list1):
            s+=j
    list3.append(s)
    print(s)
maxlength=0
s=""
for i in list3:
    if(len(i)>maxlength):
        maxlength=len(i)
        s=i
print()
print(s)