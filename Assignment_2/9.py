def caught_speeding(n,t):
    add=[0,5][t]
    if(n<=60+add):
        return "No Challan"
    if(n<=80+add):
        return "Small Challan"
    return "Heavy Challan"

while(True):
    n=int(input("Enter speed\n"))
    t=int(input("Is it your birthday(0/1)\n"))
    print(caught_speeding(n,t)+"\n")