s=input()
list1=s.split()
list2=[]
for i in list1:
    list2.append(int(i))
while(True):
    print("Press 0 to exit")
    print("Press 1 to insert element")
    print("Press 2 to delete element")
    n=int(input())
    if(n==0):
        break
    if(n==1):
        print("Enter the element to insert")
        ins=int(input())
        list2.append(ins)
        print(list2)
    if(n==2):
        print("Delete by value(0)")
        print("Delete by position(1))")
        print("Delete a slice(2)")
        opt=int(input())
        if(opt==0):
            print("Enter value to delete")
            val=int(input())
            list2.remove(val)
            print(list2)
        if(opt==1):
            print("Enter position to delete")
            pos=int(input())
            list2.pop(pos)
            print(list2)
        if(opt==2):
            print("Enter start pos")
            start=int(input())
            print("Enter end pos")
            end=int(input())
            while(end>=start):
                list2.pop(end)
            print(list2)