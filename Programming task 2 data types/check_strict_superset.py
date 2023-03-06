A=set(map(int,input().split()))
n=int(input())
final=True
for i in range(0,n,1):
    l=set(map(int,input().split()))
    if not l.issubset(A):
        final=False
    if len(l)>=len(A):
        final=False
print(final)
