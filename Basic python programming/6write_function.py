def is_leap(year):
    leap = False
    if(year%4==0):
        leap=True
        if(year%400):
            leap=False
            if(year%100):
                leap=True
    return leap

year = int(input())
print(is_leap(year))