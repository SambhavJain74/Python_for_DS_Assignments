a=int(input())
b=int(input())
c=int(input())
avg=(a+b+c)/3
print("The average is ",avg)
print(["fail","pass"][avg>=40])
if(avg>=40):
    s="Pass"
else:
    s="Fail"

print(s)