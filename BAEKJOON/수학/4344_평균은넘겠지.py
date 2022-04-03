N = int(input())

for i in range(N) :
    lst = list(map(int,input().split()))
    n = lst[0]
    lst = lst[1:]
    cnt = 0
    for j in range(len(lst)) :
        if lst[j] > sum(lst)/len(lst) :
            cnt +=1
    print('{0:0.3f}%'.format(cnt*100/len(lst)))