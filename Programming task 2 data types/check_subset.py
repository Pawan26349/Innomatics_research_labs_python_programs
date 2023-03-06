t=int(input())
while(t!=0):
    n1=int(input())
    A=set(map(int,input().split()))
    n2=int(input())
    B=set(map(int,input().split()))
    print(A.issubset(B))
    t-=1
