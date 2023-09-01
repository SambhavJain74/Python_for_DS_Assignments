s=input()
ampersand=0
upper=0
lower=0
for i in s:
    if('a'<=i<='z' or 'A'<=i<='Z'):
        if('a'<=i<='z'):
            lower+=1
        else:
            upper+=1
    elif(i=='&'):
        ampersand+=1
if(len(s)<5):
    print("password must contain at least 5 character")
if(ampersand<1):
    print("password must contain at least one '&' character")
if(upper<1):
    print("password must contain at least 1 uppercase letter")
if(lower<1):
    print("password must contain at least 1 lowercase letter")