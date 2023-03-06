def print_rangoli(n):
    alphabet=96
    for i in range(n,0,-1):
        print(((4*i)-4)//2*'-',end='')
        for j in range(n,i-1,-1):
            if(i==n):
                print(chr(alphabet+j),end='')
            else :
                print(chr(alphabet+j),'',sep='-',end='')
        for j in range(i+1,n+1,1):
            if(j==n):
                print(chr(alphabet+j),end='')
            else:            
                print(chr(alphabet+j),'',sep='-',end='')
        print(((4*i)-4)//2*'-')
    for i in range(2,n+1,1):
        print(((4*i)-4)//2*'-',end='')
        for j in range(n,i-1,-1):
            if(i==n):
                print(chr(alphabet+j),end='')
            else :
                print(chr(alphabet+j),'',sep='-',end='')
        for j in range(i+1,n+1,1):
            if(j==n):
                print(chr(alphabet+j),end='')
            else:            
                print(chr(alphabet+j),'',sep='-',end='')
        print(((4*i)-4)//2*'-')



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)