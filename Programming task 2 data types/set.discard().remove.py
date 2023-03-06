n=int(input())
a=set(map(int,input().split()))
n1=int(input())
for i in range(1,n1+1,1):
    n=input().split()
    if(n[0]=="pop"):
        a.pop()
    elif(n[0]=="remove"):
        r=int(n[1])
        a.remove(r)
    elif(n[0]=="discard"):
        r=int(n[1])
        a.discard(r)
print(sum(a))
