N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
dice = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0} 
# print(lst)
res = 0 
for i in range(6):
    result = [] 
    tmp = [1, 2, 3, 4, 5, 6] 
    tmp.remove(lst[0][i]) 
    tmp2 = lst[0][dice[i]]
    tmp.remove(tmp2) 
    result.append(max(tmp)) 
    for j in range(1, N): 
        tmp = [1, 2, 3, 4, 5, 6]
        tmp.remove(tmp2)
        tmp2 = lst[j][dice[lst[j].index(tmp2)]]
        tmp.remove(tmp2)
        result.append(max(tmp)) 
    result = sum(result) 
    if res < result: 
        res = result

print(res)
