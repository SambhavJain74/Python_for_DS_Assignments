def func():
    count=0
    s=input()
    dog='dog'
    list1=s.split()
    for i in list1:
        if(i==dog):
            count+=1
    return count

print(func())