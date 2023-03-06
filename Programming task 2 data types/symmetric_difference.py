n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))
final=s1.symmetric_difference(s2)
list(final)
positive=[]
negative=[]
for i in final:
    if(i>=0):
        positive.append(i)
    else:
        negative.append(i)
set(positive)
set(negative)
list(negative)
list(positive)
positive.sort()
f=negative+positive
for i in f:
    print(i)
