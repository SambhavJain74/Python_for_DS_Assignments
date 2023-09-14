def func():
    s=input()
    dog='dog'
    list1=s.split()
    for i in list1:
        if(i==dog):
            return True
    return False

print(func())