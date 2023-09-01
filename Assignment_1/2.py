s=input()
list1=s.split()
s=input()
list2=s.split()
print(list1)
print(list2)
for i in list2:
    list1.append(i)

print(list1)