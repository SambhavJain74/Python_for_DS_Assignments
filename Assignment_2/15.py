n=int(input("Enter the number of terms"))
n-=1
start=2
sum=0
while(n):
    sum+=start
    start=start*10+2
    n-=1
sum+=start
print(sum)