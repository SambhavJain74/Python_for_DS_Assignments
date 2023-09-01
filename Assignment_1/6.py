print("Enter the number of students")
n=int(input())
list1=[]
username=[]
domains=[]
for i in range (0,n):
    s=input()
    list2=s.split('@')
    username.append(list2[0])
    domains.append(list2[1])

print(username)
print(domains)