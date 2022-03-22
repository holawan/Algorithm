def heap(x) :
    global now 
    tree[now] = x
    child = now
    parents = child//2 

    while parents>=1 and tree[parents] > tree[child] :
        tree[parents],tree[child] = tree[child] , tree[parents]
        child = parents 
        parents = child//2 
    now += 1 

T = int(input())
for t in range(1,T+1) : 
    n = int(input())

    tree = [0] * (n+1) 

    now = 1
    value_lst = list(map(int,input().split()))


    for i in value_lst:
        heap(i)
    ans = 0
    while n >0 : 
        n //= 2 
        ans += tree[n]
    print(f'#{t} {ans}')


