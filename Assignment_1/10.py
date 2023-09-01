n=int(input())
bin=0
list1=[]
while(n>0):
    list1.append(n%2)
    n=int(n/2)
for i in reversed(list1):
    bin=bin*10+i
print(bin)