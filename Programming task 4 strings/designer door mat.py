n, m=input().split()
m=int(m)
n=int(n)
n//=2
l=0
for i in range(1,n+1,1):
    print((m-(((2*i)-1)*3))//2*'-'+((2*i)-1)*'.|.'+(m-(((2*i)-1)*3))//2*'-')
print((m-7)//2*'-'+'WELCOME'+(m-7)//2*'-')
for i in range(n,0,-1):
    print((m-(((2*i)-1)*3))//2*'-'+((2*i)-1)*'.|.'+(m-(((2*i)-1)*3))//2*'-')
