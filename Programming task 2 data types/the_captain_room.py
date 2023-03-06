from collections import Counter
n=int(input())
a=list(map(int,input().split()))
s=dict(Counter(a))
for i in s:
    if(s.get(i)==1):
        print(i)