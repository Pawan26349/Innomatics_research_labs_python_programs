def average(array):
    # your code goes here
    sum = 0 
    array = list(set(array))
    for i in array:
        sum+=i
    return (sum/len(array))
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)