s=input()
list1=s.split('@')
s="The username is {username} and the domain is {domain}"
print(s.format(username=list1[0],domain=list1[1]))