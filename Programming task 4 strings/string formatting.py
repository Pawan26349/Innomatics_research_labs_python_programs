def print_formatted(n):
    l=len(format(n,'0b'))
    for i in range(1,n+1,1):
        print(str(i).rjust(l,' '),format(i,'o').rjust(l,' '),format(i,'X').rjust(l,' '),format(i,'0b').rjust(l,' '))  

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)