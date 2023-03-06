if __name__ == '__main__':
    n = int(input())
    l = []
    for _ in range(n):
        lst = []
        name = input()
        score = float(input())
        l.append([name,score])
    
    min_score = min(l,key = lambda x:x[1])

    l = [l for l in l if l[1]>min_score[1]]

    second_min_score = min(l,key = lambda x : x[1])

    l = [l for l in l if l[1]==second_min_score[1]]

    my_new_list = sorted(l)

    for i in my_new_list:
        print(i[0])