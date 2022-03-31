def func(lst):
    if len(lst) == 1:
        return lst
 
    middle = (len(lst)+1)//2
    left = lst[:middle]
    right = lst[middle:]
 
    return play(func(left),  func(right))
 
def play(l, r):
    #무승부 
    if l[0][1] == r[0][1]:
        return l
    
    if l[0][1] == 1:
        if r[0][1] == 2:
            return r
        else:
            return l
    if l[0][1] == 2:
        if r[0][1] == 3:
            return r
        else:
            return l
    if l[0][1] == 3:
        if r[0][1] == 1:
            return r
        else:
            return l

T = int(input())
for t in range(1,T+1):
    N = int(input())
    lst = list(enumerate(list(map(int, input().split())), start=1))
    res = func(lst)
    print(f'#{t+1} {res[0][0]}')