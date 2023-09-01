s=input()
alphabets=0
digits=0
symbols=0
upper=0
lower=0
for i in s:
    if('a'<=i<='z' or 'A'<=i<='Z'):
        alphabets+=1
        if('a'<=i<='z'):
            lower+=1
        else:
            upper+=1
    elif('0'<=i<='9'):
        digits+=1
    elif(i!=' '):
        symbols+=1

print("alphabets:",alphabets)
print("digits:",digits)
print("symbols:",symbols)
print("upper:",upper)
print("lower:",lower)