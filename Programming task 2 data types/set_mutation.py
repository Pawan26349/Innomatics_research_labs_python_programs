n=int(input())
l=list(map(int,input().split()))
l=set(l)
num=int(input())
for i in range(0,num):
    s=list(input().split())
    l1=list(map(int,input().split()))
    l1=set(l1)
    if(s[0]=='intersection_update'):
        l.intersection_update(l1)
    if(s[0]=='update'):
        l.update(l1)
    if(s[0]=='difference_update'):
        l.difference_update(l1)
    if(s[0]=='symmetric_difference_update'):
        l.symmetric_difference_update(l1)

sum=0
for i in l:
    sum+=i
print(sum)
