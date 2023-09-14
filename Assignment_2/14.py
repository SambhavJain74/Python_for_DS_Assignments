d1={'a': 100, 'b': 200, 'c': 300}
done=False
for i in d1:
    if(d1[i]==200):
        print("Yes")
        done=True
        break
if(done==False):
    print("No")