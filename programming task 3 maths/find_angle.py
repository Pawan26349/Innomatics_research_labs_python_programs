import math 
ab=int(input())
bc=int(input())
ac=math.sqrt(math.pow(ab,2)+math.pow(bc,2))
ac/=2
adj=bc/2
output=int(round(math.degrees(math.acos(adj/ac))))
output=str(output)
print(output+"°")
