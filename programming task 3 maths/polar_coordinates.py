import math
import cmath
z=input()
z=list(z)
for i in range(0,len(z)):
    if(z[i].isalpha()):
        z.remove(z[i])
n1=z[0]
count=0
for i in range(1,len(z)):
    if(z[i].isnumeric()):
        n1+=z[i]
        count+=1
    else:
        break
count+=1
n2=z[count]
for i in range(count+1,len(z)):
    if(z[i].isnumeric()):
        n2+=z[i]
    else:
        break
n1=int(n1)
n2=int(n2)
sum1=math.pow(n1,2)+math.pow(n2,2)
sum1=math.pow(sum1,0.5)
print(sum1)
sum2=cmath.phase(complex(n1,n2))
print(sum2)





