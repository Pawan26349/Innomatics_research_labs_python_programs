if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(1,n+1,1):
        s=input().split()
        if(s[0]=="insert"):
            a.insert(int(s[1]),int(s[2]))
        elif(s[0]=="print"):
            print(a)
        elif(s[0]=="append"):
            a.append(int(s[1]))
        elif(s[0]=="sort"):
            a.sort()
        elif(s[0]=="pop"):
            a.pop()
        elif(s[0]=="reverse"):
            a.reverse()
        elif(s[0]=="remove"):
            a.remove(int(s[1]))
    